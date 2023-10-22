# Function to create a single-touch attribution model - Last Touch Model
# Given a DataFrame 'dt' containing user interactions, 'conv_col' indicating conversions,
# and 'channel_col' for channels, this function calculates the last-touch attribution model.
# It selects the last interaction channel before conversion for each user and returns
# a DataFrame with channel weightage percentages.

def last_touch_model(dt, conv_col, channel_col):
    import pandas as pd
    
    # Extract rows where conversion is equal to 1
    last_touch = dt.loc[dt[conv_col] == 1]
    
    # Calculate channel weightage percentages and round to 2 decimal places
    res_last_touch = pd.DataFrame(round(last_touch[channel_col].value_counts(normalize=True) * 100, 2))
    res_last_touch.columns = ['Weightage(%)']
    
    return res_last_touch
