# cleaner.py
import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    print(f"Loaded rows: {len(df)}")

    # remove duplicate rows
    df = df.drop_duplicates()
    print(f"After deduplication: {len(df)}")

    # fix missing values
    df = df.fillna("Not Available")

    # normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    df.to_csv(output_file, index=False)
    print(f"Cleaned file saved as {output_file}")
