import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/sample_data.csv")

# Basic statistics
print(data.describe())

# Visualization
plt.figure()
plt.plot(data['Month'], data['Value'])
plt.xlabel("Month")
plt.ylabel("Values")
plt.title("Monthly Data Visualization")
plt.show()
