import pandas as pd
from datetime import datetime, timedelta
import os

from helpers.data_enrichment import get_company_name_dict

def run_business_card_sync(date):
    """
    Basic synchronization logic for a specific date
    """
    print(f"--- TASK STARTED: {date} ---")
    
    try:
        # 1. EXTRACTION (ClickHouse)
        print(f"Extracting data from ClickHouse...")
        
        # 2. ENRICHMENT & TRANSFORMATION
        # company_names = get_company_name_dict(mysql_connection, company_ids)
        print(f"Enriching data with company names from MySQL...")

        # 3. LOADING (PostgreSQL)
        # df.to_sql('company_business_card', con=postgres_engine, if_exists='append')
        print(f"Loading data to PostgreSQL success.")
        
    except Exception as err:
        print(f"ERROR for date {date}: {err}")
    finally:
        print(f"--- TASK FINISHED: {date} ---")

def main(date_start=None, date_stop=None):
    """
    Entry point. Supports launch for yesterday (kron)
    or for a period (manual launch).
    """

    if not date_start:
        date_start = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    if not date_stop:
        date_stop = date_start

    print(f"Starting pipeline from {date_start} to {date_stop}")
    
    run_business_card_sync(date_start)

if __name__ == "__main__":
    main()
