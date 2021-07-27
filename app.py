from flask import Flask, request, render_template
import pickle, os
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename

app = Flask(__name__)



def model_predictThyroidDisease(values):
    model = pickle.load(open('models/ThyroidDisease/thyroid.pickle','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]


    

    
@app.route("/")


@app.route("/ThyroidDisease", methods=['GET', 'POST'])
def ThyroidDisease():
    return render_template('thyroidDisease.html')


@app.route('/predictThyroidDisease',methods=['POST', 'GET'])
def predictThyroid():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictChronicDisease(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)

    return render_template('predictThyroid.html', pred = pred)
    



if __name__ == '__main__':
	app.run(debug = True)