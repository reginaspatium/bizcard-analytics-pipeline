import pandas as pd

def get_company_name_dict(connection, company_ids):
    """
    The function gets company names from MySQL by their ID.
    This allows you to replace numeric IDs in reports with human-readable names.
    """
    if not company_ids:
        return {}
        
    # Convert to list
    ids_str = ", ".join(map(str, company_ids))
    
    # Query a table with companies
    query = f"SELECT user_id as company_id, name FROM company_catalog WHERE user_id IN ({ids_str})"
    
    # Convert to dict
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            df = pd.DataFrame(result)
            if not df.empty:
                return df.set_index('company_id')['name'].to_dict()
    except Exception as e:
        print(f"Error fetching company names: {e}")
        
    return {}
