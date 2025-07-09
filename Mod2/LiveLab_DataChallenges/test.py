# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create the dataset
data = {
    'Day': list(range(1, 11)),
    'Visitors': [100, 120, 110, 130, 150, 140, 160, 170, 180, 175],
    'Signups': [5, 8, 6, 10, 12, 11, 13, 15, 16, 14]
}

df = pd.DataFrame(data)

# Optional: Set Seaborn style
sns.set_style(style="whitegrid")

# Create a figure with 4 rows and 2 columns to make 8 visuals
fig, axs = plt.subplots(4, 2, figsize=(12, 16))
fig.suptitle("Matplotlib vs Seaborn Visualizations", fontsize=16)

# Task 1: Line chart of Visitors over Time -- Matplotlib
axs[0, 0].plot(df['Day'], df['Visitors'], marker='o', color='blue')
axs[0, 0].set_title("Matplotlib: Visitors Over Time")
axs[0, 0].set_xlabel("Day")
axs[0, 0].set_ylabel("Visitors")
# Task 2: Histogram of Signups -- MatplotLib
axs[1, 0].hist(df['Signups'], bins=5, color='orange', edgecolor='black')
axs[1, 0].set_title("Matplotlib: Signup Distribution")
axs[1, 0].set_xlabel("Signups")
axs[1, 0].set_ylabel("Frequency")



plt.show()