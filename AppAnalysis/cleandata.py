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
    events_train = readfFile('./data/events_train.csv')
    events_trainlist = events_train['1'].tolist()

    for i in range(10):
        app_events = readfFile('./event_id-app_id/new_app_events'+str(i+1)+'.csv')
        app_events = app_events[app_events.event_id.isin(events_trainlist)]
        app_events.to_csv('app_events_train.csv', mode='a', header=False)



    time_end = time.time()
    print('程序运行时时长：',time_end - time_start)