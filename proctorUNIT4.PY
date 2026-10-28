import pandas as pd
import matplotlib.pyplot as plt

# Load employee data
df = pd.read_csv("employee.csv")


print("Employee Details:")
print(df[["Name", "Department", "Salary"]])

avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary of Each Department:")
print(avg_salary)

# Generate and display the bar chart
avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
