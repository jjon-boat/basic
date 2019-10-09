#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Boat

import pandas as pd

## 初始化一个dateFrame
data = {'name':['Bob','James','Kobe','Jone','Anna'],'year':[2000,2001,2001,2000,2003],'score':[1.1,2,3.7,3,2]}
# columns限定生成的列，字典中没有，colunms中有的key会初始化为NaN
# index替代原来的0，1，2，3，4,index的长度必须与原行数一致
frame = pd.DataFrame(data,columns=['name','sex','score'],index=['one','two','three','four','five'])
print(frame)
# 新增一列
frame['age']=[10,11,12,13,14]
print(frame)


## loc与iloc的使用
# loc替代原来的ix方法
print(frame.loc['three'])  # 选出index='three'的行
print(frame.loc[['three','five']])   # 选出index='three'、'five'的的行
print(frame.loc[['three','five'],['name','score']]) # 选出index='three'、'five'，columns='name'、'score'的行与列
# iloc用数字索引筛选行列
print(frame.iloc[2])  # 实际为第三行，索引从0开始
print(frame.iloc[1,3])  # 这个千万要注意了，这个不是筛选出第1、3行，而是选出第1行、第3列的元素（这里的1、3是从0开始索引的）
# 用iloc各种切片
print(frame.iloc[1:4])  # 用切片的方法选出1:4行,所有列
print(frame.iloc[1:4,[1,3]])
print(frame.iloc[:,1:])  # 选出1之后的所有列
