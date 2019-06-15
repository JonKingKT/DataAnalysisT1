import time
import pandas as pd
import advance,run
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
phone_brand_device_model = pd.read_csv('data\phone_brand_device_model.csv')
phone_brand_device_model['newColumn'] = phone_brand_device_model['phone_brand']+phone_brand_device_model['device_model']
advance.drop_col(phone_brand_device_model,['phone_brand','device_model'])
# 使用LabelEncoder将类别转换为数字
model_label_encoder = LabelEncoder()
model_label_encoder.fit(phone_brand_device_model['newColumn'].values)
phone_brand_device_model['brand_model_label_code'] = model_label_encoder.transform(phone_brand_device_model['newColumn'].values)
advance.drop_col(phone_brand_device_model,['newColumn'])
phone_brand_device_model=run.allAdvance(phone_brand_device_model)
phone_brand_device_model.to_csv('new_phone_brand_device_model.csv')
