# 删除重复行
def drop_duplicat_row(data):
    for i in data.duplicated()[1:]:
        if i:
            print('存在重复行')
            break
    data.drop_duplicates(keep='first', inplace=True)
    return data
#删除空值
def drop_nan(data):
    del_rows=data[data.isnull().T.any()].index.tolist()
    for i in del_rows:
        data.drop(labels=i, axis=0, index=None, columns=None, inplace=True)
    return data

# 删除多余列
def delCols(data,cols):
    data = data.drop(columns=cols,inplace = True)
    return data