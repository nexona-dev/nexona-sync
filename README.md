# Nexona Sync - Shopify to Google Sheets Automation

A Python automation script that syncs product data (ID, title, price, stock) from a Shopify store to a Google Sheets spreadsheet. This tool eliminates manual data entry and ensures your reporting is always up-to-date.

## Features
- Fetches all products from Shopify API
- Writes data to Google Sheets automatically
- Configurable sync schedule
- Handles API rate limits

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Configure your Shopify API credentials and Google Sheets credentials.
3. Run: `python sync.py`

## Tech Stack
Python, Shopify API, Google Sheets API, Requests, Gspread
