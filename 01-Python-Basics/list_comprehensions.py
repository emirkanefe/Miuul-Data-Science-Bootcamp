import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
["NUM_" + num_col.upper() if df[num_col].dtype != "O" else num_col.upper() for num_col in df.columns ]

##########################################################################
## 2. Görev

[num_col.upper() + "_FLAG" if "no" not in num_col else num_col.upper() for num_col in df.columns ]

###############################################################################
## 3. Görev

og_list = ["abbrev" , "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

df[new_cols]