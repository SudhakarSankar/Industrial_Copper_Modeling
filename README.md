# Industrial_Copper_Modeling


📌 Copper Industry Price Prediction & Lead Classification

📖 Overview
This project develops machine learning models to predict selling prices of copper products and classify lead status (Won/Lost). The analysis addresses skewness, outliers, and noisy data, enabling better decision-making in pricing and sales strategies.

📊 Key Features
✔ Data Cleaning: Handled missing values, outliers, and formatted dataset.
✔ Exploratory Data Analysis (EDA): Visualized pricing trends, outliers, and feature distributions.
✔ Feature Engineering: Applied encoding techniques, transformed skewed data, and removed highly correlated features.
✔ Machine Learning Models:
     🔹 Regression: Predicted Selling_Price using Extra Trees & XGBoost.
     🔹 Classification: Predicted Status (Won/Lost) using ExtraTreesClassifier & Logistic Regression.
✔ Model Deployment: Built a Streamlit app for interactive predictions.

🔧 Technologies Used
🟢 Python (Pandas, NumPy, Matplotlib, Seaborn)
🟢 Scikit-learn & XGBoost (Machine Learning)
🟢 Streamlit (Model Deployment)
🟢 Pickle (Model Storage)

📊 Key Insights
📌 Pricing Factors: Selling price is influenced by material type, thickness, and quantity.
📌 Lead Conversion: Successful deals depend on customer segment, order quantity, and region.
📌 Model Accuracy: Regression and classification models effectively reduce prediction errors.

🚀 Future Improvements
✔ Implement deep learning models for better accuracy.
✔ Enhance feature engineering with industry-specific insights.
✔ Deploy as a web service using Flask/FastAPI for broader usability.
