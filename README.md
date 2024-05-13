# Machine Learning Analysis of Wine Data

## Summary
The objective of this project was to use machine learning to explore wine data and gain insights into the factors that influence wine prices, ratings, and regions. By applying advanced algorithms, we identified patterns, correlations, and developed predictive models to better understand the wine industry. Our work culminated in a user-friendly dashboard that guides consumers by providing information on price, rating, variety, country, and region, helping them make more informed wine choices.

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/5170fd6b-a8fc-45c1-9a98-0c9f76f2a0b1)

## What We Wanted to Explore
1. What are the key factors that significantly impact wine pricing?
2. Is it possible to predict a wine's rating using geographic data and other attributes?
3. How do wine ratings vary across different regions?
4. Are there recognizable trends in wine pricing based on location?
5. Can we detect unusual pricing patterns or outliers that might suggest issues in the wine market?

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/84c175be-fdfa-49b8-8246-8342630f60b7)

## Table of Contents


- [Data Cleaning and Storage](#DataCleaningandStorage)
- [Machine Learning](#MachineLearning)
- [Dashboard](#Dashboard)
- [Website](#Website)
- [Dataset](#Dataset)
- [Main question/prediction](#Mainquestion/prediction)
- [Model accuracy and optimization process](#Modelaccuracyandoptimizationprocess)
- [Possible Future Use](#PossibleFutureUse)
- [References](#References)
- [Github Repository](#GithubRepository)
- [Authors](#Authors)

# Technologies Used

### Data Cleaning and Storage
* **Data Extraction:** We used MongoDB to store and extract data, allowing for efficient handling of large datasets.
* **Data Cleaning and Transformation:** Using Python and pandas, we performed various cleaning tasks, including dropping redundant or incomplete columns to minimize noise.
* **Year Extraction:** We applied regex to extract the year from textual data, helping isolate the vintage of each wine.
* **Variety Classification:** A dictionary was created to map wine varieties to their specific types.
* **Rating Categorization:** We added a column to categorize wines based on their point-based ratings.
* **Final Outcome:** The resulting dataset contained only relevant features, which facilitated a more efficient and effective analysis.

### Machine Learning
In order to create a predictive model, we created a boolean target feature based on rating (Does the wine have a points rating of 90 or higher?). Additional pre-processing was completed, including making dummy columns for categorical data and applying a standard scalar in order to prepare our dataset for predicitive modeling. 

Selecting our model, we went through several iterations, using SciKitLearn's library to use Logistic Regression, K-Nearest-Neighbors (KNN) and a Random Forrest model. In the end, we decided on a Neural Network/Deep Learning Model, creating an input layer, hidden layers for processing, and a sigmoid (binary) output layer that could classify the boolean target. Ultimately, based on the number of categorical bins in our dataset, we felt that the Neural Network was handling the data the best. We employed a Keras Tuner to help with the optimization, but fell back to a simpler model that surpassed 75% accuracy. 

### Dashboard
We used Tableau to conduct data analysis and present our findings in a visually compelling story. Through this platform, we created a dashboard that illustrates key insights into wine data, allowing users to explore and interact with the results. The dashboard provides a dynamic map showcasing different U.S. provinces, with wine ratings categorized to reveal trends and patterns. You can view and interact with the dashboard to explore the data and gain a deeper understanding of our analysis here: [Wine Analysis](https://public.tableau.com/app/profile/viktor.kabelkov/viz/WineAnalysis_17149494454560/USProvincesMapperRatingCategory)

### Website
 We created a website to serve as an interface for users to interact with our model. To facilitate this, we used Flask, a lightweight web framework, to build an API that allows for seamless data retrieval and processing. This API enables dynamic data interaction, allowing for users to interact with our machine leanring model in order to make predictions. Additional functionality to display and interact with the data using a database could be employed in the future. 

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/3579ae9b-3dc8-4c6e-bdb4-1b895a1b41f6)


## Dataset
The dataset used for this project was obtained from Kaggle, with 130,000 rows and 10 columns of wine reviews. You can find the original data at this link: Kaggle Wine Reviews. The dataset, named winemag-data-130k-v2.csv, contains wine reviews scraped from Wine Enthusiast on June 15, 2017, and rescraped on November 22, 2017. The rescraping included additional information like review titles, which allowed for the extraction of the year, and data on the taster, including their name and Twitter handle. These adjustments also addressed duplicate entry issues. After cleaning the data, the final dataset contained 77,931 rows and 11 columns, including details like description, points, price, province, region, title, variety, winery, rating category, and type.


# Machine Learning Model

### Main question/prediction
How can we leverage TensorFlow deep learning models to predict wine ratings based on key factors such as price, wine type, and region? This project aims to develop a robust neural network architecture using TensorFlow, capable of effectively learning complex patterns from the input data. By preprocessing the dataset to handle both categorical and numerical data and incorporating features such as price, points, rating category, wine type, country, and variety, we seek to create a predictive model that offers insights into the factors shaping wine quality and appeal.

### Model accuracy and optimization process
Our project utilized a Keras TensorFlow deep learning model to predict wine ratings based on key features. This neural network architecture was optimized through hyperparameter tuning and cross-validation techniques. Achieving an accuracy range of 75% to 80%, our model demonstrates reliable precision and generalization. However, further refinement and the inclusion of additional data could enhance its performance for even more accurate predictions.

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/87d0e726-6495-4b95-a807-b2934af12325)


## Possible Future Use
In the future, this model could be enhanced by incorporating additional data sources, such as customer reviews or expert ratings, to improve its accuracy. Additional features may be able to be extracted using sentiment analysis or keyword extraction from the reviews in the original dataset. Improvements could also come from exploring different algorithms, such as gradient boosting or neural networks, which may offer greater predictive power. Additionally, expanding the dataset to include more wine regions and vintages could provide broader insights and allow for a more comprehensive analysis. Further development could focus on creating a recommendation system to assist consumers in selecting wines based on personalized preferences and historical data.

## References
* Data Source: [Kaggle](https://www.kaggle.com/datasets/zynicide/wine-reviews)
* ChatGPT from OpenAI
* Photos from [Unsplash](https://unsplash.com/)
* Confusion Matrix: [Matplotlib Docs](https://matplotlib.org/stable/), [Seaborn Docs](https://seaborn.pydata.org/generated/seaborn.heatmap.html), [CF Visualization Example](https://medium.com/@dtuk81/confusion-matrix-visualization-fc31e3f30fea)
* [Saving Sacler](https://stackoverflow.com/questions/53152627/saving-standardscaler-model-for-use-on-new-datasets)
* Wordcloud Examples: [#1](https://amueller.github.io/word_cloud/auto_examples/simple.html#sphx-glr-auto-examples-simple-py), [#2](https://www.datacamp.com/tutorial/wordcloud-python)
* Flask: [Deploying Flask with Model](https://www.geeksforgeeks.org/deploy-machine-learning-model-using-flask/), [Content Dict](https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e)
 
* Additional references for code and visualization techniques were cited within the project files as needed.

## Github Repository
The project will be housed in the Capstone Project Github Repository located here: https://github.com/Zetaorionis/Capstone_Project.git

## Authors
Jessica Padilla, Mandy Cisler, Tim Haake, Viktor Kabelkov, Kevin Nazario
