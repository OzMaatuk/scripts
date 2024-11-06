import pandas as pd

src_fp = "NortonPasswordManager_23_06_24_21_10.csv"
dst_fp = "Chrome Passwords.csv"

# Identify the elemts exist in src file but not exist or not fully equals in dst file

# Item Type,User Name,Password,Site Name,Login URL,Notes,Secure,Favorite
src_df = pd.read_csv(src_fp)

# name,url,username,password,note
dst_df = pd.read_csv(dst_fp)

res_df = pd.DataFrame(columns=["name","url","username","password","note"])

for src_row in src_df['Site Name']: # ['Login URL']
    is_exist_in_dst = False
    for dst_row in dst_df['url']: # ['name']
        if src_row.lower() in dst_row.lower():
            is_exist_in_dst = True
    if not is_exist_in_dst:
        print(src_row)

        # unique_row = src_df[src_df['Login URL'] == src_row]
        # x1 = unique_row["Site Name"].to_string(index=False)
        # x2 = unique_row['Login URL'].to_string(index=False)
        # x3 = unique_row['User Name'].to_string(index=False)
        # x4 = unique_row['Password'].to_string(index=False)
        # x5 = ""
        # print(x1, x2, x3, x4, x5, sep=",")