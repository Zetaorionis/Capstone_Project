# Import Dependencies
from flask import Flask, redirect, url_for, render_template, send_from_directory, jsonify, request
import pandas as pd
import numpy as np
import tensorflow as tf

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')



# prediction function
def ValuePredictor(predict_row):
    loaded_model = tf.keras.models.load_model('static/resources/Wine2.h5')
    result = loaded_model.predict(predict_row)
    return result[0][0] 


# Root endpoint with links to api1, api2, and api3
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to redirect to Tableau Dashboard
@app.route('/dashboard')
def dashboard():
    dashboard = 'https://public.tableau.com/app/profile/viktor.kabelkov/viz/WineAnalysis_17149494454560/WineInfoDaashboard'
    return redirect(dashboard)

# API endpoint to Trained Model Landing Page
@app.route('/makeprediction')
def makeprediction():
    return render_template('Prediction.html')

# API endpoint to redirect to github repo
@app.route('/repo')
def repo():
    return redirect('https://github.com/Zetaorionis/Capstone_Project/tree/main')

# API endpoint for displaying prediction results. Function loads model and makes prediciton
@app.route('/result', methods = ['POST'])
def result3():
    wine_df = pd.read_csv('static/resources/clean_wine_data_final.csv')
    scaled_df = pd.read_csv('static/resources/scaled_data_df.csv')

    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        wine = int(to_predict_list['number'])
        predict_row = np.expand_dims(scaled_df.iloc[wine,0:68], axis=0)
        predict_index = scaled_df.iloc[wine,-1]
        wine_data = wine_df.iloc[predict_index,:]
        prediction = ValuePredictor(predict_row) 

        if prediction < .5:
            prediction_text = f"We predict this wine is less than 90 points (Probability: {round(float(prediction),2)})"
        else: 
            prediction_text = f"This wine is 90 points or higher! (Probability: {round(float(prediction),2)})"

        result = wine_data.to_dict()
        result['prediction'] = prediction_text

    return render_template('result.html', result = result)

# API endpoint to Trained Model Landing Page
@app.route('/makeprediction2')
def makeprediction():
    return render_template('Prediction.html')

if __name__ == '__main__':
    app.run(debug=True)
