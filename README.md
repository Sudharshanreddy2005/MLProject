# 🎓 Student Performance Prediction (Math Score) – End-to-End ML Project

This project is an **end-to-end Machine Learning pipeline** that predicts a student's **Math Score** based on demographic and academic features such as gender, race/ethnicity, parental education level, lunch type, test preparation course, reading score, and writing score.

The project includes:
- Data ingestion
- Data preprocessing & transformation
- Model training with multiple ML algorithms + hyperparameter tuning
- Model evaluation (R2 Score)
- Model saving (`model.pkl`, `preprocessor.pkl`)
- Flask web application for real-time prediction

---

## 📌 Project Overview

### ✅ Problem Statement
Predict the **Math Score** of a student using the following inputs:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

This prediction can help identify students who may need academic support.

---

## ⚙️ Tech Stack Used

### 💻 Programming / Libraries
- Python 3.13
- Pandas, NumPy
- Scikit-learn
- CatBoost
- XGBoost
- Dill (for saving/loading objects)

### 🌐 Web Application
- Flask
- HTML (Templates)

---

## 🧠 Machine Learning Models Used

During training, the system evaluates multiple models such as:
- Linear Regression
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- KNeighbors Regressor
- XGBRegressor
- CatBoostRegressor
- AdaBoostRegressor

✅ Best model is selected based on **R2 Score**.

---

## 📁 Project Structure

MLProject/  
│── app.py  
│── artifacts/  
│   ├── data.csv  
│   ├── train.csv  
│   ├── test.csv  
│   ├── model.pkl  
│   ├── preprocessor.pkl  
│  
│── notebook/  
│   └── data/  
│       └── stud.csv  
│  
│── src/  
│   ├── __init__.py  
│   ├── exception.py  
│   ├── logger.py  
│   ├── utils.py  
│  
│   ├── components/  
│   │   ├── __init__.py  
│   │   ├── data_ingestion.py  
│   │   ├── data_transformation.py  
│   │   ├── model_trainer.py  
│  
│   ├── pipeline/  
│   │   ├── __init__.py  
│   │   ├── train_pipeline.py  
│   │   ├── predict_pipeline.py  
│  
│── templates/  
│   ├── index.html  
│   ├── home.html  
│  
│── README.md  

---

## 🔥 ML Pipeline Workflow

### ✅ Step 1: Data Ingestion
- Reads dataset from:
  `notebook/data/stud.csv`
- Saves:
  - raw dataset → `artifacts/data.csv`
  - train dataset → `artifacts/train.csv`
  - test dataset → `artifacts/test.csv`

---

### ✅ Step 2: Data Transformation
Applies preprocessing using `ColumnTransformer`:
- Numerical columns: `reading_score`, `writing_score`
  - Median Imputer
  - StandardScaler

- Categorical columns:
  - Most Frequent Imputer
  - OneHotEncoder (`handle_unknown="ignore"`)
  - StandardScaler

✅ Preprocessor is saved as:
`artifacts/preprocessor.pkl`

---

### ✅ Step 3: Model Training
- Trains multiple models
- Uses GridSearchCV for tuning (except CatBoost)
- Selects best model based on test R2 score

✅ Saves trained model:
`artifacts/model.pkl`

---

### ✅ Step 4: Prediction Pipeline
- Loads:
  - `model.pkl`
  - `preprocessor.pkl`
- Transforms input data
- Predicts Math Score

---

## ▶️ How to Run the Project

### ✅ Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd MLProject
✅ Step 2: Install Dependencies
bash
Copy code
pip install -r requirements.txt
If requirements.txt is not available, install manually:

bash
Copy code
pip install pandas numpy scikit-learn flask dill catboost xgboost
✅ Step 3: Train the Model (Generate artifacts)
bash
Copy code
python -m src.pipeline.train_pipeline
After training, artifacts/ folder will include:

model.pkl

preprocessor.pkl

✅ Step 4: Run Flask App
bash
Copy code
python app.py
Open:
http://127.0.0.1:5000/predictdata

🖥️ Web App Input Fields
User provides:

Gender

Race/Ethnicity

Parental Level of Education

Lunch type

Test preparation course

Reading score

Writing score

✅ Output:

Predicted Math Score (example: 66.15)

✅ Output Example
Prediction Result:
Math Score: 66.15

🚀 Future Improvements
Can add:

Model explainability (SHAP / feature importance)

Deployment (AWS / Render / Railway)

Better UI using Bootstrap

Logging improvement and monitoring

Saving prediction history
