import numpy as np 
#from sklearn import sklearn
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = np.loadtxt("Bank_Customer.csv",skiprows=1,dtype=str,delimiter=',')

'''
Your work
非數值型資料需轉換成數值型資料 (country, gender)
去除掉無意義的特徵類別 (customer_id)
標準化特徵 (StandardScaler)
'''
# pre_data = ...



# 非數值型資料轉換成數值型資料
_, data[:, 2] = np.unique(data[:, 2], return_inverse=True)
_, data[:, 3] = np.unique(data[:, 3], return_inverse=True)


# 去除無意義的特徵類別 (第0欄的 customer_id)
data = np.delete(data, 0, axis=1)

# 將整個陣列轉為浮點數型態，方便後續數值運算
data = data.astype(float)


X = data[:, :-1]
y = data[:, -1]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pre_data = np.column_stack((X_scaled, y))


np.savetxt("Bank_Customer_Preprocessed.csv", pre_data, delimiter=",")


from sklearn.linear_model import LogisticRegression 
# 決策分類器
clf = LogisticRegression()

'''
Your work
切割 data 為 x_train, x_test, y_train, y_test
請學習 train_test_split 的使用方法
'''
x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

# 使用訓練集來訓練我們的分類器
clf.fit(x_train, y_train)
# 測試資料集中進行預測
pred = clf.predict(x_test)

#print (pred) # 預測分類，即客戶是否流失
#print (y_test) # 分類
print (str(accuracy_score(pred, y_test)*100 ) + "% ")   # 預測精度 