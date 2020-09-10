import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

#calculate for overweight
#calc BMI by value = weight (kg) / (height (m))^2
#if value > 25, overweight (1), else (0)
#formula : if bmi > 25, yes (1) else no (0)


#populate overweight array
df['overweight'] = 0
df.loc[(df['weight']/(df['height'] / 100)**2 > 25),'overweight'] = 1
#print(df)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
#not correct ---- huh?
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] == 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Convert the data into long format // Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke','alco','active', 'overweight'], var_name = 'variable', value_name = 'value')


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    #my old code
    #df_cat = df_cat.groupby(by = 'cardio')['variables'].count()

    #someone else's code --- does it print? also explain logic please?
    df_cat['total'] = 1 #should be count value
    df_cat = df_cat.groupby(['variable', 'cardio', 'value'], as_index=False).count()
    

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot( x='variable', y='total',hue= 'value', col='cardio', data=df_cat, kind='bar')


    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap()



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
