import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import advance
#画图 画出最受欢迎的手机品牌和型号
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
    pingpai = readfFile('./data/pingpai.csv')
    print(pingpai)
    data1 = np.array(pingpai['count'])
    data1_x = np.array(pingpai['pingpai'])
    xinghao= readfFile('./data/xinhao.csv')
    print(xinghao)

    data2 = np.array(xinghao['count'])
    data2_x = np.array(xinghao['xinhao'])
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文


    p1 = plt.figure(figsize=(8,8))
    p1_1 = p1.add_subplot(2, 1, 1)     #创建第一幅子图
    plt.bar(data1_x,data1)
    plt.ylabel('使用数量')
    plt.title('最受欢迎的十大手机品牌')
    p2_2 = p1.add_subplot(2, 1, 2)     #创建第二幅子图
    plt.title('最受欢迎的十大手机型号')
    plt.bar(data2_x, data2)
    plt.xticks(rotation=45)
    plt.ylabel('使用数量')
    plt.show()