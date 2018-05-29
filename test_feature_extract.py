import pandas as pd
import numpy as np
import math

test = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/test1.csv')
adFeature = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/adFeature.csv')
userFeature = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/userFeature.csv')

test = pd.merge(test, adFeature, how='left', on='aid')
test = pd.merge(test, userFeature, how='left', on='uid')


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


def drop_nan_columns(test):
    column_list = test.columns
    none_nan_columns = []
    for column in column_list:
        test_single_column = test[column]
        if (test_single_column.isnull().any() == True and nan_val(
                test_single_column)) or test_single_column.isnull().any() == False:
            none_nan_columns.append(column)
    feature_none_nan_columns = [x for x in test.columns if x in none_nan_columns]
    return test[feature_none_nan_columns]


test = drop_nan_columns(test)
# test = drop_nan_columns(test)
test.to_csv('D:/TencentAds/TencentLookalike/MetaData/test_extract.csv', index=None)


