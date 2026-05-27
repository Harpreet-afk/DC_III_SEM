# DC_III_SEM

## Laser Welding Tensile Strength Prediction using Machine Learning

A machine learning-based predictive modeling project focused on analyzing the influence of laser welding process parameters and material properties on weld tensile strength. The project combines data collected from research papers with regression-based machine learning techniques to study welding behavior and parameter importance.

## Project Overview

This project aims to predict the tensile strength of laser welds using material characteristics and laser process parameters.

A structured dataset was developed by compiling experimental data from multiple research papers and preprocessing it for machine learning applications.

The workflow includes:

Data collection and preprocessing
Feature engineering
Exploratory Data Analysis (EDA)
Correlation analysis using heatmaps
Random Forest Regression modeling
Model evaluation and visualization

## Dataset Information

The dataset was curated from published laser welding research papers and contains 14 key features related to:

Material properties
Laser parameters
Welding configuration
Electrical characteristics
Features Used
Core Beam Power
Ring Beam Power
Laser Speed
Material Thickness
Microhardness
Electrical Resistance / Conductivity
Material Types
Laser Type
Laser Mode
Weld Configuration
Tensile Strength (Target Variable)

## Machine Learning Pipeline
1️. Data Preprocessing
Removed missing target values
Converted mixed-type columns into numeric format
Handled duplicate column names
Encoded categorical variables using One-Hot Encoding
Filled missing feature values
2️. Exploratory Data Analysis
Scatter plots for parameter relationships
Correlation heatmaps
Feature interaction analysis
3️. Model Development
Implemented:
Random Forest Regression
4️. Model Evaluation
Performance evaluated using:
R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)

## Visualizations
The project includes:

Feature Importance Graphs
Correlation Heatmaps
Actual vs Predicted Plots
Residual Analysis
Parameter Relationship Scatter Plots

## Technologies Used
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Jupyter Notebook / VS Code
