import pandas as pd
import numpy as np
import math

train = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/train.csv')
adFeature = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/adFeature.csv')
userFeature = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/userFeature.csv')

train = pd.merge(train, adFeature, how='left', on='aid')
train = pd.merge(train, userFeature, how='left', on='uid')



# train = train.dropna(how='all', axis=1)


def nan_val(df):
    n = len(df)
    df = (np.array(df)).tolist()
    count = 0
    for val in df:
        if isinstance(val, float) and math.isnan(val):
            count += 1
    nan_rate = float(count) / float(n)
    if nan_rate <= 0.5:
        return True
    return False


def drop_nan_columns(train):
    column_list = train.columns
    none_nan_columns = []
    for column in column_list:
        train_single_column = train[column]
        if (train_single_column.isnull().any() == True and nan_val(
                train_single_column)) or train_single_column.isnull().any() == False:
            none_nan_columns.append(column)
    feature_none_nan_columns = [x for x in train.columns if x in none_nan_columns]
    return train[feature_none_nan_columns]


train = drop_nan_columns(train)
train.to_csv('D:/TencentAds/TencentLookalike/MetaData/train_extract.csv', index=None)





