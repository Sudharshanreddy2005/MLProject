import os
import sys
import dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    """
    Save any python object to file using dill
    Example: model, preprocessor, etc.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info(f"Object saved successfully at: {file_path}")

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load any python object from file using dill
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    """
    Train multiple ML models and return:
    - report: {model_name: r2_score}
    - best_models: {model_name: trained_best_model_object}
    """
    try:
        report = {}
        best_models = {}

        for model_name, model in models.items():
            logging.info(f"Training model: {model_name}")

            # ✅ Fix: CatBoost cannot be used with sklearn GridSearchCV (Python 3.13 tags issue)
            if "catboost" in model_name.lower():
                logging.info("CatBoost detected -> skipping GridSearchCV")
                model.fit(X_train, y_train)
                y_test_pred = model.predict(X_test)

                score = r2_score(y_test, y_test_pred)
                report[model_name] = score
                best_models[model_name] = model
                continue

            param_grid = params.get(model_name, {})

            gs = GridSearchCV(model, param_grid, cv=3)
            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_

            y_test_pred = best_model.predict(X_test)
            score = r2_score(y_test, y_test_pred)

            report[model_name] = score
            best_models[model_name] = best_model

            logging.info(f"{model_name} R2 Score: {score}")

        return report, best_models

    except Exception as e:
        raise CustomException(e, sys)
