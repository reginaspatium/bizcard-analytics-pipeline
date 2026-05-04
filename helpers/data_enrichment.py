def get_company_name_dict(connection, company_ids):
    if not company_ids:
        return {}

    placeholders = ", ".join(["%s"] * len(company_ids))

    query = f"""
        SELECT user_id as company_id, name
        FROM company_catalog
        WHERE user_id IN ({placeholders})
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, company_ids)
            result = cursor.fetchall()

            df = pd.DataFrame(result)
            if not df.empty:
                return df.set_index('company_id')['name'].to_dict()

    except Exception as e:
        print(f"Error fetching company names: {e}")

    return {}
