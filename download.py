import kagglehub
import os

# 1. Download the dataset
path = kagglehub.dataset_download("muhammadroshaanriaz/most-popular-programming-languages-2004-2024")

print("--- DOWNLOAD COMPLETE ---")
print("Your files are located here:", path)

# 2. List the files inside that folder to make sure the CSV is there
files = os.listdir(path)
print("Files in folder:", files)