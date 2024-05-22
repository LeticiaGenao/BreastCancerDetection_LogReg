# Breast Cancer Diagnosis Using Logistic Regression

**By: Leticia Genao**  
**Course: N.U. ANA680**

## Problem Statement

Breast cancer continues to be a significant global health challenge. This project focuses on applying logistic regression to predict the occurrence of breast cancer using the dataset from the UCI Machine Learning Repository. The objective is to build an effective model for classifying tumors as benign or malignant, optimizing it for the highest accuracy.

## Dataset Description

The dataset used is the **Breast Cancer Wisconsin (Original) Dataset**, consisting of 683 instances with 11 columns, including the target variable 'Class'. Each instance includes 10 predictive features related to the cell nuclei characteristics from a fine needle aspirate (FNA) of a breast mass.

**Data Source:** [Breast Cancer Wisconsin (Original) Dataset](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original))  
**Rows:** 683  
**Columns:** 11 (including the target variable 'Class')

## Methodology

### Data Preprocessing

The class labels were converted from 2 (benign) and 4 (malignant) to 0 and 1 to facilitate binary classification. The dataset was divided into a training set (75%) and a testing set (25%), with no further cleaning or feature engineering to maintain the integrity of the original data.

### Model Building

The logistic regression model was implemented using Scikit-learn, with hyperparameters fine-tuned through extensive grid search involving 900 fits across 180 candidate settings.

## Model Evaluation

The logistic regression model's performance was evaluated based on accuracy and a confusion matrix, which are critical for assessing the model's ability to classify the data correctly.

## Results

### Model Performance Summary

- **Accuracy:** 96.49%
- **Best Cross-Validation Score:** 0.97

### Model Confusion Matrix

- True Negative (TN): 102
- False Positive (FP): 1
- False Negative (FN): 5
- True Positive (TP): 63

## Discussion

The logistic regression model achieved an accuracy of 96.49%, with an optimal cross-validation score of 0.97, indicating a strong predictive performance. The model utilized the 'liblinear' solver with L2 regularization, demonstrating robustness in handling the linear relationships among the features. The low false positive rate suggests that the model is effective in minimizing the risk of mistakenly identifying benign instances as malignant, which is crucial in medical diagnostics.

## Conclusion

The logistic regression model proved to be highly effective for this dataset, offering a significant trade-off between sensitivity and specificity. The chosen parameters allowed the model to achieve a high level of accuracy, making it a viable tool for clinical support in diagnosing breast cancer. Future work might explore the integration of this model into clinical decision-support systems and the application of ensemble techniques to further enhance its predictive power.

## Deployment
The application is deployed on Heroku, allowing users to interact with the model in real-time. This deployment serves as a practical demonstration of how machine learning models can be integrated into web applications and accessed via standard web interfaces.

 - Live Application: [Visit Heroku App](https://breastcancerlogreg-c9c8adb2a410.herokuapp.com/)


## Reference

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [Breast Cancer Wisconsin (Original) Dataset](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original)). Irvine, CA: University of California, School of Information and Computer Science.
