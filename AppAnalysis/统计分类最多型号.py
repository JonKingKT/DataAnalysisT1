import time
import pandas as pd
import advance,run
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
phone_brand_device_model = pd.read_csv('data\phone_brand_device_model.csv')
phone_brand_device_model['newColumn'] = phone_brand_device_model['phone_brand']+phone_brand_device_model['device_model']
new_phone_brand_device_model=run.allAdvance(phone_brand_device_model)
xinhao_cate={}
new_app_brand = new_phone_brand_device_model['newColumn'].tolist()
for i in new_app_brand:
    xinhao_cate[i] = xinhao_cate.get(i,0) + 1
items=list(xinhao_cate.items())
items.sort(key=lambda x:x[1],reverse=True)
new_app_brand_phone=pd.DataFrame(items[:10],columns=['xinhao', 'count'])
new_app_brand_phone.to_csv("xinhao.csv")

