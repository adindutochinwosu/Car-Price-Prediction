# Car-Price-Prediction
An analysis of different machine learning models that is capable of predicting the prices of cars.

## Table of Contents
1. Installation
2. Project Motivation
3. File Descriptions
4. Results
5. Licensing and Acknowledgements
6. CRISP-DM Process

## Installation
Most of the code in this project will run with the Anaconda distribution of Python version 3.*. However, two additional packages are required to run the entire code and can be installed with pip as follows:

1. pip install xgboost
2. pip install hyperopt

## Project Objectives
This project aims to provide a machine learning model that is capable of predicting the prices of used cars. The following objectives are considered in order to accomplish this
1. Analyze different state-of-the art machine learning techniques.
2. Acquire dataset and develop different machine learning prediction models.
3. Examine the performance of the developed models.
4. Build and deploy a machine learning car prediction web application.
## File Descriptions
1. Cars_price_prediction.ipynb - contains code for cleaning, exploring, preparing and modelling the data, and results of the predictive models built from the data.
2. csv_data - used to store the .csv file of the scraped data.
3. models - contains all the models trained in the course of this project.
4. application.py - contains the code for the application.
5. dockerfile - contains all the dependencies and libraries to run the application.
## CRISP-DM Process
1. Business Understanding: The focus is to understand the objectives of the project from a business perspective, by defining the features to be considered for the purpose of answering the above Business questions.
2. Data Understanding: In this section, we perform the initial data collection and become familiar with the dataset by identifying data quality issues, and building initial insight into the data.
3. Data Preparation: Here the data was cleaned (checking for missing values and duplicate data) and digging deeper into the data by visualizing it and identifying relationships between the features themselves and between the features and target variable - Car Prices. We also carried out carried out feature engineering on model car model column.
4. Data Modelling - We split the dataset into training to fit the model and testing to determine accuracy of the model. Several algorithms are fitted to the training set and evaluated on the test set, and the model with the best result is selected as the best model for deployment.
5. Result - Comparing the performances of the models with their default parameters, a baseline was established where the gradient boost model had the best performance compared to the other models on this particular task of predicting car prices with an 𝑅2 score of 85%. The linear regression model was the worst performing model with an 𝑅2 score of 73%. Compared with linear regression or regression trees, the tree ensembles performed considerably better.

After establishing this baseline the different models were then tuned and extreme gradient boost model had the best performance with an 𝑅2 score 95% while gradient boost model also saw an improvement in performance. There was no improvement in the linear regression model while decision tree and random forest saw a drop in their performance.
The machine learning model could not predict the prediction error. This is as a result of limited datapoint.

From the dataset, the most import features for predicitng car prices are
1. Car model
2. Year of registration
3. Price of car
4. Transmission type
5. Mileage of the car
6. Fuel type
7. Tax
8. MPG, ie the distance in miles the car traveled per gallon of fuel.
9. Engine size

Users can access the application front end by typing localhost:8501 from their machine.
