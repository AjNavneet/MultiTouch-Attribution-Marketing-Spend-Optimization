# Function to create a probabilistic attribution model - Shapley Model
# Given a DataFrame 'df' containing user interactions, 'conv_col' indicating conversions,
# 'channel_col' for channels, and 'user_id' for user identifiers, this function implements
# the Shapley attribution model to calculate channel weightages based on their contributions to conversions.


def shapley_model(df, conv_col, channel_col, user_id):

    import pandas as pd
    import numpy as np
    from collections import defaultdict
    from collections import Counter
    import itertools
    from itertools import permutations,combinations


    def power_set(List):

        #Creating a power set of a given list
        PS = [list(j) for i in range(len(List)) for j in itertools.combinations(List, i+1)]
        return PS

    def subsets(s):
        '''
        This function returns all the possible subsets of a set of channels.
        input :
                - s: a set of channels.
        '''

        if len(s)==1:
            return s
        else:
            sub_channels=[]
            for i in range(1,len(s)+1):
                sub_channels.extend(map(list,itertools.combinations(s, i)))
        return list(map(",".join,map(sorted,sub_channels)))

    def v_function(A,C_values):
        '''
        This function computes the worth of each coalition.
        inputs:
                - A : a coalition of channels.
                - C_values : A dictionnary containing the number of conversions that each subset of channels has yielded.
        '''
        subsets_of_A = subsets(A)
        #print(subsets_of_A)
        #exit()
        worth_of_A=0
        for subset in subsets_of_A:
            #print("subset:", subset)
            if subset in C_values:
                #print("subset:", subset, "; Value:", C_values[subset])
                worth_of_A += C_values[subset]
        return worth_of_A

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def calculate_shapley(df, col_name):
        '''
        This function returns the shapley values
                - df: A dataframe with the two columns: ['channels_subset', 'conversion_sum'].
                - col_name: A string that is the name of the column with conversions in the dataframe
                **Make sure that that each value in channel_subset is in alphabetical order. Facebook,Paid Search and Paid Search,Facebook are the same 
                in regards to this analysis and should be combined under Facebook,Paid Search.
                ***Be careful with the distinct number of channels because this can signifcantly slow the perfomance of this function.
        '''
        
        c_values = df.set_index("channels_subset").to_dict()[col_name]
        df['channels'] = df['channels_subset'].apply(lambda x: x if len(x.split(",")) == 1 else np.nan)
        channels = list(df['channels'].dropna().unique())
        
        v_values = {}
        for A in power_set(channels):
            v_values[','.join(sorted(A))] = v_function(A,c_values)
        #print(v_values)
        n=len(channels)
        shapley_values = defaultdict(int)
        for channel in channels:
            for A in v_values.keys():
                #print(A)
                if channel not in A.split(","):
                    #print(channel)
                    cardinal_A=len(A.split(","))
                    A_with_channel = A.split(",")
                    A_with_channel.append(channel)            
                    A_with_channel=",".join(sorted(A_with_channel))
                    # Weight = |S|!(n-|S|-1)!/n!
                    weight = (factorial(cardinal_A)*factorial(n-cardinal_A-1)/factorial(n))
                    # Marginal contribution = v(S U {i})-v(S)
                    contrib = (v_values[A_with_channel]-v_values[A]) 
                    shapley_values[channel] += weight * contrib
            # Add the term corresponding to the empty set
            shapley_values[channel]+= v_values[channel]/n 
            
        return shapley_values

    dt_paths = df.sort_values(channel_col).groupby(user_id)[channel_col].aggregate(lambda x: x.unique().tolist()).reset_index()
    dt_paths['channels']=[str(x) for x in dt_paths[channel_col]]
    channel_count=Counter(dt_paths['channels'])
    channel_ct=pd.DataFrame(channel_count.items())
    channel_ct[0] =  channel_ct[0].apply(lambda x: x.replace('[','').replace(']','').replace("'","").replace(", ",","))
    channel_ct.columns=['channels_subset','conversion_sum']
    attribution=calculate_shapley(channel_ct,'conversion_sum')
    res_shapley=pd.DataFrame(attribution.values(),index=attribution.keys())
    res_shapley.columns=['weightage']
    sum=res_shapley['weightage'].sum()
    res_shapley['Weightage(%)']=res_shapley.apply(lambda x: round((x['weightage']/sum)*100,2),axis=1)
    res_shapley.drop(['weightage'], axis=1,inplace=True)
    res_shapley = res_shapley.sort_index()
    return res_shapley