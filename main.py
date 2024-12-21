import pandas as pd
import os
import sys


current_folder = os.getcwd()
def is_valid_json_file(filename: str) -> bool:
    return (not filename.startswith('.') and
            filename.endswith('.json') and
            os.path.isfile(filename) and
            os.access(filename, os.R_OK))

json_files = [f for f in os.listdir(current_folder) if is_valid_json_file(f)]
if not json_files:
    print("No valid JSON files found in the current directory.")
    input("Press enter to continue. . .")
    sys.exit(0)
for file_name in json_files:
        try:
            json_path = os.path.join(current_folder, file_name)

            with open(json_path, encoding="utf-8-sig") as inputfile:
                df = pd.read_json(inputfile)

            csv_name = file_name.replace(".json", ".csv")
            csv_path = os.path.join(current_folder, csv_name)

            df.to_csv(csv_path, encoding="utf-8-sig", index=False)
            print(f"Converted: {file_name} -> {csv_name}")

        except pd.errors.EmptyDataError:
            print(f"Error: {file_name} is empty or has invalid JSON structure")
        except pd.errors.ParserError:
            print(f"Error: {file_name} contains invalid JSON format")
        except PermissionError:
            print(f"Error: Permission denied accessing {file_name}")
        except MemoryError:
            print(f"Error: Not enough memory to process {file_name}")
        except Exception as e:
            print(f"Unexpected error processing {file_name}: {str(e)}")
            print("Please report this issue with the stack trace below:")
            import traceback
            print(traceback.format_exc())
            input("Press enter to continue. . .")

input(f"Processing complete! Successfully processed {successful_count} out of {len(json_files)} files.\nPress enter to continue. . .")
