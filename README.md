# Lead Data Cleaning & Automation (Python)

## Project Overview
This project demonstrates automated cleaning of messy CSV/Excel lead data using Python.
It handles duplicate records, missing values, inconsistent formatting, and produces a clean,
ready-to-use dataset suitable for CRM, marketing, and reporting.

## Problem
Raw lead data often contains:
- Duplicate entries
- Missing email or phone values
- Inconsistent column formatting
- Manual cleaning effort that wastes time

## Solution
A Python-based automation workflow was built to:
- Load raw CSV data
- Remove duplicate records
- Fix missing values
- Normalize column names
- Export a cleaned CSV automatically

## Before vs After (Proof)
Screenshots showing:
- Raw messy CSV data
- Cleaned and structured CSV output
- Terminal execution proof
**Before:** Raw, messy CSV data with duplicates and missing values  
![Messy CSV](proof/messy_csv_preview.png)

**After:** Cleaned and structured data using Python automation  
![Cleaned CSV](proof/cleaned_csv_preview.png)

**Execution Proof:** Terminal output showing automated processing  
![Terminal Output](proof/terminal_output.png)


## Tools & Technologies
- Python
- Pandas
- Requests
- BeautifulSoup (sample scraping integration)

## Output
The final cleaned file (`cleaned_leads.csv`) is ready for business use and can be integrated
into CRM systems or further automation pipelines.


