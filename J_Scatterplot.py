import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load data
df = pd.read_csv('chlamydia_by_state.csv')

# Clean and prepare data
# Assuming 'Rate' needs to be converted from string to float, and 'Year' is already in correct format
df['Rate'] = pd.to_numeric(df['Rate'], errors='coerce')  # Convert 'Rate' to float, coerce errors to NaN

# Filter data for a specific state, e.g., California
state_data = df[df['Geography'] == 'California']

# Remove rows with NaN values in 'Rate' or 'Year' if any
state_data = state_data.dropna(subset=['Year', 'Rate'])

# Get x and y for plotting
x = state_data['Year']
y = state_data['Rate']

# Calculate regression line
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regression_line = slope * x + intercept

# Create scatter plot
plt.scatter(x, y, color='blue', label='Observed Data')

# Add regression line
plt.plot(x, regression_line, color='red', label=f'Regression Line: y={slope:.2f}x+{intercept:.2f}')
plt.xlabel('Year')
plt.ylabel('Chlamydia Rate per 100,000 Population')
plt.title('Chlamydia Rate in California Over Time')
plt.legend()

# Show the plot
plt.show()


