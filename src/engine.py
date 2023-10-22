from matplotlib import pyplot as plt
from ML_Pipeline import last_touch
from ML_Pipeline import data_prep
from ML_Pipeline import plot_data
from ML_Pipeline import first_touch
from ML_Pipeline import last_non_direct
from ML_Pipeline import linear
from ML_Pipeline import u_shaped
from ML_Pipeline import position_decay
from ML_Pipeline import markov
from ML_Pipeline import shapley
from ML_Pipeline import optimization

import pandas as pd
import numpy as np

# Import CSV file as PD
dt = data_prep.Import("../input/attribution_data.csv")


# User-input for required columns to be used in function arguments
user_id = input("Enter user-id column name : ")
conv_col = input("Enter conversion column name : ")
channel_col = input("Enter channel column name : ")

print("--------------------------------------MODELS-----------------------------------------------------")

# Pass Through model 1
last_touch_out=last_touch.last_touch_model(dt, conv_col, channel_col)
print (last_touch_out)

# Plot output of model 1
'''plot_data.plotter(last_touch_out,'last_touch')'''

print("-------------------------------------------------------------------------------------------------")

# Pass Through model 2
first_touch_out=first_touch.first_touch_model(dt, conv_col,channel_col,user_id)
print (first_touch_out)

# Plot output of model 2
'''plot_data.plotter(first_touch_out,'first_touch')'''

print("-------------------------------------------------------------------------------------------------")

# Pass Through model 3
last_non_direct_out=last_non_direct.last_non_direct_model(dt, conv_col,channel_col,user_id)
print (last_non_direct_out)

# Plot output of model 3
'''plot_data.plotter(last_non_direct_out,'last_non_direct')'''

print("-------------------------------------------------------------------------------------------------")

# Pass Through model 4
linear_out=linear.linear_model(dt, conv_col,channel_col,user_id)
print (linear_out)

# Plot output of model 4
'''plot_data.plotter(linear_out,'linear')'''

print("-------------------------------------------------------------------------------------------------")

# Pass Through model 5
u_shaped_out=u_shaped.u_shaped_model(dt, conv_col,channel_col,user_id)
print (u_shaped_out)

# Plot output of model 5
'''plot_data.plotter(u_shaped_out,'u_shaped')'''

print("-------------------------------------------------------------------------------------------------")

# Pass Through model 6
position_decay_out=position_decay.pos_decay_model(dt, conv_col,channel_col,user_id)
print (position_decay_out)

# Plot output of model 6
'''plot_data.plotter(position_decay_out,'position_decay')'''

print("-------------------------------------------------------------------------------------------------")

# Pass Through model 7
markov_out=markov.markov_model(dt, conv_col,channel_col,user_id)
print (markov_out)

# Plot output of model 7
'''plot_data.plotter(markov_out,'markov')'''

print("-------------------------------------------------------------------------------------------------")

# Pass Through model 8
shapley_out=shapley.shapley_model(dt, conv_col,channel_col,user_id)
print (shapley_out)

# Plot output of model 8
'''plot_data.plotter(shapley_out,'shapley')'''

print("--------------------------------------OVER-------------------------------------------------------")

print("NOTE: Barplots are saved in output folder.")

# result evaluation 
Combined_dataframe = pd.concat([last_touch_out,first_touch_out,last_non_direct_out,linear_out,u_shaped_out,position_decay_out,markov_out,shapley_out],axis=1)
Combined_dataframe.columns=['Last-Touch','First-Touch','Last-Non-direct','Linear','U-shaped','Position Decay','Markov','Shapley']
Combined_dataframe['Mean'] = round(Combined_dataframe.mean(axis=1),2)
Combined_dataframe

# plot the graphs
'''
plt.clf()
X_axis = np.arange(len(first_touch_out.index))
plt.bar(X_axis - 0.2, last_touch_out['Weightage(%)'],0.2,label='last touch')
plt.bar(X_axis , first_touch_out['Weightage(%)'],0.2,label='first touch')
plt.bar(X_axis + 0.2, last_non_direct_out['Weightage(%)'],0.2,label='last non-direct touch')
plt.xticks(X_axis, first_touch_out.index)
plt.legend()
plt.savefig('../output/Combined_Models/Single-Touch_Models.png')
plt.clf()

print()
X_axis = np.arange(len(first_touch_out.index))
plt.bar(X_axis - 0.2, linear_out['Weightage(%)'],0.2,label='linear model')
plt.bar(X_axis , u_shaped_out['Weightage(%)'],0.2,label='U-shaped model')
plt.bar(X_axis + 0.2, position_decay_out['Weightage(%)'],0.2,label='position decay model')
plt.xticks(X_axis, first_touch_out.index)
plt.legend()
plt.savefig('../output/Combined_Models/Multi-Touch_Models.png')
plt.clf()
print()

X_axis = np.arange(len(markov_out.index))
plt.bar(X_axis - 0.2, markov_out['Weightage(%)'],0.4,label='markov-chain model model')
plt.bar(X_axis + 0.2, shapley_out['Weightage(%)'],0.4,label='shapley value model')
plt.xticks(X_axis, first_touch_out.index)
plt.legend()
plt.savefig('../output/Combined_Models/Probabilistic_Models.png')
plt.clf()
'''

# build budget optimization engine
coeff_A = Combined_dataframe['Mean'].tolist()
ch_names=list(sorted(Combined_dataframe.index))
budget=int(input("Enter campaign budget: "))
optimization.optimize(budget,coeff_A,ch_names)