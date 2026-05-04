import pandas as pd
from datetime import datetime, timedelta

from helpers.data_enrichment import get_company_name_dict


def extract_data(date_start, date_stop):
    """
    Simulated extraction step (ClickHouse).
    In production this would execute SQL query.
    """
    print("Extracting data from ClickHouse...")

    # demo data instead of real DB
    df = pd.DataFrame({
        "date": [date_start, date_start],
        "company_id": [1, 2],
        "total_view": [120, 80],
        "unique_view": [100, 60],
        "total_click": [30, 10],
        "unique_click": [25, 8],
        "click_action": ["Показ візитки", "Клік на заголовок"]
    })

    return df


def enrich_data(df):
    """
    Enrichment step (MySQL).
    Replace company_id with company_name.
    """
    print("Enriching data with company names...")

    company_ids = df["company_id"].unique().tolist()

    # demo instead of real MySQL
    company_names = {
        1: "Company A",
        2: "Company B"
    }

    df["company_name"] = df["company_id"].map(company_names).fillna("Unknown")

    return df.drop(columns=["company_id"])


def load_data(df):
    """
    Load step (PostgreSQL).
    """
    print("Loading data to PostgreSQL...")

    # simulate insert
    print(df.head())


def run_business_card_sync(date_start, date_stop):
    print(f"--- TASK STARTED: {date_start} ---")

    try:
        df = extract_data(date_start, date_stop)
        df = enrich_data(df)
        load_data(df)

    except Exception as err:
        print(f"ERROR: {err}")

    finally:
        print(f"--- TASK FINISHED ---")


def main(date_start=None, date_stop=None):

    if not date_start:
        date_start = datetime.now() - timedelta(days=1)
    else:
        date_start = datetime.strptime(date_start, "%Y-%m-%d")

    if not date_stop:
        date_stop = date_start
    else:
        date_stop = datetime.strptime(date_stop, "%Y-%m-%d")

    current_date = date_start

    while current_date <= date_stop:
        run_business_card_sync(
            current_date.strftime("%Y-%m-%d"),
            current_date.strftime("%Y-%m-%d")
        )
        current_date += timedelta(days=1)


if __name__ == "__main__":
    main()
