import mlflow
from mlflow_utils import get_mlflow_experiment

if __name__ == "__main__":
    
    experiment = get_mlflow_experiment(experiment_name="testing_mlflow1")
    print("Name: ", experiment.name)
    
    with mlflow.start_run(run_name = "logging_metrics", experiment_id=experiment.experiment_id) as run:
        mlflow.log_metric("mse", 0.01)
        
        metrics = {
            "mse": 0.01,
            "mae":0.01,
            "rmse":0.01,
            "r2":0.01
        }
        mlflow.log_metrics(metrics)
        
        # print run info
        print()
        print("Run_ID : ", run.info.run_id)
        print("Experiment_ID : ", run.info.experiment_id)
        print("Status :", run.info.status)
        print("Start_time : ", run.info.start_time)
        print("End _ime : ", run.info.end_time)
        print("lifecycle_Stage : ", run.info.lifecycle_stage)
        
        
        