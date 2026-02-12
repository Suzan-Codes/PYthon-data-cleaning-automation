# main.py
from cleaner import clean_csv
from scraper import scrape_sample

def main():
    print("Starting Lead Data Automation...\n")

    scrape_sample()

    clean_csv(
        input_file="messy_leads.csv",
        output_file="cleaned_leads.csv"
    )

    print("\nProcess completed successfully.")

if __name__ == "__main__":
    main()
