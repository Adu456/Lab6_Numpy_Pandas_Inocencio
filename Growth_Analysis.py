import pandas as pd
import numpy as np

file_path = r"C:\Users\lenovo\.cache\kagglehub\datasets\muhammadroshaanriaz\most-popular-programming-languages-2004-2024\versions\1\Most Popular Programming Languages.csv"
df = pd.read_csv(file_path)
df['Month'] = pd.to_datetime(df['Month'])

# CONFIG
student_id = 351 # <--- PALITAN MO
last_three = student_id % 1000
languages = sorted(['C#', 'Flutter', 'Java', 'JavaScript', 'Matlab', 'PhP', 'Python', 'React', 'Swift', 'TypeScript'])
assigned_lang = languages[last_three % 10]
target_col = [c for c in df.columns if assigned_lang in c][0]

# CALCULATIONS
p1_df = df[['Month', target_col]].copy()
p1_df.columns = ['Month', 'Popularity']
p1_df['Growth_Rate'] = p1_df['Popularity'].pct_change() * 100
p1_df['Moving_Avg'] = p1_df['Popularity'].rolling(window=12).mean()
p1_df['Moving_STD'] = p1_df['Popularity'].rolling(window=12).std()

cond = [(p1_df['Growth_Rate'] > 5), (p1_df['Growth_Rate'] < -5)]
p1_df['Phase'] = np.select(cond, ['Growth phase', 'Decline phase'], default='Stable phase')

print(f"=== PART 1: {assigned_lang} ===")
print(p1_df.tail(10))
print("\nSTATISTICAL SUMMARY:")
print(p1_df['Popularity'].describe())
print(f"\nOVERALL GROWTH: {((p1_df['Popularity'].iloc[-1] - p1_df['Popularity'].iloc[0])/p1_df['Popularity'].iloc[0]*100):.2f}%")