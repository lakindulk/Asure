import json
from this import d
from unicodedata import name
import pandas as pd
from flask import Flask,render_template,request
import pickle
import numpy as np
from flask_cors import CORS 

app=Flask(__name__)
CORS(app)
data=pd.read_csv('https://res.cloudinary.com/iplus/raw/upload/v1662091543/test/Reserch/Cleaned_data_jkxneq.csv')

@app.route('/',methods=['GET'])
def test():
    data='Hello Page'
    print('Hello Page')
    return json.dumps({ "data":data  })

#Get all city names from csv
@app.route('/city',methods=['GET'])
def index():
    locations=sorted(data['Location'].unique())
    country_list=[]
    for row in locations:
            country_list.append(row)
    return json.dumps(country_list)

if __name__ == '__init__':
   app.run(debug=True,port=7001)