import pandas as pd
import numpy as np
import os

# 1. SETUP & LOADING
file_path = r"C:\Users\lenovo\.cache\kagglehub\datasets\muhammadroshaanriaz\most-popular-programming-languages-2004-2024\versions\1\Most Popular Programming Languages.csv"
df = pd.read_csv(file_path)

# 2. LANGUAGE ASSIGNMENT (Siguraduhin mong tama yung ID mo dito)
student_id = 351
last_three_digits = student_id % 1000
languages = sorted(['C#', 'Flutter', 'Java', 'JavaScript', 'Matlab', 'PhP', 'Python', 'React', 'Swift', 'TypeScript'])
lang_index = last_three_digits % 10
assigned_language = languages[lang_index]

print(f"--- ANALYZING: {assigned_language} ---\n")

# 3. DATA CLEANING & PREPARATION
# I-convert ang 'Month' column sa datetime format
df['Month'] = pd.to_datetime(df['Month'])

# Hanapin yung column na naglalaman ng assigned language mo
# (Kasi minsan may "Worldwide (%)" na text sa column name)
target_col = [col for col in df.columns if assigned_language in col][0]

# Isolate the data
growth_df = df[['Month', target_col]].copy()
growth_df.rename(columns={target_col: 'Popularity'}, inplace=True)

# 4. CALCULATIONS
# Compute month-to-month growth rate (%)
growth_df['Growth_Rate'] = growth_df['Popularity'].pct_change() * 100

# Calculate rolling statistics (12-month window para sa long-term trend)
growth_df['Moving_Avg'] = growth_df['Popularity'].rolling(window=12).mean()
growth_df['Moving_STD'] = growth_df['Popularity'].rolling(window=12).std()

# 5. CLASSIFY GROWTH PHASES (NumPy Logic)
# Threshold: > 5% is Growth, < -5% is Decline, rest is Stable
conditions = [
    (growth_df['Growth_Rate'] > 5),
    (growth_df['Growth_Rate'] < -5),
    (growth_df['Growth_Rate'].between(-5, 5))
]
choices = ['Growth phase', 'Decline phase', 'Stable phase']
growth_df['Phase'] = np.select(conditions, choices, default='Stable phase')

# 6. STATISTICAL SUMMARIES
stat_summary = growth_df['Popularity'].describe()
phase_counts = growth_df['Phase'].value_counts()

# Overall Growth (First vs Last record)
initial_val = growth_df['Popularity'].iloc[0]
final_val = growth_df['Popularity'].iloc[-1]
overall_growth_pct = ((final_val - initial_val) / initial_val) * 100

# 7. OUTPUTS
print("--- DATAFRAME OUTPUT (Tail) ---")
print(growth_df.tail(10))

print("\n--- STATISTICAL SUMMARY TABLE ---")
print(stat_summary)

print("\n--- GROWTH PHASE COUNTS ---")
print(phase_counts)

print("\n--- KEY PERFORMANCE METRICS ---")
print(f"Initial Popularity: {initial_val}%")
print(f"Final Popularity: {final_val}%")
print(f"Overall Growth: {overall_growth_pct:.2f}%")