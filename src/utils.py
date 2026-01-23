from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from src.logger import logging
import sys

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        best_models = {}

        for model_name, model in models.items():
            logging.info(f"Training model: {model_name}")

            # ✅ CatBoost: no GridSearchCV
            if "catboost" in model_name.lower():
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

        return report, best_models

    except Exception as e:
        raise CustomException(e, sys)
