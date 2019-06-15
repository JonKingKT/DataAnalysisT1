import time

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import fowlkes_mallows_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabaz_score
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import run


def float_col(r):
    return int(time.mktime(r.timetuple())/1000)

# 使用处理好的数据进行构建模型，并用模型来预测test集
if __name__ == '__main__':
    time_start = time.time()
    train_test1 = run.readfFile('train_test1_rewr.csv')
    train_test1 = train_test1.ix[0:int(len(train_test1)/10)]
    test1_data = train_test1[['device_id','event_id','timestamp','longitude','latitude','brand_model_label_code']]

    test1_data['timestamp'] = pd.to_datetime(test1_data['timestamp'])
    test1_data['timestamp'] = test1_data['timestamp'].apply(lambda r: float_col(r))
    test1_data = test1_data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
    print(test1_data.head())
    print('pass')
    test1_age_label =train_test1['age']
    test1_male_label =train_test1['gender']
    train_test1_age_data, test_test1_age_data, train_test1_age_label, test_test1_age_label = train_test_split(test1_data, test1_age_label, test_size=0.2,
                                                                                random_state=42)
    train_test1_male_data, test_test1_male_data, train_test1_male_label, teat_test1_male_label = train_test_split(test1_data, test1_male_label, test_size=0.2,
                                                                                random_state=42)

    svm_age = SVC(C = 10, kernel='rbf', gamma=20, decision_function_shape='ovr').fit(train_test1_age_data, train_test1_age_label)
    print('建立的 AGE_SVM 模型为：\n', svm_age)
    pred_test1_age_label = svm_age.predict(test_test1_age_data)
    print('age测试集的预测结果为：\n', pred_test1_age_label)
    print('AGE_SVM 模型分类报告：\n', classification_report(test_test1_age_label, pred_test1_age_label))

    svm_gender = SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr').fit(train_test1_male_data, train_test1_male_label)
    print('建立的 gender_SVM 模型为：\n', svm_gender)
    pred_test1_male_label = svm_gender.predict(test_test1_male_data)
    print('gender测试集的预测结果为：\n', pred_test1_male_label)
    print('gender_SVM 模型分类报告：\n', classification_report(teat_test1_male_label, pred_test1_male_label))
    pred_test1_age_label = pd.DataFrame(pred_test1_age_label)
    pred_test1_age_label .to_csv('test_test1_age_label.csv')
    pred_test1_male_label = pd.DataFrame(pred_test1_male_label)
    pred_test1_male_label.to_csv('pred_test1_male_label.csv')

    try:
        pickle_file = open('report_age.txt', 'wb')
        pickle.dump(classification_report(test_test1_age_label, pred_test1_age_label), pickle_file)
        pickle_file.close()
    except Exception as e:
        print(e)

    time_end = time.time()
    print('程序运行时间为：',time_end - time_start)
