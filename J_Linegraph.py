import pandas as pd
import matplotlib.pyplot as plt

# Assuming data is already loaded into a DataFrame called df
# For example:
# df = pd.read_csv('path_to_your_data.csv')
df = pd.read_csv('Chlamydia_by_state.csv')
# Select a specific state for visualization, e.g., California
data_california = df[df['Geography'] == 'California']

# Convert 'Year' to datetime if it's not already
data_california['Year'] = pd.to_datetime(data_california['Year'], format='%Y')

# Sort by Year if not sorted
data_california = data_california.sort_values('Year')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data_california['Year'], data_california['Rate'], marker='o', linestyle='-', color='b')
plt.title('Chlamydia Rates Over Time in California')
plt.xlabel('Year')
plt.ylabel('Rate per 100,000 Population')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.tight_layout()  # Adjust layout to make room for the rotated date labels

plt.show()

