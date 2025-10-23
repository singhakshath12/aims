# this is data generated from chatgpt specifically for Ordinal Encoding, One Hot Encoding and Imputation Techniques. 
# clearly we can see Department, Gender, City will be used for one hot encoding since they hold no specific order.
# Education, Job Position, Performance Rating will be used for ordinal encoding since they can be ordered.
# Experience, Salary will be used for imputation since they have missing values


```python
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Marketing', 'Finance'],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Bachelor', 'Master', 'Bachelor'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male'],
    'Experience (Years)': [2, 5, np.nan, 3, 6, np.nan, 7],
    'Salary': [35000, 60000, 75000, np.nan, np.nan, 55000, 80000],
    'City': ['Delhi', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai', 'Kolkata'],
    'Job Position': ['Junior', 'Senior', 'Manager', 'Junior', 'Senior', 'Junior', 'Manager'],
    'Performance Rating': ['Good', 'Excellent', 'Average', 'Poor', 'Good', 'Excellent', 'Good']
}

