import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset='salary',keep='first',inplace=True)
    employee.sort_values(by='salary', ascending=False, inplace=True)
    if employee.shape[0] < N or N <= 0:
        ans = {'getNthHighestSalary('+str(N)+')': [None]}
    else:
        ans = {'getNthHighestSalary('+str(N)+')': [employee.iloc[N-1, 1]]}
    return pd.DataFrame(ans)
