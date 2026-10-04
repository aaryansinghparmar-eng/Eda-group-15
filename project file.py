
# ==========================================
# ODI Cricket Dataset Analysis
# File: odb new.csv
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# 1. READ THE CSV FILE
# ------------------------------------------

file_path = "odb new.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("=" * 50)

# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# ------------------------------------------
# 2. BASIC DATASET INFORMATION
# ------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------------
# 3. DATA CLEANING
# ------------------------------------------

# Remove unnecessary index column if present
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Remove leading/trailing whitespace from column names
df.columns = df.columns.str.strip()

# Remove whitespace from player names
df["Player"] = df["Player"].str.strip()

# Convert numeric columns to numeric data types
numeric_columns = [
    "Mat", "Inns", "NO", "Runs", "Ave",
    "BF", "SR", "100", "50", "0", "4s", "6s"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Convert Highest Score (HS)
# Remove * from not-out scores
df["HS_numeric"] = (
    df["HS"]
    .astype(str)
    .str.replace("*", "", regex=False)
    .replace("nan", pd.NA)
)

df["HS_numeric"] = pd.to_numeric(
    df["HS_numeric"], errors="coerce"
)

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# 4. TOP 10 PLAYERS BY RUNS
# ------------------------------------------

top_runs = df.sort_values(
    by="Runs",
    ascending=False
).head(10)

print("\nTop 10 Players by Runs:")
print(
    top_runs[["Player", "Runs", "Mat", "Ave"]]
    .to_string(index=False)
)

# ------------------------------------------
# 5. TOP 10 PLAYERS BY BATTING AVERAGE
# ------------------------------------------

top_average = df.sort_values(
    by="Ave",
    ascending=False
).head(10)

print("\nTop 10 Players by Batting Average:")
print(
    top_average[["Player", "Ave", "Runs"]]
    .to_string(index=False)
)

# ------------------------------------------
# 6. TOP 10 PLAYERS BY STRIKE RATE
# ------------------------------------------

top_strike_rate = df.sort_values(
    by="SR",
    ascending=False
).head(10)

print("\nTop 10 Players by Strike Rate:")
print(
    top_strike_rate[["Player", "SR", "Runs"]]
    .to_string(index=False)
)

# ------------------------------------------
# 7. PLAYER WITH MOST CENTURIES
# ------------------------------------------

top_centuries = df.sort_values(
    by="100",
    ascending=False
).head(10)

print("\nTop 10 Players by Centuries:")
print(
    top_centuries[["Player", "100", "Runs"]]
    .to_string(index=False)
)

# ------------------------------------------
# 8. PLAYER WITH MOST SIXES
# ------------------------------------------

top_sixes = df.sort_values(
    by="6s",
    ascending=False
).head(10)

print("\nTop 10 Players by Sixes:")
print(
    top_sixes[["Player", "6s", "Runs"]]
    .to_string(index=False)
)

# ------------------------------------------
# 9. CORRELATION ANALYSIS
# ------------------------------------------

correlation_columns = [
    "Mat", "Inns", "Runs", "Ave",
    "BF", "SR", "100", "50", "4s", "6s"
]

correlation_matrix = df[correlation_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# ------------------------------------------
# 10. DATA VISUALIZATION
# ------------------------------------------

sns.set_theme(style="whitegrid")

# Chart 1: Top 10 Players by Runs

plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_runs,
    x="Runs",
    y="Player"
)

plt.title("Top 10 ODI Players by Total Runs")
plt.xlabel("Total Runs")
plt.ylabel("Player")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 2: Top 10 Players by Strike Rate
# ------------------------------------------

plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_strike_rate,
    x="SR",
    y="Player"
)

plt.title("Top 10 Players by Strike Rate")
plt.xlabel("Strike Rate")
plt.ylabel("Player")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 3: Runs vs Batting Average
# ------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Ave",
    y="Runs",
    size="Mat",
    hue="SR",
    palette="viridis",
    sizes=(30, 300)
)

plt.title("Runs vs Batting Average")
plt.xlabel("Batting Average")
plt.ylabel("Total Runs")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 4: Centuries Distribution
# ------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="100",
    bins=15,
    kde=True
)

plt.title("Distribution of ODI Centuries")
plt.xlabel("Number of Centuries")
plt.ylabel("Number of Players")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 5: Correlation Heatmap
# ------------------------------------------

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Cricket Statistics")

plt.tight_layout()
plt.show()

# ------------------------------------------
# 11. EXPORT RESULTS
# ------------------------------------------

top_runs.to_csv(
    "top_10_players_by_runs.csv",
    index=False
)

top_average.to_csv(
    "top_10_players_by_average.csv",
    index=False
)

top_strike_rate.to_csv(
    "top_10_players_by_strike_rate.csv",
    index=False
)

top_centuries.to_csv(
    "top_10_players_by_centuries.csv",
    index=False
)

print("\nAnalysis completed successfully!")
print("Results saved as CSV files.")