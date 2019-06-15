import numpy as np
import pandas as pd
import matplotlib.patches as mpatches
import  random
import matplotlib.pyplot as plt
cate_list=[548,405,704,713,710]
cate_eng_list=['Industry tag','Custom label','Property Industry 2.0','Services 1','Relatives 1']
new_apps0=[]
new_apps1=[]
new_apps2=[]

# def randomcolor():
#     colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#     color = ""
#     for i in range(6):
#         color += colorArr[random.randint(0,14)]
#     return "#"+color
color=['#F5341B', '#549E1D', '#FB73D5', '#95434B', '#B68574', '#519F33', '#6A6DE8', '#418C19', '#63F9EC', '#46B3DF', '#7411F7', '#C71EC6', '#A28478', '#644B8C', '#65587A']
# for i in range(15):
#     color.append(randomcolor())
# print(color)
for k in cate_list:
    count0=[]
    count1 = []
    count2 = []
    new_apps = pd.read_csv(r'data\new_app_welcome\{}.csv'.format(k))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    count0.append(str(new_apps['app_id'][0]))
    count0.append(str(new_apps['is_active'][0]))
    new_apps0.append(count0)
    count1.append(str(new_apps['app_id'][1]))
    count1.append(str(new_apps['is_active'][1]))
    new_apps1.append(count1)
    count2.append(str(new_apps['app_id'][2]))
    count2.append(str(new_apps['is_active'][2]))
    new_apps2.append(count2)
plt.figure(figsize=(20,15))
plt.bar(np.arange(5),[int(x[1]) for x in new_apps0],color=color[:5],width=0.2)
plt.bar(np.arange(5)+0.2,[int(x[1]) for x in new_apps1] ,color=color[5:10],width=0.2)
plt.bar(np.arange(5)+0.4,[int(x[1]) for x in new_apps2] ,color=color[10:15],width=0.2)
plt.xticks(np.arange(5),cate_eng_list,rotation =20)
labels=[]
for i in range(5):
      labels.append(new_apps0[i][0])
      labels.append(new_apps1[i][0])
      labels.append(new_apps2[i][0])
# print(labels)
patches = [ mpatches.Patch(color=color[i], label="{:s}".format(labels[i]) ) for i in range(len(color)) ]
plt.legend(handles=patches, bbox_to_anchor=(1,1), ncol=1)
plt.title('最受欢迎的五个APP分类中前三的appID',fontsize=40)
plt.savefig("最受欢迎的五个APP分类中前三的appID.png")


