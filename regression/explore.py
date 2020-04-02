import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

# Write a function, plot_variable_pairs(dataframe) that plots all of the pairwise relationships along with the regression line for each pair.
def plot_variable_pairs(df):
    """
    Takes:
          df
    Returns:
          PairGrid plot of all relationships
          histogram and scatter plots
    """
    g = sns.PairGrid(df)
    g = g.map_diag(sns.distplot) # distplot for a single variable
    g = g.map_offdiag(sns.regplot) # regression line + scatter plot for 2 vars
    g



# Write a function, months_to_years(tenure_months, df) that returns your dataframe with a new feature tenure_years, in complete years as a customer.
def months_to_years(df):
      """
      Takes:
            df
      Returns:
            df with new feature "tenure_years"
      """
      df["tenure_years"] = round(df.tenure // 12).astype(object)
      return df



# Write a function, plot_categorical_and_continous_vars(categorical_var, continuous_var, df), that outputs 3 different plots for plotting a categorical variable with a continuous variable.
def plot_categorical_and_continuous_vars(categorical_var, continuous_var, df):
      """
      Takes:
            df
      Returns:
            three plots of categorical var with continuous var
      """
      plt.suptitle(f'{continuous_var} by {categorical_var}', fontsize=18)
      
      sns.lineplot(x=categorical_var, y=continuous_var, data=df)
      plt.xlabel(categorical_var, fontsize=12)
      plt.ylabel(continuous_var, fontsize=12)
      plt.show()
      
      
      sns.catplot(x=categorical_var, y=continuous_var, data=df, kind="swarm", palette='Blues')
      plt.xlabel(categorical_var, fontsize=12)
      plt.ylabel(continuous_var, fontsize=12)
      plt.show()
      
      sns.catplot(x=categorical_var, y=continuous_var, data=df, kind="bar", palette='Purples')
      plt.xlabel(categorical_var, fontsize=12)
      plt.ylabel(continuous_var, fontsize=12)
      plt.show()