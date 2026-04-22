import pandas as pd
import numpy as np

file_path = r"C:\Users\lenovo\.cache\kagglehub\datasets\muhammadroshaanriaz\most-popular-programming-languages-2004-2024\versions\1\Most Popular Programming Languages.csv"
df = pd.read_csv(file_path)
df['Month'] = pd.to_datetime(df['Month'])

# CONFIG
student_id = 351 # <--- PALITAN MO
languages = sorted(['C#', 'Flutter', 'Java', 'JavaScript', 'Matlab', 'PhP', 'Python', 'React', 'Swift', 'TypeScript'])
assigned_lang = languages[(student_id % 1000) % 10]
target_col = [c for c in df.columns if assigned_lang in c][0]

# CALCULATIONS
p2_df = df[['Month', target_col]].copy()
p2_df.columns = ['Month', 'Popularity']
p2_df['Growth_Rate'] = p2_df['Popularity'].pct_change() * 100
mean_g, std_g = p2_df['Growth_Rate'].mean(), p2_df['Growth_Rate'].std()

lc_cond = [
    (p2_df['Growth_Rate'] > 0) & (p2_df['Growth_Rate'] < mean_g),
    (p2_df['Growth_Rate'] > mean_g),
    (p2_df['Growth_Rate'].abs() <= 1),
    (p2_df['Growth_Rate'] < 0) & (p2_df['Growth_Rate'] < (-1 * std_g))
]
p2_df['Lifecycle_Phase'] = np.select(lc_cond, ['Introduction', 'Growth', 'Maturity', 'Decline'], default='Stable/Transition')

print(f"=== PART 2: {assigned_lang} LIFECYCLE ===")
print(p2_df[['Month', 'Popularity', 'Lifecycle_Phase']].tail(10))
print("\nCOUNT PER PHASE:")
print(p2_df['Lifecycle_Phase'].value_counts())