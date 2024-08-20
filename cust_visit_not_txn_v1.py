import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_df = visits.merge(transactions, how = "left", on = "visit_id")
    filtered_df = merged_df.where(merged_df.transaction_id.isna())
    return filtered_df.groupby("customer_id").size().reset_index(name='count_no_trans')