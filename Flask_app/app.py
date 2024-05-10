# Import Dependencies
from flask import Flask, redirect, url_for, render_template, send_from_directory, jsonify, request
import pandas as pd
import numpy as np
import tensorflow as tf

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
# app.config['TEMPLATES_AUTO_RELOAD'] = True  # Optional: Auto-reload templates during development
 
dashboard = 'https://public.tableau.com/app/profile/viktor.kabelkov/viz/WineAnalysis_17149494454560/WineInfoDaashboard'

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
@app.route('/endpoint1')
def endpoint1():
    return redirect(dashboard)

# API endpoint to Trained Model Landing Page
@app.route('/endpoint2')
def endpoint2():
    return render_template('Prediction.html')

# API endpoint to redirect to github repo
@app.route('/endpoint3')
def endpoint3():
    return redirect('https://github.com/Zetaorionis/Capstone_Project/tree/main')

# API endpoint to Trained Model Landing Page
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        if int(to_predict_list['number']) > 5: 
            prediction = 'Greater than 5'
        else: 
            prediction = 'Less than or equal to 5'
    return render_template('result.html', prediction = prediction)

# API endpoint to Trained Model Landing Page
@app.route('/result2', methods = ['POST'])
def result2():
    wine_df = pd.read_csv('static/resources/clean_wine_data_final.csv')
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        wine = int(to_predict_list['number'])
        wine_row = wine_df.iloc[wine,:]
        prediction = wine_row['title']

    return render_template('result.html', prediction = prediction)

# API endpoint to Trained Model Landing Page
@app.route('/result3', methods = ['POST'])
def result3():
    wine_df = pd.read_csv('static/resources/clean_wine_data_final.csv')
    scaled_df = pd.read_csv('static/resources/scaled_data_df.csv')

    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        wine = int(to_predict_list['number'])
        predict_row = np.expand_dims(scaled_df.iloc[wine,0:68], axis=0)
        predict_index = scaled_df.iloc[wine,-1]
        wine_data = wine_df.iloc[predict_index,:]
        result = ValuePredictor(predict_row) 

        if result < .5:
            prediction = f"We predict this wine is less than 90 points (Probability: {round(float(result),2)})"
        else: 
            prediction = f"This wine is 90 points or more! (Probability: {round(float(result),2)})"

        output ={
            'prediction': prediction, 
            'wine' : wine_data['title'],
            'country' : f"{wine_data['region']}, {wine_data['country']}",
            'rating': wine_data['points'] 
            }

    return render_template('result.html', result = output)

# Serve static files like CSS, JS, and images
# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
