import pandas as pd

# Path to your current space-separated dataset
input_csv = "/Users/mannawarhussain/Desktop/my_video_dataset.csv"

# Path to save the cleaned CSV
output_csv = "/Users/mannawarhussain/Desktop/my_video_dataset_clean.csv"

# Read the space-separated dataset
df = pd.read_csv(input_csv, header=None, sep=r'\s+')

# Make sure there are exactly 2 columns: filepath and label
if df.shape[1] != 2:
    raise ValueError(f"Expected 2 columns, got {df.shape[1]}")

# Strip any extra whitespace from strings
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Save as a proper CSV with comma separator
df.to_csv(output_csv, index=False, header=False)

print(f"Cleaned dataset saved to: {output_csv}")
