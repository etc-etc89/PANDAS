import pandas as pd

# Create the data
data = {
    'Name': ['Aarav', 'Meera', 'Vivaan', 'Ananya', 'Kabir', 'Diya', 'Ishaan', 'Riya', 'Aditya', 'Sanya'],
    'English': [88, 76, 90, 85, 67, 92, 73, 89, 84, 77],
    'Math': [95, 82, 91, 75, 70, 89, 78, 88, 90, 72],
    'Science': [85, 78, 88, 92, 66, 94, 81, 87, 90, 79],
    'History': [75, 80, 85, 79, 68, 88, 74, 81, 82, 77],
    'Computer': [92, 84, 95, 87, 71, 96, 80, 89, 93, 85],
    'Hindi': [78, 88, 82, 84, 76, 90, 70, 86, 83, 79],
    'Physical_Education': [90, 85, 93, 89, 80, 95, 84, 91, 92, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("🔹 Student Report Card:\n")
print(df)

print("\n🔹 Basic Statistics:\n")
print(df.describe())

# Average marks per student (exclude 'Name' column)
df['Average'] = df.loc[:, 'English':'Physical_Education'].mean(axis=1)

print("\n🔹 Average Marks per Student:\n")
print(df[['Name', 'Average']])

# Highest scorer in each subject (include all subject columns)
print("\n🔹 Toppers in Each Subject:\n")
for subject in df.columns[1:-1]:  # columns from 'English' to 'Physical_Education'
    topper = df[df[subject] == df[subject].max()]
    print(f"{subject}: {topper['Name'].values[0]} ({df[subject].max()})")

# Overall topper
overall_topper = df[df['Average'] == df['Average'].max()]
print(f"\n🏆 Overall Topper: {overall_topper['Name'].values[0]} with average {overall_topper['Average'].values[0]:.2f}")

# Subject-wise average
print("\n🔹 Subject-wise Average:\n")
print(df.loc[:, 'English':'Physical_Education'].mean())

# Students who scored below 75 in any subject
print("\n🔹 Students who scored below 75 in any subject:\n")
mask = (df.loc[:, 'English':'Physical_Education'] < 75).any(axis=1)
print(df[mask][['Name']])
