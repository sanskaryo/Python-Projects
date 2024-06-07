import pandas as pd


import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Sansk\Downloads\SA2024_W1_Pokemon.csv")

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Plot 1: Distribution of Attack
plt.figure(figsize=(10, 6))
sns.histplot(df['Attack'], kde=True)
plt.title('Distribution of Attack')
plt.xlabel('Attack')
plt.ylabel('Frequency')
plt.show()

# Plot 2: Scatter plot of Attack vs Defense
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Attack', y='Defense', data=df, hue='Legendary')
plt.title('Attack vs Defense')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.legend(title='Legendary')
plt.show()

# Plot 3: Box plot of Speed by Generation
plt.figure(figsize=(10, 6))
sns.boxplot(x='Generation', y='Speed', data=df)
plt.title('Speed by Generation')
plt.xlabel('Generation')
plt.ylabel('Speed')
plt.show()

# Plot 4: Count plot of Pokémon types
plt.figure(figsize=(14, 8))
sns.countplot(y='Type 1', data=df, order=df['Type 1'].value_counts().index)
plt.title('Count of Pokémon Types')
plt.xlabel('Count')
plt.ylabel('Type 1')
plt.show()