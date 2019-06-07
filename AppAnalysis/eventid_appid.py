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
    events = readfFile('./data/events.csv')
    app_events=readfFile('./data/app_events.csv')
    eventis_list=[]
    # for i in app_events:
    #     eventis_list.append(i.iat[0, 0])
    # print(eventis_list)
    eventis_list1=[2, 347249, 701234, 1052490, 1401004, 1752200,
                   2101756, 2453615, 2804074, 3148298]
    event_id_app_id_dict={'event_id':"app_id"}
    app_id_list=[]
    eventis_list=events['event_id'].tolist()

    for j in eventis_list[0:347249]:
        app_id_list.extend(app_events[0][app_events[0].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[347250:701234]:
        app_id_list.extend(app_events[1][app_events[1].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[701235:1052490]:
        app_id_list.extend(app_events[2][app_events[2].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[1052491:1401004]:
        app_id_list.extend(app_events[3][app_events[3].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[1401005:1752200]:
        app_id_list.extend(app_events[4][app_events[4].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[1752201:2101756]:
        app_id_list.extend(app_events[5][app_events[5].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[2101757:2453615]:
        app_id_list.extend(app_events[6][app_events[6].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[2453616:2804074]:
        app_id_list.extend(app_events[7][app_events[7].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[2453617:3148298]:
        app_id_list.extend(app_events[8][app_events[8].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list[314829:len(eventis_list)]:
        app_id_list.extend(app_events[9][app_events[9].event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    for j in eventis_list1[1:]:
        for i in app_events:
            app_id_list.extend(i[i.event_id == j]["app_id"].tolist())
        event_id_app_id_dict[j] = app_id_list
        app_id_list = []

    pd.DataFrame.from_dict(event_id_app_id_dict, orient='index').to_csv("event_id_app_id.csv")
    time_end = time.time()
    print('设备运行时间：',time_end - time_start)