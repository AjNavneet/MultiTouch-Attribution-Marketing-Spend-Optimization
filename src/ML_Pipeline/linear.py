# Function to create a multi-touch attribution model - Linear Model
# Given a DataFrame 'dt' containing user interactions, 'conv_col' indicating conversions,
# 'channel_col' for channels, and 'user_id' for user identifiers, this function implements
# the linear attribution model. It calculates weightages for each channel based on the
# number of interactions with channels and returns a DataFrame with channel weightage percentages.

def linear_model(dt, conv_col, channel_col, user_id):
    import pandas as pd
    from collections import Counter
    
    # Filter data for users who convert
    pd.options.mode.chained_assignment = None 
    temp = dt.loc[dt[conv_col] == 1]
    cookie_index = list(temp[user_id])
    dt['new'] = dt[user_id].isin(cookie_index)      
    y = dt['new'].isin([True])
    dt_conv = dt[y]

    # Keep the last interaction for each user who converts
    temp = pd.DataFrame(dt_conv.groupby(user_id).tail(1)
    
    # Calculate the number of interactions (click count) for each user
    x = Counter(dt_conv[user_id])
    temp['click_count'] = x.values()

    temp.set_index(user_id, inplace=True)
    
    # Add click count to the filtered data
    count = Counter(dt_conv[user_id])
    dt_conv['clicks'] = dt_conv[user_id].map(count)
    
    # Assign weightages in a linear fashion
    dt_conv = dt_conv.assign(click_per=lambda x: round(100 / dt_conv['clicks'], 2))

    # Get the mean weightage of every channel
    res_linear = dt_conv.groupby(channel_col, as_index=False)['click_per'].mean()
    
    # Calculate total weightage sum
    total_weightage_sum = res_linear['click_per'].sum()
    
    # Calculate channel weightage percentages
    res_linear['Weightage(%)'] = res_linear.apply(lambda x: round((x['click_per'] / total_weightage_sum) * 100, 2), axis=1)
    
    res_linear.drop(['click_per'], inplace=True, axis=1)
    res_linear = res_linear.set_index(channel_col)
    res_linear.index.name = None
    
    return res_linear
