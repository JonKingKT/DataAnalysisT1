import pandas as pd
import advance,run
import numpy as np
import matplotlib.pyplot as plt
app_labels = pd.read_csv('2_test_test1_male_label.csv')
new_app_lables=run.allAdvance(app_labels)
app_cate={}
new_app_lables = app_labels['genter'].tolist()
for i in new_app_lables:
    app_cate[i] = app_cate.get(i,0) + 1
items=list(app_cate.items())
items.sort(key=lambda x:x[1],reverse=True)
new_app_10_lables=pd.DataFrame(items,columns=['male', 'count'])
print(new_app_10_lables)

plt.rcParams['font.sans-serif'] = ['SimHei']
y=new_app_10_lables['count'].tolist()
x=new_app_10_lables['male'].tolist()
color = 'red','green'  # 各类别颜色
fig, ax = plt.subplots()
b = ax.bar(x, y,color=color)
plt.title('男女总数')
for a, b in zip(x, y):
    ax.text(a, b+1, b, ha='center', va='bottom')
plt.xticks(range(len(x)+2))
plt.xlabel('性别')
plt.ylabel('counts')
plt.show()






