import pandas as pd

data_ordinalencoding = {
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Bachelor', 'Master', 'Bachelor'],
    'Job Position': ['Junior', 'Senior', 'Manager', 'Junior', 'Senior', 'Junior', 'Manager'],
    'Performance Rating': ['Good', 'Excellent', 'Average', 'Poor', 'Good', 'Excellent', 'Good']
}

df = pd.DataFrame(data_ordinalencoding)

edu_mapping = {'Bachelor': 0, 'Master': 1, 'PhD': 2}
job_mapping = {'Junior': 0, 'Senior': 1, 'Manager': 2}
PR_mapping = {'Poor': 0, 'Average': 1, 'Good': 2, 'Excellent': 3}

e=[]
j=[]
p=[]

for a in df['Education']:
    e.append(edu_mapping[a])

for a in df['Job Position']:
    j.append(job_mapping[a])

for a in df['Performance Rating']:
    p.append(PR_mapping[a])

df['edu_encode']=e
df['job_encode']=j
df['PR_encode']=p

print(df)

