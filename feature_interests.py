import pandas as pd

df = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/train_extract.csv')
subsamples = 10000
df = df[:subsamples]
df = pd.DataFrame(df['interest1'])
interest_dict = {}
l = []
print '------------------- interest_dict -------------------'
rows = str(len(df))
for index, row in df.iterrows():
    print '------------------- row: ' + str(row) + '(' + rows + ')' + ' -------------------'
    if isinstance(row['interest1'], str):
        r = {}
        interest_list = [int(interest) for interest in row['interest1'].split(' ')]
        for interest_id in interest_list:
            print '------------------- interest_id: ' + str(interest_id) + ' -------------------'
            r[interest_id] = 1
            if interest_id not in interest_dict:
                interest_dict[interest_id] = 1
            else:
                interest_dict[interest_id] += 1
        l.append(r)

print '------------------- deleting_df -------------------'
del df
print '------------------- df_is_deleted -------------------'
delete_interest = []
print '------------------- delete_interest -------------------'
length = str(len(interest_dict))
count = 0
for i in interest_dict:
    print '------------------- index_in_dict:' + str(i) + '(' + length + ')' + '-------------------'
    if interest_dict[i] < 20:
        count += 1
        print count
        delete_interest.append(i)


m = []
print '------------------- interest_array -------------------'
length = str(len(l))
count = 0
for row in l:
    new = {}
    count += 1
    print '------------------- row: ' + str(count) + '(' + length + ')' + ' -------------------'
    for n in row.keys():
        if n not in delete_interest:
            new[n] = row[n]
    m.append(new)
print '------------------- over -------------------'
m = pd.DataFrame(m)
m = m.fillna(0)
