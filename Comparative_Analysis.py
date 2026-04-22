import pandas as pd
import numpy as np

file_path = r"C:\Users\lenovo\.cache\kagglehub\datasets\muhammadroshaanriaz\most-popular-programming-languages-2004-2024\versions\1\Most Popular Programming Languages.csv"
df = pd.read_csv(file_path)
df['Month'] = pd.to_datetime(df['Month'])

# CONFIG
student_id = 351 # <--- PALITAN MO
languages = sorted(['C#', 'Flutter', 'Java', 'JavaScript', 'Matlab', 'PhP', 'Python', 'React', 'Swift', 'TypeScript'])
idx_a = (student_id % 1000) % 10
idx_b = (idx_a + 1) % 10
lang_a, lang_b = languages[idx_a], languages[idx_b]

col_a = [c for c in df.columns if lang_a in c][0]
col_b = [c for c in df.columns if lang_b in c][0]

# CALCULATIONS
p3_df = df[['Month', col_a, col_b]].copy()
p3_df.columns = ['Month', 'Lang_A', 'Lang_B']
corr = np.corrcoef(p3_df['Lang_A'], p3_df['Lang_B'])[0,1]
dom_ratio = (len(p3_df[p3_df['Lang_A'] > p3_df['Lang_B']]) / len(p3_df)) * 100

print(f"=== PART 3: {lang_a} vs {lang_b} ===")
print(f"Correlation: {corr:.4f}")
print(f"Dominance Ratio ({lang_a} > {lang_b}): {dom_ratio:.2f}%")