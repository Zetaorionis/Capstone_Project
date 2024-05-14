# Import Dependencies
from flask import Flask, redirect, url_for, render_template, send_from_directory, request
import pandas as pd
import numpy as np
import tensorflow as tf
from joblib import load

# Establish Falsk App, defining static and template folders for rendering
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

# Prediction Function 
def predict_rating(predict_row):
    loaded_model = tf.keras.models.load_model('static/resources/model.h5')  # Loading trained model
    result = loaded_model.predict(predict_row)  # Making a single prediction based on passed data-row. Returns probablity result (0-1)
    return result[0][0] 

# Prediction accuracy function : compares passed values of prediction and target to return accuracy string (right or wrong)
# Additionally will return confusion matrix value (True Negative, False Positive ...etc. )
def pred_accuracy(prediction, target):
    correct = "The model's prediction was correct!"
    incorrect = "The model got it wrong for this wine."
    if target and prediction: 
        return "True Positive", correct
    elif not target and not prediction:
        return "True Negative", correct
    elif not target and prediction:
        return "False Positive", incorrect
    else: 
        return "False Negative", incorrect

# Root endpoint (Landing/Main page with links to the other endpoints)
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to redirect to Tableau Dashboard
@app.route('/dashboard')
def dashboard():
    dashboard = 'https://public.tableau.com/app/profile/viktor.kabelkov/viz/WineAnalysis_17149494454560/WineInfoDaashboard'
    return redirect(dashboard)

# API endpoint to making prediction page based on X_Test Dataset
@app.route('/makeprediction')
def makeprediction():
    return render_template('Prediction.html')

# API endpoint to redirect to github repo
@app.route('/repo')
def repo():
    return redirect('https://github.com/Zetaorionis/Capstone_Project/tree/main')

# API endpoint for displaying prediction results. 
@app.route('/result', methods = ['POST'])  # redered via form submission on makeprediction route
def result():
    # Loading wine data (for metadata display) & scaled data (for model prediction)
    wine_df = pd.read_csv('static/resources/clean_wine_data_final.csv')
    scaled_df = pd.read_csv('static/resources/scaled_data_df.csv')

    if request.method == 'POST':
        to_predict_list = request.form.to_dict()    # turns form response into a dictionary
        
        try: 
            wine = int(to_predict_list['row'])   # extracts value entered and sets as integer
            
            # Extracts index from scaled_df and pulls metadata for selected wine based on index
            predict_index = scaled_df.iloc[wine,-2]
            wine_data = wine_df.iloc[predict_index,:]
            
            # extracts row based on integer and excludes index and target (last 2 columns) as numpy array and 
            #converts to float32 for tensor model     
            predict_row = np.expand_dims(scaled_df.iloc[wine,:-2], axis=0)  
            predict_row = np.asarray(predict_row).astype(np.float32)
        
            # Calls predict_rating function and passes numpy array of scaled data
            prediction = predict_rating(predict_row)

            # Assigns confusion matrix value and accuracy text based on prediction probabilty (less than .5 = False/< 90) 
            # and adds probability value
            if prediction < .5:
                prediction_text = f"This wine's rating is less than 90 points (Probability: {round(float(prediction),2)})"
                cf_value, accuracy = pred_accuracy(False,scaled_df.iloc[wine,-1])
            else: 
                prediction_text = f"This wine's rating is 90 points or higher! (Probability: {round(float(prediction),2)})"
                cf_value, accuracy = pred_accuracy(True,scaled_df.iloc[wine,-1])

            # Create content dictionary based on wine metadata and add a prediction key with prediction text
            result = wine_data.to_dict()
            result['prediction'] = prediction_text
            result['accuracy'] = accuracy
            result['cf_value'] = cf_value

            return render_template('result.html', result = result)  # render results template and pass content dictionary for display
        # Catch value error for input not being an integer 
        except ValueError as e:     
            message = f"You did not enter an integer. Please try again. (Error Message: {e.args[0]})."
            return render_template('error.html', message = message)
        except IndexError as e:
            message = f"The number you entered is larger than our test dataset."
            return render_template('error.html', message = message)

##########################################################################
#### VERSION 2 of Prediction script - Work in Progress (Incomplete)
# API endpoint to 
@app.route('/makeprediction2')
def makeprediction2():
    return render_template('Prediction2.html')

# API endpoint for displaying prediction results (version 2- User-driven)
@app.route('/result2', methods = ['POST'])  # redered via form submission on makeprediction route
def result2():

    X_scaler = load('static/resources/X_scaler.bin')

    if request.method == 'POST':
        to_predict_list = request.form.to_dict()

        result = to_predict_list

        data =np.zeros(68)

        country_col = 'country_'+ to_predict_list['country']
        variety_col = 'variety_'+ to_predict_list['variety']
        vintage_col = 'vintage_'+ to_predict_list['vintage']
        price_col = int(to_predict_list['price'])

        return render_template('result2.html', result = result)

##################################################################################3

if __name__ == '__main__':
    app.run(debug=True)
