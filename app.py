from flask import Flask, render_template
import jyserver.Flask as jsf

import pandas as pd # data processing
import numpy as np # working with arrays


from sklearn.model_selection import train_test_split # data split

from sklearn.linear_model import LinearRegression # OLS algorithm
from sklearn.linear_model import Ridge # Ridge algorithm
from sklearn.linear_model import Lasso # Lasso algorithm
from sklearn.linear_model import BayesianRidge # Bayesian algorithm
from sklearn.linear_model import ElasticNet # ElasticNet algorithm

from sklearn.metrics import explained_variance_score as evs # evaluation metric
from sklearn.metrics import r2_score as r2 # evaluation metric
from csv import writer
import math

# IMPORTING DATA

df = pd.read_csv('house_data.csv')
df.set_index('Id', inplace = True)

df.head(5)

# EDA

df.dropna(inplace = True)


df.describe()


df['MasVnrArea'] = pd.to_numeric(df['MasVnrArea'], errors = 'coerce')
df['MasVnrArea'] = df['MasVnrArea'].astype('int64')

X_var = df[['LotArea', 'MasVnrArea', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF']].values
y_var = df['SalePrice'].values

X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size = 0.2, random_state = 0)

# MODELLING

# 1. OLS

ols = LinearRegression()
ols.fit(X_train, y_train)

app = Flask(__name__,static_url_path = "/static")

@app.route("/")
def hello_world():
    return App.render(render_template('index.html'))


@jsf.use(app) # Connect Flask object to JyServer
class App:
    def __init__(self): 
        pass

    def rewind(self):
        self.js.document.querySelector(".cover1").style.bottom = "-300px";
        self.js.document.querySelector(".cover1").style.left = "-300px";
        self.js.document.querySelector(".cover2").style.top = "-451px";
        self.js.document.querySelector(".cover2").style.right = "-400px";
        self.js.document.getElementById("formdiv-2").style.display = "block"
        self.js.document.getElementById("formdiv-1").style.display = "none"
        for i in range(5000):
            for j in range(1275):
                pass
        self.js.document.querySelector(".cover1").style.bottom = "-500px"
        self.js.document.querySelector(".cover1").style.left = "-1100px"
        self.js.document.querySelector(".cover2").style.top = "-1000px"
        self.js.document.querySelector(".cover2").style.right = "-1200px"

    def predicte(self): 



        var1 = self.js.document.getElementById("id1").value
        var2 = self.js.document.getElementById("id2").value
        var3 = self.js.document.getElementById("id3").value
        var4 = self.js.document.getElementById("id4").value
        var5 = self.js.document.getElementById("id5").value
        var6 = self.js.document.getElementById("id6").value
        var7 = self.js.document.getElementById("id7").value
        var8 = self.js.document.getElementById("id8").value
        var9 = self.js.document.getElementById("id9").value
        var0 = self.js.document.getElementById("id0").value
        sample = [self.js.parseInt(var1),self.js.parseInt(var2),self.js.parseInt(var3),self.js.parseInt(var4),self.js.parseInt(var5),self.js.parseInt(var6),self.js.parseInt(var7),self.js.parseInt(var8),self.js.parseInt(var9),self.js.parseInt(var0)]


        for i in range(10):
            sample[i] = int(sample[i])

        self.js.document.querySelector(".cover1").style.bottom = "-300px";
        self.js.document.querySelector(".cover1").style.left = "-300px";
        self.js.document.querySelector(".cover2").style.top = "-451px";
        self.js.document.querySelector(".cover2").style.right = "-400px";

        ols_yhat = ols.predict([sample])
        accuracy = str(math.floor(r2(y_test, ols.predict(X_test))*100))
        for i in range(5000):
            for j in range(1275):
                pass	
	
        self.js.document.getElementById("formdiv-1").innerHTML = str(math.floor(ols_yhat[0]))+" $  <span style='font-size: 1ch;'>"+accuracy+"% accurate</span> <button class='btn btn-info' onclick='server.rewind()'>Back</button>"
        self.js.document.getElementById("formdiv-2").style.display = "none"
        self.js.document.getElementById("formdiv-1").style.display = "block"
        self.js.document.querySelector(".cover1").style.bottom = "-500px"
        self.js.document.querySelector(".cover1").style.left = "-1100px"
        self.js.document.querySelector(".cover2").style.top = "-1000px"
        self.js.document.querySelector(".cover2").style.right = "-1200px"

        with open('House_Data.csv', 'r') as f_object:

            data=f_object.readlines()
            var = len(data)
            var=str(var)
            f_object.close()
        List=[var]
        for values in sample:
            List.append(values)

        List.append(str(int(ols_yhat[0])))

        with open('House_Data.csv', 'a') as f_object:

                # Pass this file object to csv.writer()
                # and get a writer object
            writer_object = writer(f_object)

                # Pass the list as an argument into
                # the writerow()
            writer_object.writerow(List)

                #Close the file object
            f_object.close()
