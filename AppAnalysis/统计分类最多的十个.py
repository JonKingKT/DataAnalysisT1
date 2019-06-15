import time
import pandas as pd
import advance,run
app_labels = pd.read_csv(r'data\app_labels.csv')
label_categories= pd.read_csv('data\label_categories.csv')
new_app_lables=run.allAdvance(app_labels)
app_cate={}
new_app_lables = app_labels['genter'].tolist()
for i in new_app_lables:
    app_cate[i] = app_cate.get(i,0) + 1
items=list(app_cate.items())
items.sort(key=lambda x:x[1],reverse=True)
new_app_10_lables=pd.DataFrame(items,columns=['male', 'count'])
print(new_app_10_lables)
# result = pd.merge(new_app_10_lables, label_categories, on='label_id')
# result.to_csv("lable_trans.csv")




