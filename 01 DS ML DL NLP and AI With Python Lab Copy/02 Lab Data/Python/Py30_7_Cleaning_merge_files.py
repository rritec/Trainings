import pandas as pd
emp_df1 = pd.read_csv('emp_merge.csv')
dept_df2 = pd.read_csv('dept_merge.csv')
# Merge two DataFrames: emp_dept
emp_dept = pd.merge(left=emp_df1, right=dept_df2, on=None,left_on='DEPTNO', right_on='DEPTID')
# Print emp_dept
print(emp_dept)
