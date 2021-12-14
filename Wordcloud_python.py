#!/usr/bin/python
# -*- encoding: utf-8 -*-
# File    :   Wordcloud.py
# Time    :   2021/12/14 16:44:08
# Author  :   Hsu, Liang-Yi
# Email:   yi75798@gmail.com
# Description : 2021輿情分析與選舉研究文字雲程式

# 先載入套件
from collections import Counter
import matplotlib.pyplot as plt
from typing import Counter
from wordcloud import WordCloud
import jieba
import numpy as np
import pandas as pd
import os
os.chdir(os.path.dirname(__file__))

# 先完成斷詞
# 匯入停用詞表
stopwords = []
for word in open('stopwords.txt', 'r'):
    stopwords.append(word.strip())

# 匯入使用者自訂詞典
jieba.load_userdict('userdict.txt')

# 讀入原始文本檔案
# windows使用者改編碼為'ansi' or 'ascii'
df = pd.read_csv('TextData.csv', encoding='utf_8_sig').dropna(subset=['Text'])

# 建立儲存輸出的dataframe
data_Token = pd.DataFrame(columns=['id', 'words'])

# 開始斷詞
for i in df.index:
    result = [seg for seg in jieba.cut(df.loc[i, 'Text'].replace(" ", "").replace("　", '').replace('\n', ""),
                                       cut_all=False) if seg not in stopwords]  # 以迴圈一一抓出每個文本並斷詞
    # 文本空格先去除

    data_Token = data_Token.append(pd.DataFrame({'id': [df.loc[i, 'id']] * len(result),  # 存進output
                                                 'words': result}), ignore_index=True)

# 輸出檔案
data_Token.to_excel('data_seg.xlsx', index=False, encoding='utf_8_sig')

# 製作文字雲
text = Counter(data_Token['words'])


def filter_n(data, min_n: int):
    return {k: v for k, v in data.items() if v >= min_n}


text = filter_n(text, 5)

wc = WordCloud(font_path=font).generate_from_frequencies(text)


plt.imshow(wc)
plt.axis('off')
plt.show()
