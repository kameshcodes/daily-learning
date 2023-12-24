# logging parameter is important because it allows you to keep track of hypterparmeters you used during training phase
import mlflow 
from mlflow_utils import get_mlflow_experiment

if __name__ == "__main__":
    experiment = get_mlflow_experiment(experiment_name="testing_mlflow1")
    print("Name :", experiment.name)
    
    with mlflow.start_run(run_name="logging_params", experiment_id=experiment.experiment_id) as run:
        #ml code here
        mlflow.log_param("learning_rate",0.01)
        
        parameters = {
            "learning_rate" : 0.01,
            "epochs": 10,
            "batch_size": 128,
            "loss_function": "mse",
            "optimiser":"adam"
        }
        
        mlflow.log_params(parameters)
        
