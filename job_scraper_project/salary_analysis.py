import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load scraped job data
df = pd.read_csv("indeed_jobs.csv")

# Add a dummy 'Salary' column (Modify this based on real scraped data)
df['Salary'] = [
    "₹5,00,000 - ₹7,00,000", "₹4,00,000", "₹6,50,000 - ₹8,00,000", 
    "₹5,50,000 - ₹6,50,000", "₹4,20,000 - ₹5,00,000", "₹7,00,000", 
    np.nan, "₹6,00,000 - ₹9,00,000", "₹5,00,000", "₹6,00,000"
]

# Function to convert salary strings to numeric values
def parse_salary(salary):
    if pd.isna(salary):
        return np.nan
    salary = salary.replace("₹", "").replace(",", "").split("-")
    salary = [int(s.strip()) for s in salary]
    return np.mean(salary)  # Average if range, else single value

# Apply function to Salary column
df["Salary"] = df["Salary"].apply(parse_salary)

# Remove rows with no salary data
df = df.dropna(subset=["Salary"])

# Perform Salary Analysis
average_salary = np.mean(df["Salary"])
median_salary = np.median(df["Salary"])
min_salary = np.min(df["Salary"])
max_salary = np.max(df["Salary"])

print(f"📌 Average Salary: ₹{average_salary:,.2f}")
print(f"📌 Median Salary: ₹{median_salary:,.2f}")
print(f"📌 Min Salary: ₹{min_salary:,.2f}")
print(f"📌 Max Salary: ₹{max_salary:,.2f}")

# Plot Salary Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Salary"], bins=5, color="skyblue", edgecolor="black")
plt.axvline(average_salary, color="red", linestyle="dashed", linewidth=2, label="Avg Salary")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Jobs")
plt.title("Salary Distribution for Python Developer Jobs")
plt.legend()
plt.show()