import pandas as pd

test = pd.read_csv('D:/TencentAds/TencentLookalike/MetaData/test1.csv')
submission = pd.read_csv('D:/TencentAds/TencentLookalike/Code/submission_csv/score.csv')
submission = pd.concat((test[['aid', 'uid']], submission), axis=1)
submission.to_csv('D:/TencentAds/TencentLookalike/Code/submission_csv/submission.csv', index=None)

