# Machine Learning Analysis of Wine Data

## Summary
The objective of this project was to use machine learning to explore wine data and gain insights into the factors that influence wine prices, ratings, and regions. By applying advanced algorithms, we identified patterns, correlations, and developed predictive models to better understand the wine industry. Our work culminated in a user-friendly dashboard that guides consumers by providing information on price, rating, variety, country, and province, helping them make more informed wine choices.

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/5170fd6b-a8fc-45c1-9a98-0c9f76f2a0b1)

## Key Questions 
1. What are the key factors that significantly impact wine pricing?
2. Is it possible to predict a wine's rating using geographic data and other attributes?
3. How do wine ratings vary across different regions?
4. Are there recognizable trends in wine pricing based on location?
5. Can we detect unusual pricing patterns or outliers that might suggest issues in the wine market?

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/84c175be-fdfa-49b8-8246-8342630f60b7)

## Technologies Used

### Data Cleaning and Storage
* **Data Extraction:** We used MongoDB to store and extract data, allowing for efficient handling of large datasets.
* **Data Cleaning and Transformation:** Using Python and pandas, we performed various cleaning tasks, including dropping redundant or incomplete columns to minimize noise.
* **Year Extraction:** We applied regex to extract the year from textual data, helping isolate the vintage of each wine.
* **Variety Classification:** A dictionary was created to map wine varieties to their specific types.
* **Rating Categorization:** We added a column to categorize wines based on their point-based ratings.
* **Final Outcome:** The resulting dataset contained only relevant features, which facilitated a more efficient and effective analysis.

### Machine Learning
We used SciKitLearn's Random Forest model to implement our machine learning solutions. This ensemble-based algorithm provided robust predictions and allowed us to harness the collective strength of multiple decision trees, yielding a more accurate and reliable model.


### Dashboard
We used Tableau to conduct data analysis and present our findings in a visually compelling story. Through this platform, we created a dashboard that illustrates key insights into wine data, allowing users to explore and interact with the results. The dashboard provides a dynamic map showcasing different U.S. provinces, with wine ratings categorized to reveal trends and patterns. You can view and interact with the dashboard to explore the data and gain a deeper understanding of our analysis here: [Wine Analysis](https://public.tableau.com/app/profile/viktor.kabelkov/viz/WineAnalysis_17149494454560/USProvincesMapperRatingCategory)

### Website
 We created a website to serve as an interface for users to interact with our model. To facilitate this, we used Flask, a lightweight web framework, to build an API that allows for seamless data retrieval and processing. This API enables dynamic data interaction, allowing users to request information and receive real-time responses, thereby enhancing the functionality and user experience of the website. 

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/3579ae9b-3dc8-4c6e-bdb4-1b895a1b41f6)


## Dataset
The dataset used for this project was obtained from Kaggle, with 130,000 rows and 10 columns of wine reviews. You can find the original data at this link: Kaggle Wine Reviews. The dataset, named winemag-data-130k-v2.csv, contains wine reviews scraped from Wine Enthusiast on June 15, 2017, and rescraped on November 22, 2017. The rescraping included additional information like review titles, which allowed for the extraction of the year, and data on the taster, including their name and Twitter handle. These adjustments also addressed duplicate entry issues. After cleaning the data, the final dataset contained 77,931 rows and 11 columns, including details like description, points, price, province, region, title, variety, winery, rating category, and type.


## Machine Learning Model

### Main question/prediction
Our project aimed to predict wine ratings based on key factors like price, wine type, and region. We built a robust model using a random forest classifier, suitable for both categorical and numerical data. Preprocessing involved data cleaning, with encoding and dummy variables to convert categorical data into a numerical format. Key features in our model included price, points, rating category, wine type, country, and variety. The model's output offers an estimated rating for a given wine, shedding light on the factors influencing wine quality and appeal.

### How does the model work?

### Model accuracy and optimization process
The random forest classifier, our chosen machine learning model, works by building multiple decision trees and aggregating their results to make predictions. This ensemble approach reduces overfitting and increases model robustness. In our project, we used this model to predict the rating of a wine based on several key features. To optimize the model's performance, we tuned hyperparameters and validated our approach with cross-validation techniques. The accuracy of the model, which measures its prediction success rate, ranged between 75% and 80%, indicating that the model has a reliable level of precision and generalization, but could benefit from further tuning and additional data to improve its performance.

![image](https://github.com/Zetaorionis/Capstone_Project/assets/143036776/87d0e726-6495-4b95-a807-b2934af12325)


## Possible Future Use
In the future, this model could be enhanced by incorporating additional data sources, such as customer reviews or expert ratings, to improve its accuracy. Improvements could also come from exploring different algorithms, such as gradient boosting or neural networks, which may offer greater predictive power. Additionally, expanding the dataset to include more wine regions and vintages could provide broader insights and allow for a more comprehensive analysis. Further development could focus on creating a recommendation system to assist consumers in selecting wines based on personalized preferences and historical data.

## References
* Data Source: Kaggle
* ChatGPT from OpenAI
* Additional references for code and visualization techniques were cited within the project files as needed.

## Github Repository
The project will be housed in the Capstone Project Github Repository located here: https://github.com/Zetaorionis/Capstone_Project.git

## Authors
Jessica Padilla, Mandy Cisler, Tim Haake, Viktor Kabelkov, Kevin Nazario
