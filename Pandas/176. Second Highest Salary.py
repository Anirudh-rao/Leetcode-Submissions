import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salary = employee['salary'].drop_duplicates().sort_values(ascending = False)
    second_highest = distinct_salary.iloc[1] if len(distinct_salary) > 1 else None
    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})
    return result_df