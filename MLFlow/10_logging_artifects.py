import mlflow
from mlflow_utils import get_mlflow_experiment

if __name__ == "__main__":
    
    experiment = get_mlflow_experiment(experiment_name="testing_mlflow1")
    print("Name: ", experiment.name)
    
    with mlflow.start_run(run_name = "logging_metrics", experiment_id=experiment.experiment_id) as run:
        
        
        # create a textfile that says hello world
        with open("hello.txt", "w") as f:
            f.write("Hello World!")
        with open("hello2.txt", "w") as f:
            f.write("Hello World2!")
        
        #mlflow.log_artifact(local_path="hello.txt", artifact_path="txt file")
        ## the log_artifact() method can log only one file at time use 'log_artifacts()' to log every file
        mlflow.log_artifacts(local_dir="./testing_mlflow_artifacts", artifact_path="run_artifacts") #get this error fixed

        
        # print run info
        print()
        print("Run_ID : ", run.info.run_id)
        print("Experiment_ID : ", run.info.experiment_id)
        print("Status :", run.info.status)
        print("Start_time : ", run.info.start_time)
        print("End _ime : ", run.info.end_time)
        print("lifecycle_Stage : ", run.info.lifecycle_stage)
        
        
        