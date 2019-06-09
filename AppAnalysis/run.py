import time

import pandas as pd
import advance


# inputfile = open('./data/app_events.csv', 'rb')   #可打开含有中文的地址
# data = pd.read_csv(inputfile, encoding='gbk' ,iterator=True)

def largeFile(filename):
    data = pd.read_csv(filename, encoding='gbk', iterator=True)
    loop = True
    chunkSize = 3500000
    chunks = []
    while loop:
        try:
            chunk = data.get_chunk(chunkSize)
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
        advance.drop_nan(data)
        advance.drop_duplicat_row(data)
    except:
        for i in range(len(data)):
            advance.drop_nan(data[i])
            advance.drop_duplicat_row(data[i])
    return data


if __name__ == '__main__':
    time_start = time.time()

    # 数据地址
    app_events = readfFile('./data/app_events.csv')
    # app_labels = readfFile('./data/app_labels.csv')
    events = readfFile('./data/events.csv')
    # gender_age_test = readfFile('./data/gender_age_test.csv')
    gender_age_train = readfFile('./data/gender_age_train.csv')
    # label_categories = readfFile('./data/label_categories.csv')
    # phone_brand_device_model = readfFile('./data/phone_brand_device_model.csv')


    events.longitude[events.longitude < 0] = 0
    events = events[-events.longitude.isin([0])]
    # events[i].ix[events[i]['longitude'] == '0',['longitude']] = ''
    allAdvance(events)



    allAdvance(gender_age_train)
    # gender_age_train = gender_age_train[gender_age_train.gender.isin['M','F']]
    gender_age_train.age[gender_age_train.age < 0] = 0
    gender_age_train.age[gender_age_train.age > 70] = 0
    gender_age_train = gender_age_train[-gender_age_train.age.isin([0])]

    device_id = gender_age_train['device_id'].tolist()
    events_device = events[['device_id','event_id']]
    # print(events_device.describe())
    events_device = events_device[events_device.device_id.isin(device_id)]
    events_device = events_device.dropna()
    events_device = events_device['event_id']
    # events_device.to_csv('events_device.csv')
    events_device_list = events_device.tolist()
    # print(events_device_list)





    #
    #
    # age_train =  gender_age_train[['device_id','age']]
    # new_events = pd.merge(age_train, events)
    # new_events.to_csv('new_events.csv', index = True)
    # print(new_events.head())


    # 合并主表与手机型号表
    # allAdvance(phone_brand_device_model)
    # phone_brand_device_model = phone_brand_device_model[-phone_brand_device_model.device_model.str.contains('???')]
    # phone_brand_device_model = phone_brand_device_model[['device_id','device_model']]
    # print(phone_brand_device_model.head(10))
    # new_events = readfFile('new_events.csv')
    # new_events = pd.merge(new_events,phone_brand_device_model)
    # new_events.to_csv('new_events1.csv')



    # for i in range(len(app_events)):
    #     app_events[i] = advance.delCols(app_events[i],['is_installed','is_active'])
    #     app_events[i] = advance.drop_nan(app_events[i])
    #     app_events[i] = advance.drop_duplicat_row(app_events[i])
    # for i in app_events:
    #     print(i.shape)
    # app_events = pd.concat(app_events)
    # # app_events.to_csv('app_eve.csv', index=False)
    # print('程序运行时时长：',time_end - time_start)


    # *********************合并event_id_app_id********************
    # print(events.iat[0, 0])
    event_id_app_id_dict={'event_id':"app_id"}
    app_id_list=[]


    # print(len(events['event_id'].tolist()))
    for i in range(len(app_events)):
        app_events[i] = app_events[i][['event_id', 'app_id']]
        app_events[i] = app_events[i].groupby('event_id')

    for j in range(len(app_events)):
        event_id_app_id_dict = {'event_id': "app_id"}
        for i,group in app_events[j]:
            event_id_app_id_dict[str(i)] = list(group)
        new_app_events = pd.DataFrame(event_id_app_id_dict)
        new_app_events.to_csv('new_app_events'+str(j+1)+'.csv')
        event_id_app_id_dict.clear()
            # print(app_id_list.append(list(group)))
            # print(i)
            # print(list(group.app_id))

    # for j in events['event_id'].tolist():
    # for i in app_events:
    #     app_id_list.extend(i[i.event_id == 2]["app_id"].tolist())
    #
    # event_id_app_id_dict[2] = app_id_list
    # app_id_list = []
    # pd.DataFrame.from_dict(event_id_app_id_dict, orient='index').to_csv("event_id_app_id.csv")
    # # pd.DataFrame(event_id_app_id_dict).to_csv("event_id_app_id.csv")
    # print(app_events[0][app_events[0].event_id == 2]["app_id"].tolist())
    # print(events['event_id'].tolist())
    time_end = time.time()
    print('程序运行时时长：',time_end - time_start)