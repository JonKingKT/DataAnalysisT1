import time

import pandas as pd
import advance


# inputfile = open('./data/app_events.csv', 'rb')   #可打开含有中文的地址
# data = pd.read_csv(inputfile, encoding='gbk' ,iterator=True)

def largeFile(filename):
    data = pd.read_csv(filename, encoding='gbk', iterator=True)
    loop = True
    chunkSize = 350000
    chunks = []
    while loop:
        try:
            chunk = data.get_chunk(chunkSize)
            chunk = advance.drop_duplicat_row(chunk)
            chunk = advance.drop_nan(chunk)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("读取完成.")
    return chunks

def readfFile(filename):
    try:
        file = pd.read_csv(filename)
    except:
        file = largeFile(filename)
    return file

def allAdvance(data):
    try:
        data = advance.drop_nan(data)
        data = advance.drop_duplicat_row(data)
    except:
        for i in range(len(data)):
            data[i] = advance.drop_nan(data[i])
            data[i] = advance.drop_duplicat_row(data[i])
    return data


if __name__ == '__main__':
    time_start = time.time()

    # 数据地址
    # app_events = readfFile('./data/app_events.csv')
    # app_labels = readfFile('./data/app_labels.csv')
    events = readfFile('./data/events.csv')
    # gender_age_test = readfFile('./data/gender_age_test.csv')
    gender_age_train = readfFile('./data/gender_age_train.csv')
    # label_categories = readfFile('./data/label_categories.csv')
    # phone_brand_device_model = readfFile('./data/phone_brand_device_model.csv')


    # events.longitude[events.longitude < 0] = 0
    # events = events[-events.longitude.isin([0])]
    # # events[i].ix[events[i]['longitude'] == '0',['longitude']] = ''
    # allAdvance(events)


    allAdvance(gender_age_train)
    # gender_age_train = gender_age_train[gender_age_train.gender.isin['M','F']]
    # gender_age_train.age[gender_age_train.age < 0] = 0
    # gender_age_train.age[gender_age_train.age > 70] = 0
    # gender_age_train = gender_age_train[-gender_age_train.age.isin([0])]
    print(gender_age_train.describe())

    # for i in range(len(app_events)):
    #     app_events[i] = advance.delCols(app_events[i],['is_installed','is_active'])
    #     app_events[i] = advance.drop_nan(app_events[i])
    #     app_events[i] = advance.drop_duplicat_row(app_events[i])
    # for i in app_events:
    #     print(i.shape)
    # app_events = pd.concat(app_events)
    # app_events.to_csv('app_eve.csv', index=False)
    time_end = time.time()
    print('程序运行时时长：',time_end - time_start)