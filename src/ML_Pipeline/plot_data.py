# Function to plot and save graphs of channel weightage
# Given a 'data' DataFrame containing weightage percentages for channels and a 'name' for the plot title,
# this function uses Matplotlib and Seaborn to create a bar plot of the weightage and saves it as a PNG image.

def plotter(data, name):
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Create a bar plot to visualize the weightage with respect to channels
    plt.subplots(figsize=(18, 6))
    p = sns.barplot(y='Weightage(%)', x=data.index, data=data)
    p.set_title(name)

    # Save the plot as a PNG image in the '../output/' directory
    p.figure.savefig(f"../output/{name}.png")
