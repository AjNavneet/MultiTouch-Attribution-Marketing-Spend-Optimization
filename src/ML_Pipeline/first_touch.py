# Function to create a single-touch attribution model - First Touch Model

def first_touch_model(dt, conv_col, channel_col, user_id):
    import pandas as pd
    temp = dt.loc[dt[conv_col] == 1]  # Save the dataframe where all the conversions are 1 into the 'temp' variable
    first_touch = pd.DataFrame(dt.groupby(user_id).first(), index=dt[user_id])  # Grouping with respect to the user and keeping only the first instance of every user
    cookie_index = list(temp[user_id])  # Make a list of the user identifier column of 'temp'
    mid_first_touch = first_touch.loc[cookie_index]  # Locate user identifiers in the 'first_touch' dataframe
    res_first_touch = pd.DataFrame(round(mid_first_touch[channel_col].value_counts(normalize=True) * 100, 2))  # Calculate channel weightage
    res_first_touch.columns = ['Weightage(%)']
    return res_first_touch
