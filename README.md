# POES_wordcloud_Python
NTUPS 2021輿情分析實習課文字雲程式

## 台大2021輿情分析與選舉研究專題實習課 文字雲程式使用說明
### 1. 將整個資料夾下載
### 2. TextData.csv為文本資料原始檔，欄位不拘，但一定要包含「id」及「Text」欄位（注意大小寫）
a. id為每一篇文本的編號，格式不拘，但每篇文都要有id   
b. Text即文本，一個儲存格為一篇文本

### 3. userdict.txt為使用者自定義詞典，可新增專有名詞的特殊詞典
### 4. stopwords.txt為停用詞典，停用詞如標點符號、語助詞、介系詞等
### 5. 打開Wordcloud_python.py並執行
註： 需要套件包含 pandas, numpy, os, jieba, wordcloud，缺少套件時請先執行以下程式碼：   
```
pip install '套件名'
```
or   
```
conda install '套件名'
```

### 6. 先完成斷詞，會在原資料夾新增一個檔案data_seg.xlsx
### 7. 修改filte_n函式中 min_n參數，設定納入文字雲的最小詞頻
```
filter_n(data_Token, min_n=最小詞頻)
```
### 8. 文字雲製作完成