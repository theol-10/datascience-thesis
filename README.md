# Forecasting Urban Traffic Patterns in London Using Hybrid AI Techniques

This repository contains the code for the Master's thesis project in Data Science at the University of Barcelona, focused on forecasting traffic severity levels in urban environments using machine learning techniques.

The project focuses on predicting traffic severity levels (Good, Minor, Serious) in London, using data from Transport for London (TfL) and weather data from Open-Meteo. The models implemented in this repository aim to enhance the accuracy of traffic forecasting by integrating recent historical traffic patterns with engineered features such as time, weather, and contextual indicators.

The objective of this work is to combine traditional statistical models with advanced machine learning techniques, such as Random Forests and XGBoost, to build a predictive system that can effectively handle class imbalance, model temporal dependencies, and improve minority class recall. Interpretability has also been a key consideration, with SHAP analysis incorporated to provide insights into model behavior and feature importance.

## Project Overview

This repository includes Jupyter notebooks with the following:

- **Data Preprocessing**: Includes data cleaning, feature engineering, and combining multiple data sources (traffic data, weather data, and baseline probabilities).
- **Modeling**: Implements various models including baseline models, Random Forest, XGBoost, and hybrid approaches combining machine learning with statistical priors.
- **Model Evaluation**: Performance evaluation of different models with a focus on macro F1-score, accuracy, recall, and fairness across different classes.
- **Explainability**: Uses SHAP (SHapley Additive exPlanations) to analyze feature importance and provide transparency into the model's decision-making process.

## Objective

The goal of this work is to develop a robust model for traffic severity prediction that can be used in real-world applications to improve urban traffic management, congestion prediction, and dynamic routing decisions. This thesis also aims to explore the intersection of traditional statistical forecasting models with modern machine learning techniques, and evaluate the trade-off between model complexity, interpretability, and predictive power.

### Key Aspects:

- **Hybrid Machine Learning Approach**: Integrating statistical baseline models with machine learning techniques.
- **Class Imbalance Handling**: Special focus on improving minority class recall and model fairness.
- **Model Interpretability**: SHAP analysis for transparent decision-making.
- **Real-time Application**: Designed for urban traffic forecasting with flexible data integration from APIs.

## Repository Contents

- `notebooks/`: Jupyter notebooks for data exploration, modeling, evaluation, and feature engineering.
- `data/`: Contains the traffic and weather datasets used for model development.
- `models/`: Pre-trained models saved for future predictions.
- `results/`: Model evaluation results, including performance metrics and SHAP visualizations.
- `README.md`: This file.

## How to Run the Code

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/traffic-severity-forecasting.git
    cd traffic-severity-forecasting
    ```

2. Install dependencies:

    You can install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. Run Jupyter notebooks:

    Launch Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

    Open the desired notebook from the `notebooks/` folder.


## Acknowledgments

- The project leverages data from the **Transport for London (TfL) API** and **Open-Meteo** for weather data.
- Special thanks to my supervisor for providing guidance and feedback throughout the project.

---