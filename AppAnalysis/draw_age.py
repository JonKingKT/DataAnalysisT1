import pandas as pd
import advance,run
import numpy as np
import matplotlib.pyplot as plt
app_labels = pd.read_csv('2_test_test1_age_label.csv')
new_app_lables=run.allAdvance(app_labels)
app_cate={}
new_app_lables = app_labels['age'].tolist()
for i in new_app_lables:
    app_cate[i] = app_cate.get(i,0) + 1
items=list(app_cate.items())
items.sort(key=lambda x:x[0],reverse=False)
new_age=pd.DataFrame(items,columns=['age', 'count'])
plt.rcParams['font.sans-serif'] = ['SimHei']
y=new_age['count'].tolist()
x=new_age['age'].tolist()
x=[str(i) for i in x]
fig, ax = plt.subplots()
b = ax.bar(x, y)
plt.title('年龄总数')
plt.xticks(range(len(x)+2))
plt.xlabel('年龄')
plt.ylabel('counts')
plt.show()






