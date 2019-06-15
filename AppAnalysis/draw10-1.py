import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
new_fenlei = pd.read_csv(r'lable_trans.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
count=new_fenlei['count'].tolist()
cate=new_fenlei['category'].tolist()
color = 'red', 'orange', 'yellow', 'green', 'blue', 'gray', 'goldenrod','pink','brown','purple'  # 各类别颜色
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0,0)
plt.pie(count, colors=color, explode=explode, labels=cate, shadow=True, autopct='%1.1f%%')
plt.title('最受欢迎的十个APP分类',fontsize=20)
plt.savefig("最受欢迎的十个APP分类.png")
