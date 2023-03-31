from flask import Flask, request, render_template 
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
application = Flask(__name__) # __name__ : It will give the entry point

app = application

# Route for a home page
@app.route('/')
def index():
    return render_template('index.html') # It will search for template folder

@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint(): # All the prediction code will be written here
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # In the POST part, we have to capture the data, do standard scaling and make prediction
        #  Reading all the data. Get will have all the information
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    # It will map wit 127.0.0.1
    app.run(host="0.0.0.0")    
