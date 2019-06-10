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


    # new_events=readfFile('./data/new_events.csv')
    # dataframe1 = readfFile('./data/app_events_train.csv')
    #
    # new_events2=pd.merge(new_events,dataframe1,on='event_id',how='left')
    #
    # new_events2.to_csv('new_events3.csv')
    # app_events1=readfFile('./data/app_events.csv')
    # for i in app_events1:
    #     i[['app_id','is_active']].to_csv('new_app_events.csv', mode='a', header=False)
    new_events3=readfFile('./data/new_events3.csv')
    print(new_events3.head())
    new_events4=new_events3.dropna()
    new_events4.to_csv('train_test1.csv')