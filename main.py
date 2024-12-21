import pandas as pd
import os

current_folder = os.getcwd()

for file_name in os.listdir(current_folder):
    if file_name.endswith(".json"):
        try:
            json_path = os.path.join(current_folder, file_name)

            with open(json_path, encoding="utf-8-sig") as inputfile:
                df = pd.read_json(inputfile)

            csv_name = file_name.replace(".json", ".csv")
            csv_path = os.path.join(current_folder, csv_name)

            df.to_csv(csv_path, encoding="utf-8-sig", index=False)
            print(f"Converted: {file_name} -> {csv_name}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("All JSON files have been processed!")
