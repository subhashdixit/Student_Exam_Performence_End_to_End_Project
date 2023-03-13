# Train the model
# different type of models
# evaluation as well
# model pusher code will alse be present 
# This is mainly for the training purpose
# Try different algorithms to solve the problem, whichever will give good accuracy choose that
import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRFRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models 

# for every components create config 
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    # Input will be output of data transformation 
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Spliting training and test input data")
            X_train, y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            ) 
            
            models = {
                "Random Forest":RandomForestRegressor(),
                "Decison Tree":DecisionTreeRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regression":LinearRegression(),
                "K-Neighbours Regressor":KNeighborsRegressor(),
                "XGB Regressor":XGBRFRegressor(),
                "Catboosting Regressor":CatBoostRegressor(),
                "Adaboost Regressor":AdaBoostRegressor()
            }

            # evaluate model is a function in utils
            model_report:dict=evaluate_models(X_train=X_train, y_train=y_train,X_test=X_test, y_test=y_test, models=models)

            # To get the best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # To get the best model name from dict
            best_model_name  = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info(f"Best model found on both training and testing dataset")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            predicted = best_model.predict(X_test)
            r2_test_score = r2_score(y_test,predicted)
            
            return r2_test_score
        
        except Exception as e:
            raise CustomException(e,sys)