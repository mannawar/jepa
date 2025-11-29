import pandas as pd

# Path to your original CSV
input_csv = "/Users/mannawarhussain/Desktop/my_video_dataset_clean.csv"

# Path to save the converted CSV
output_csv = "/Users/mannawarhussain/Desktop/my_video_dataset_clean_space.csv"

# Read the original CSV (comma-separated)
df = pd.read_csv(input_csv, header=None)

# Save it as space-separated
df.to_csv(output_csv, sep=' ', header=False, index=False)

print(f"Converted CSV saved at: {output_csv}")
