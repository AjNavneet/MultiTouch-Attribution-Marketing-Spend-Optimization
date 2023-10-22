# Function to create probabilistic multi-touch attribution model - markov model
# Given a DataFrame 'df' containing user interactions, 'conv_col' indicating conversions,
# 'channel_col' for channels, and 'user_id' for user identifiers, this function implements
# the Markov attribution model. It calculates weightages for each channel based on Markov chains
# and returns a DataFrame with channel weightage percentages.

def markov_model(df, conv_col, channel_col, user_id):
    import pandas as pd
    import numpy as np
    from collections import defaultdict
    from collections import Counter

    # Define functions for transition states, probabilities, matrix, removal effects, and allocations.

    def transition_states(list_of_paths):
        # Create all possible transition states between channels.
        list_of_unique_channels = set(x for element in list_of_paths for x in element)
        transition_states = {x + '>' + y: 0 for x in list_of_unique_channels for y in list_of_unique_channels}

        # Calculate the frequencies of transition combinations.
        for possible_state in list_of_unique_channels:
            if possible_state not in ['Conversion', 'Null']:
                for user_path in list_of_paths:
                    if possible_state in user_path:
                        indices = [i for i, s in enumerate(user_path) if possible_state in s]
                        for col in indices:
                            transition_states[user_path[col] + '>' + user_path[col + 1]] += 1
        return transition_states

    def transition_prob(trans_dict, list_of_paths):
        # Assign probabilities to each combination of paths of length 2.
        list_of_unique_channels = set(x for element in list_of_paths for x in element)
        trans_prob = defaultdict(dict)
        for state in list_of_unique_channels:
            if state not in ['Conversion', 'Null']:
                counter = 0
                index = [i for i, s in enumerate(trans_dict) if state + '>' in s]
                for col in index:
                    if trans_dict[list(trans_dict)[col]] > 0:
                        counter += trans_dict[list(trans_dict)[col]]
                for col in index:
                    if trans_dict[list(trans_dict)[col]] > 0:
                        state_prob = float((trans_dict[list(trans_dict)[col]])) / float(counter)
                        trans_prob[list(trans_dict)[col]] = state_prob
        return trans_prob

    def transition_matrix(list_of_paths, transition_probabilities):
        # Create a transition matrix using the probabilities of each path of length 2.
        trans_matrix = pd.DataFrame()
        list_of_unique_channels = set(x for element in list_of_paths for x in element)
        for channel in list_of_unique_channels:
            trans_matrix[channel] = 0.00
            trans_matrix.loc[channel] = 0.00
            trans_matrix.loc[channel][channel] = 1.0 if channel in ['Conversion', 'Null'] else 0.0

        for key, value in transition_probabilities.items():
            origin, destination = key.split('>')
            trans_matrix.at[origin, destination] = value
        return trans_matrix

    def removal_effects(dt, conversion_rate):
        # Calculate the effect of removing each channel.
        removal_effects_dict = {}
        channels = [channel for channel in dt.columns if channel not in ['Start', 'Null', 'Conversion']]
        for channel in channels:
            removal_dt = dt.drop(channel, axis=1).drop(channel, axis=0)
            for column in removal_dt.columns:
                row_sum = np.sum(list(removal_dt.loc[column]))
                null_pct = float(1) - row_sum
                if null_pct != 0:
                    removal_dt.loc[column]['Null'] = null_pct
                removal_dt.loc['Null']['Null'] = 1.0

            removal_to_conv = removal_dt[
                ['Null', 'Conversion']].drop(['Null', 'Conversion'], axis=0)
            removal_to_non_conv = removal_dt.drop(
                ['Null', 'Conversion'], axis=1).drop(['Null', 'Conversion'], axis=0)

            removal_inv_diff = np.linalg.inv(
                np.identity(
                    len(removal_to_non_conv.columns)) - np.asarray(removal_to_non_conv))
            removal_dot_prod = np.dot(removal_inv_diff, np.asarray(removal_to_conv))
            removal_cvr = pd.DataFrame(removal_dot_prod,
                                    index=removal_to_conv.index)[[1]].loc['Start'].values[0]
            removal_effect = 1 - removal_cvr / conversion_rate
            removal_effects_dict[channel] = removal_effect
        return removal_effects_dict

    def markov_chain_allocations(removal_effects, total_conversions):
        re_sum = np.sum(list(removal_effects.values()))

        return {k: (v / re_sum) * total_conversions for k, v in removal_effects.items()}


    pd.options.mode.chained_assignment = None 
    df = df.sort_values(user_id)
    df['visit_order'] = df.groupby(user_id).cumcount() + 1

    df_paths = df.groupby(user_id)[channel_col].aggregate(lambda x: x.unique().tolist()).reset_index()
    df_last_interaction = df.drop_duplicates(user_id, keep='last')[[user_id, conv_col]]
    df_paths = pd.merge(df_paths, df_last_interaction, how='left', on=user_id)

    df_paths['start'] = [["Start"] for i in range(len(df_paths[conv_col]))]
    df_paths['buff'] = [["Conversion"] for i in range(len(df_paths[conv_col]))]
    df_paths['null'] = [["Null"] for i in range(len(df_paths[conv_col]))]


    df_paths['path'] = np.where(df_paths[conv_col] == 0, df_paths['start'] + df_paths[channel_col] + df_paths['null'], df_paths['start'] + df_paths[channel_col] + df_paths['buff'])
    df_paths = df_paths[[user_id, 'path']]

    list_of_paths = df_paths['path']
    total_conversions = np.sum(a.count('Conversion') for a in df_paths['path'].tolist())
    base_conversion_rate = total_conversions / len(list_of_paths)

    trans_states = transition_states(list_of_paths)
    trans_prob = transition_prob(trans_states, list_of_paths)
    trans_matrix = transition_matrix(list_of_paths, trans_prob)
    removal_effects_dict = removal_effects(trans_matrix, base_conversion_rate)    #Creating a dictionary of the removal effect

    attributions = markov_chain_allocations(removal_effects_dict, total_conversions)    #Allocating markov chains
    res_markov=pd.DataFrame(attributions.values(),index=attributions.keys())
    res_markov.columns=['weightage']
    sum=res_markov['weightage'].sum()
    res_markov['Weightage(%)']=res_markov.apply(lambda x: round((x['weightage']/sum)*100,2),axis=1)
    res_markov.drop(['weightage'], axis=1,inplace=True)
    res_markov=res_markov.sort_index()
    return res_markov