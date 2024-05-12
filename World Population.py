import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
excel_file = r"F:\Data Science internship\Book1.xlsx"
data = pd.read_excel(excel_file)

# Extract the "World Pop" row
world_pop_row = data.loc[data.iloc[:, 0] == "World Pop"].squeeze()

# Extract years and population data
years = world_pop_row.index[1:]
population = world_pop_row.values[1:]

# Create a bar plot
plt.figure(figsize=(12, 6))  # Adjust figure size for better spacing
bars = plt.bar(years, population, color='skyblue', width=0.8)  # Change color to blue and adjust width for spacing

# Add data labels on each bar with some spacing
for bar, pop in zip(bars, population):
    plt.text(bar.get_x() + bar.get_width() / 2, pop + 0.05 * max(population), str(int(pop)), ha='center')

# Customize labels and title
plt.xlabel('Year')
plt.title('World Population Over Years')

# Remove y-axis scale
plt.gca().axes.get_yaxis().set_visible(False)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()  # Adjust layout to prevent overlapping elements
plt.show()
