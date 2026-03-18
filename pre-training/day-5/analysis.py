import pandas as pd

df = pd.read_csv("titanic.csv")

# Q1
print("\nQ1 - Survival counts and %")
counts = df['Survived'].value_counts()
pct = counts / len(df) * 100

print("Survived:", counts[1], f"({pct[1]:.1f}%)")
print("Died:", counts[0], f"({pct[0]:.1f}%)")

# Q2
print("\nQ2 - Survival rate by class")
class_map = {1: "1st", 2: "2nd", 3: "3rd"}
rates = df.groupby('Pclass')['Survived'].mean() * 100

for c in rates.index:
    print(class_map[c], "class:", f"{rates[c]:.1f}%")

# Q3
print("\nQ3 - Avg age (survived vs died)")
avg_age = df.groupby('Survived')['Age'].mean()

print("Survived avg age:", round(avg_age[1], 1))
print("Died avg age:", round(avg_age[0], 1))

# Q4
print("\nQ4 - Port with highest survival")
ports = df.groupby('Embarked')['Survived'].mean() * 100
top_port = ports.idxmax()

print("Top port:", top_port, f"({ports[top_port]:.1f}%)")

# Q5
print("\nQ5 - Missing ages")
print("Before:", df['Age'].isnull().sum())

df['Age'] = df.groupby('Pclass')['Age'].transform(
    lambda x: x.fillna(x.median())
)

print("After:", df['Age'].isnull().sum())

# Q6
print("\nQ6 - Oldest survivor")
oldest = df[df['Survived'] == 1].sort_values('Age', ascending=False).iloc[0]

print("Name:", oldest['Name'])
print("Age:", int(oldest['Age']))
print("Class:", class_map[oldest['Pclass']])

# Q7
print("\nQ7 - Survival by gender")
gender_rates = df.groupby('Sex')['Survived'].mean() * 100

for g in gender_rates.index:
    print(g, f"{gender_rates[g]:.1f}%")

# Q8
print("\nQ8 - Survival by age group")


def get_age_group(age):
    if age < 18:
        return "Child"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"


df['AgeGroup'] = df['Age'].apply(get_age_group)

group_rates = df.groupby('AgeGroup')['Survived'].mean() * 100

for g in group_rates.index:
    print(g, f"{group_rates[g]:.1f}%")

# Q9
print("\nQ9 - 3rd class survival by gender")
third = df[df['Pclass'] == 3]
third_rates = third.groupby('Sex')['Survived'].mean() * 100

for g in third_rates.index:
    print(g, f"{third_rates[g]:.1f}%")

# Q10
print("\nQ10 - Cabin missing drop")
original = len(df)
df2 = df.dropna(subset=['Cabin'])

print("Original:", original)
print("Remaining:", len(df2))
print("Kept %:", round(len(df2) / original * 100, 1))
