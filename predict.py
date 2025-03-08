from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import json,os,pickle

# load data
# structure of data:[[<distance:float>,<avgspd:float>,<direction_change_std:float>,<isrelay:bool>],...]
data = []   # all the samples
for i in os.listdir('train/traits'):
    print(i,end=' ')
    file_data = []  # single sample
    isrelay = '1' == i.split('.')[1]    # distinguish isrelay from filename
    with open(os.path.join('train/traits',i)) as file:
        file_data.extend(json.load(file))
    file_data.append(isrelay)
    data.append(file_data)
print()

# reconstruct data
X = []  # [[<distance:float>,<avgspd:float>,<direction_change_std:float>],...]
y = []  # [<isrelay:bool>,...]
for i in data:
    X.append(i[:3])
    y.append(i[3])

#Because the set of data is too small to divide into train_data and test_data
'''
# divide train_data and test_data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=TESTSIZE,random_state=42)
'''
X_train = X_test = X
y_train = y_test = y

'''
# standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
'''

# load the model
with open('model/model','rb') as file:
    clf = pickle.load(file)

# predict
print(X_test)
y_pred = clf.predict(X_test)
print(y_pred)

# assess
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

