from vega_datasets import data
data = data.sf_temps()

'''
Use the above dataset for the exercises below:


Write the code necessary to visualize the minimum temperature over time.
Write the code necessary to visualize the maximum temperature over time.
Which month is the coldest, on average?
Which month has the highest average temperature?
Resample by the day and calculate the min and max temp for the day (Hint: .agg(['min', 'max'])). Use this resampled dataframe to calculate the change in temperature for the day. Which month has the highest daily temperature variability?
Bonus: Visualize the daily min, average, and max temperature over time on a single line plot, i.e. the min, average, and maximum temperature should be 3 seperate lines.
'''

# 1.) Resample by the day and take the average temperature. Visualize the average temperature over time.

