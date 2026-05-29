from dask.array import delete
from pyarrow.types import dictionary

salaries = [1,2,3,4,5,6]

def new_salary(x):
    return x * 20 / 100 + x

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

for salary in salaries:
    if salary > 3:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary * 2) if salary < 3 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary > 3]
[new_salary(salary * 2) if salary > 3 else new_salary(salary * 0.2) for salary in salaries ]

students = ["a","b","c","d","e","f"]

students_no =["a","b"]

[student.lower() if student in students_no else student.upper() for student in students]

[student.upper() if student not in students_no else student.lower() for student in students]

#################################################################################################

dictionary = { 'a':1,
               'b':2,
               'c':3,
               'd':4,}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}

############################################################################################

numbers = range(10)
new_dict = {}

for number in numbers:
    if number % 2 == 0:
        new_dict[number] = number ** 2


{number: number ** 2 for number in numbers if number % 2 == 0}


####################################################################################################
### 1. Uygulama

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


df.columns = [col.upper() for col in df.columns]

################################################################################################
### 2.Uygulama

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

["FLAG_" + col  if "INS" in col else "NO_FLAG_" + col for col in df.columns]

##############################################################################
######## 3. uygulama
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}

agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)

##########################################################################

liste = [1,2,3,4,5]
yeni_liste = [i for i in liste]
print(yeni_liste)

print([i*2 for i in range(1,5)])

eski_fiyat = {'süt': 1.02, 'kahve': 2.5, 'ekmek': 2.5}

dolar_tl = 0.76
yeni_fiyat = {item: value*dolar_tl for (item, value) in eski_fiyat.items()}
print(yeni_fiyat)

