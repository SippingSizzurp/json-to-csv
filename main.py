import pandas as pd
import os

current_folder = os.getcwd()

for file_name in os.listdir(current_folder):
    if file_name.endswith(".json"):
        try:
            json_path = os.path.join(current_folder, file_name)

            # Read JSON in chunks for large files
            df = pd.read_json(json_path, encoding="utf-8-sig", chunksize=10000)
            
            # Create CSV file
            csv_name = file_name.replace(".json", ".csv")
            csv_path = os.path.join(current_folder, csv_name)
            
            # Write chunks to CSV
            first_chunk = True
            for chunk in df:
                chunk.to_csv(csv_path, 
                           encoding="utf-8-sig",
                           index=False,
                           mode='w' if first_chunk else 'a',
                           header=first_chunk)
                first_chunk = False
            print(f"Converted: {file_name} -> {csv_name}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("All JSON files have been processed!")
