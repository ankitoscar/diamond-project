#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
df = pd.read_csv("diamonds.csv")


df.drop(['depth','table','Unnamed: 0'],axis = 1,inplace = True)
df = df.sample(frac = 1)
train_set = df[:round(0.6*len(df))]
valid_set = df[round(0.6*len(df)):round(0.8*len(df))]
test_set = df[round(0.8*len(df)):]

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
column = make_column_transformer((OneHotEncoder(drop = 'first',sparse = False),['cut','color','clarity']),remainder = 'passthrough')

X_train = train_set.drop('price',axis = 1)
y_train = train_set.price

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
model = make_pipeline(column,RandomForestRegressor())

model.fit(X_train,y_train)


# In[11]:


from sklearn.model_selection import cross_val_score
X_valid = valid_set.drop('price',axis = 1)
y_valid = valid_set.price
print(cross_val_score(model,X_valid,y_valid,cv = 5).mean())


# In[12]:


import pickle as pkl
pkl.dump(model,open('model1.pkl','wb'))


# In[13]:


model1 = pkl.load(open('model1.pkl','rb'))


# In[14]:




df = {
    'carat':int(current_user.carat),
    'cut':str(current_user.cut),
    'color':str(current_user.color),
    'clarity':str(current_user.clarity),
    'x':int(current_user.length),
    'y':int(current_user.width),
    'z':int(current_user.depth)
}

columns = ['carat', 'cut', 'color', 'clarity', 'x', 'y', 'z']

data3 = pd.DataFrame(df,index = [0],columns = columns)


# In[15]:


data3


# In[16]:


model.predict(data3)


# In[ ]:




