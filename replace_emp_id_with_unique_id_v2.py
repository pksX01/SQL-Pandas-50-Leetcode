import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employees.join(employee_uni.set_index('id'), how='left', on=['id'])[['unique_id', 'name']]