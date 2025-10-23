import pandas as pd

data_onehot = {
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Marketing', 'Finance'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male'],
    'City': ['Delhi', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai', 'Kolkata']
}

df = pd.DataFrame(data_onehot)

def check(x, y):
    if x == y:
        return 1
    else:
        return 0

dep = df['Department'].unique()
for a in dep:
    df[a] = df['Department'].apply(check, args=(a,))

gender = df['Gender'].unique()
for a in gender:
    df[a] = df['Gender'].apply(check, args=(a,))

city = df['City'].unique()
for a in city:
    df[a] = df['City'].apply(check, args=(a,))

print (df)
