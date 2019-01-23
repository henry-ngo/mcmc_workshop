# generate_sample_data.py
# Creates a toy dataset for Session 1's emcee introduction

import numpy as np

# Define x values (part of our dataset)
x_val = np.array([0,1,2,6,9])

# Define true values based on a line with slope and intercept
true_slope = 1.3
true_intercept = 0.9
true_y_val = true_intercept + true_slope*x_val

# Define measured y_values with Gaussian errors
y_err = np.array([0.9,0.6,0.3,1.8,1.5])
y_val = np.random.normal(loc=true_y_val,scale=y_err)

# Write to file
np.savetxt('../sample_data.csv',np.column_stack((x_val,y_val,y_err)),delimiter=',',fmt='%0.2f', header='x,y,y_err')
