# JSON to CSV Converter

This Python script converts all valid JSON files in the current directory to CSV format. It reads each `.json` file, parses its content, and generates a corresponding `.csv` file with the same base name.

---

## Features

- Processes all JSON files in the current directory.
- Handles invalid or empty JSON files gracefully.
- Skips files that are unreadable or inaccessible due to permission issues.
- Provides detailed error messages for debugging.
- Outputs converted CSV files in the same directory as the script.

---

## Requirements

- Python 3.6 or later
- Required library: `pandas`

Install the dependencies using:
```bash
pip install pandas
