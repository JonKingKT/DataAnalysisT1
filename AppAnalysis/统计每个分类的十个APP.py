import time
import pandas as pd
import advance,run
#把app_events转化成9个小CSV，然后根据APP_ID贴上标签，最后算出了，前十的标签APP的个数
# for j in range(1,10):
#     app_labels = run.readfFile(r'data\app_events10pers\app_events{}.csv'.format(j))
#     lable_trans = run.readfFile(r'data\app_labels.csv')
#     cate_list=[548, 405,794,795,704,714,713,854,710,711]
#     result = pd.merge(app_labels,lable_trans, on='app_id')
#     result.drop(['event_id', 'is_installed'],axis=1,inplace=True)
#     new_result= result[result.label_id.isin(cate_list)]
#     for i in cate_list:
#         data_result = new_result[new_result.label_id.isin([i])]
#         k = data_result.groupby('app_id').is_active.sum()
#         k1=k.sort_values(ascending=False,inplace=True)
#         k1 = pd.DataFrame(k)
#         k1=k1.head(10)
#         k1.to_csv(str(i)+str("({})".format(j))+'.csv')
#         k.drop(k.index, inplace=True)
#         k1.drop(k1.index, inplace=True)
#         data_result.drop(data_result.index, inplace=True)
cate_list=[548, 405,794,795,704,714,713,854,710,711]
for j in cate_list:
    new_df = pd.read_csv(r'data\app_welcome\{}(1).csv'.format(j))
    for i in range(2,10):
        app_labels = pd.read_csv(r'data\app_welcome\{}({}).csv'.format(j,i))
        new_df = pd.concat([new_df,app_labels])
        app_labels.drop(app_labels.index, inplace=True)
    k = new_df.groupby('app_id').is_active.sum()
    k1=k.sort_values(ascending=False,inplace=True)
    k1 = pd.DataFrame(k)
    k1=k1.head(10)
    k1.to_csv(r'data\new_app_welcome\{}.csv'.format(j))
    k.drop(k.index, inplace=True)
    k1.drop(k1.index, inplace=True)
    new_df.drop(new_df.index, inplace=True)









