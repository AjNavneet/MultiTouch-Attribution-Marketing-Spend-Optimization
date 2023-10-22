# Function to create a single-touch attribution model - Last Non-Direct Touch Model
# Given a DataFrame 'dt' containing user interactions, 'conv_col' indicating conversions,
# 'channel_col' for channels, and 'user_id' for user identifiers,
# this function calculates the last non-direct touch attribution model.
# It selects the last non-direct interaction channel for each user before conversion
# and returns a DataFrame with channel weightage percentages.

def last_non_direct_model(dt, conv_col, channel_col, user_id):
    import pandas as pd
    
    # Group by user and keep the last two observations for each user
    slp = pd.DataFrame(dt.groupby(user_id).tail(2)
    
    # Filter rows where conversions are equal to 1
    temp = slp.loc[slp[conv_col] == 1]
    
    # Group by user and keep the first observation for each user
    last_non_direct = pd.DataFrame(slp.groupby(user_id).first(), index=slp[user_id])
    
    # Create a list of user identifiers from 'temp'
    cookie_index = list(temp[user_id])
    
    # Locate user identifiers in the 'last_non_direct' dataframe
    mid_last_non_direct = last_non_direct.loc[cookie_index]
    
    # Calculate channel weightage percentages and round to 2 decimal places
    res_last_non_direct = pd.DataFrame(round(mid_last_non_direct[channel_col].value_counts(normalize=True) * 100, 2))
    res_last_non_direct.columns = ['Weightage(%)']
    
    return res_last_non_direct
