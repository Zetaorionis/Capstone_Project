from flask import Flask, redirect, url_for, render_template, send_from_directory

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
# app.config['TEMPLATES_AUTO_RELOAD'] = True  # Optional: Auto-reload templates during development
 
dashboard = 'https://public.tableau.com/views/WineAnalysis_17149494454560/USProvincesMapperRatingCategory?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link'


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

# Serve static files like CSS, JS, and images
# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
