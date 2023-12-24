import mlflow
import pandas as pd
from mlflow_utils import get_mlflow_experiment

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import PrecisionRecallDisplay
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt

if __name__=="__main__":
    
    run_id = "bdf2515ca72045159f7827ad77350328"
    
    X, y = make_classification(n_samples = 1000, 
                               n_features = 10,
                               n_redundant = 5,
                               random_state = 42)
    
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    #Method 1
    #model_uri = f'runs:/{run_id}/rfc'
    
    #method 2
    model_uri = "file:///C:/Users/kames/mlflowtut/testing_mlflow_artifacts/bdf2515ca72045159f7827ad77350328/artifacts/rfc"
    rfc = mlflow.sklearn.load_model(model_uri=model_uri)
    
    y_pred = rfc.predict(X_test)
    y_pred = pd.DataFrame(y_pred, columns = ["prediction"])
    print(y_pred.head())