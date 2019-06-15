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
    # app_events = readfFile('./data/app_events.csv')
    # app_labels = readfFile('./data/app_labels.csv')
    # events = readfFile('./data/events.csv')
    # gender_age_test = readfFile('./data/gender_age_test.csv')
    gender_age_train = readfFile('./data/gender_age_train.csv')
    # label_categories = readfFile('./data/label_categories.csv')
    # phone_brand_device_model = readfFile('./data/phone_brand_device_model.csv')




    # events.longitude[events.longitude < 0] = 0
    # events = events[-events.longitude.isin([0])]
    # # events[i].ix[events[i]['longitude'] == '0',['longitude']] = ''
    # allAdvance(events)



    # allAdvance(gender_age_train)
    # # gender_age_train = gender_age_train[gender_age_train.gender.isin['M','F']]
    # gender_age_train.age[gender_age_train.age < 0] = 0
    # gender_age_train.age[gender_age_train.age > 70] = 0
    # gender_age_train = gender_age_train[-gender_age_train.age.isin([0])]

    # allAdvance(gender_age_test)
    #
    # device_id = gender_age_test['device_id'].tolist()
    # # events_device = events[['device_id','event_id']]
    # # print(events_device.describe())
    # events_device = events[-events.device_id.isin(device_id)]
    # events_device = events_device.dropna()
    # # events_device = events_device[['device_id','event_id']]
    # events_device.to_csv('events_device_test.csv')
    # # events_device_list = events_device.tolist()
    # # print(events_device_list)





    #
    #
    # age_train =  gender_age_train[['device_id','age']]
    # new_events = pd.merge(age_train, events)
    # new_events.to_csv('new_events.csv', index = True)
    # print(new_events.head())

    # *********************合并主表与手机型号表********************
    # phone = readfFile('new_phone_brand_device_model.csv')
    # event = readfFile('events_device_test.csv')
    # events_device_test = pd.merge(event,phone,on='device_id')
    # events_device_test.to_csv('events_device_test_phone.csv')

    # *********************获取app类型********************
    # app_labels = allAdvance(app_labels)
    # label_categories = allAdvance(label_categories)
    # new_label_categories = pd.merge(app_labels, label_categories,on='label_id')
    # new_label_categories.to_csv('new_label_categories.csv')

    # *********************app类型整合********************
    # new_label_categories = readfFile('./new_label_categories.csv')
    # new_label_categories = new_label_categories[['app_id','category']].groupby('app_id')
    # new_label_categories_dict = {'app_id': "category"}
    # for i, group in new_label_categories:
    #     new_label_categories_dict[i] = list(group.category)
    # new_label_categories = pd.DataFrame.from_dict(new_label_categories_dict, orient='index')
    # new_label_categories.to_csv('new_label_categories.csv')

    # *********************events_app与app类型整合********************
    # app_events_train = readfFile('./app_events_train.csv')
    # new_label_categories = readfFile('./new_label_categories.csv')
    # categories_list_dict = {'event_id': "category"}
    # allAdvance(new_label_categories)
    # for i in range(len(app_events_train)):
    #     app_events_train_list = app_events_train.loc[i]
    #     app_id_list_small = []
    #     app_id_list = app_events_train_list.app_id.split('[')[1].split(',')
    #     for j in app_id_list:
    #         # categories_list = new_label_categories[new_label_categories.app_id.isin([int(j)])]
    #         try:
    #             categories_list = (new_label_categories.loc[str(new_label_categories.app_id) == j])
    #             app_id_list_small.extend(categories_list)
    #         except Exception as e:
    #             categories_list = []
    #     app_id_list_small = list(set(app_id_list_small))
    #     categories_list_dict[app_events_train_list.event_id] = app_id_list_small
    #
    # app_events_train = pd.DataFrame.from_dict(categories_list_dict, orient='index')
    # app_events_train.to_csv('new_app_events_train.csv')
    # categories_list_dict.clear()


    # *********************不知名代码********************
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
    # event_id_app_id_dict={'event_id':"app_id"}
    # app_id_list=[]


    # print(len(events['event_id'].tolist()))
    # for i in range(len(app_events)):
    #     app_events[i] = app_events[i][['event_id', 'app_id']]
    #     app_events[i] = app_events[i].groupby('event_id')

    # for i,group in app_events[0]:
    #     event_id_app_id_dict[i] = list(group)
    #     print(list(group.app_id))
    #     print(event_id_app_id_dict[i])
    # event_id_app_id_dict = {'event_id': "app_id"}
    # for i, group in app_events[5]:
    #     event_id_app_id_dict[str(i)] = list(group.app_id)
    #     # print(list(group))
    # new_app_events = pd.DataFrame.from_dict(event_id_app_id_dict, orient='index')
    # new_app_events.to_csv('new_app_events' + str(5 + 1) + '.csv')
    # event_id_app_id_dict.clear()
    # for j in range(6,len(app_events)):
    #     event_id_app_id_dict = {'event_id': "app_id"}
    #     for i,group in app_events[j]:
    #         event_id_app_id_dict[str(i)] = list(group.app_id)
    #         # print(list(group))
    #     new_app_events = pd.DataFrame.from_dict(event_id_app_id_dict, orient='index')
    #     new_app_events.to_csv('new_app_events'+str(j+1)+'.csv')
    #     event_id_app_id_dict.clear()
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