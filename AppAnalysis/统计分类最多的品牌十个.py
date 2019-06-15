import time
import pandas as pd
import advance,run
phone_brand_device_model= pd.read_csv(r'data\phone_brand_device_model.csv')
events= pd.read_csv(r'data\events.csv')
new_phone_brand_device_model=run.allAdvance(phone_brand_device_model)
events=run.allAdvance(events)
appPingPai_cate={}
new_app_brand=pd.merge(events,phone_brand_device_model,on='device_id')
new_app_brand = new_app_brand['phone_brand'].tolist()
for i in new_app_brand:
    appPingPai_cate[i] = appPingPai_cate.get(i,0) + 1
items=list(appPingPai_cate.items())
items.sort(key=lambda x:x[1],reverse=True)
new_app_brand_phone=pd.DataFrame(items[:10],columns=['pingpai', 'count'])
new_app_brand_phone.to_csv("pingpai.csv")




