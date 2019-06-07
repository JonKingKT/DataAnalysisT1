
# 删除重复行
def drop_duplicat_row(data):
    for i in data.duplicated()[1:]:
        if i:
            print('存在重复行')
            break
    data.drop_duplicates(keep='first', inplace=True)
#删除空值
def drop_nan(data):
    del_rows=data[data.isnull().T.any()].index.tolist()
    for i in del_rows:
        data.drop(labels=i, axis=0, index=None, columns=None, inplace=True)

#删除不需要的列
def drop_col(data_all,del_col):#参数（数据集，需要删除的列名列表）
    for columns in del_col:
        data_all.drop(labels=columns, axis=1, index=None, columns=None, inplace=True)

