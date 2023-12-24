import mlflow 
from mlflow_utils import create_mlflow_experiment, get_mlflow_experiment

if __name__ == "__main__":
    experiment_id = create_mlflow_experiment(
        experment_name='testing_mlflow2',
        artifact_location="testing_mlflow2_artifacts",
        tags={"env":"dev", "version":"1.0.0"}
    )
    
    # mlflow.set_experiment(experiment_name="testing_mlflow2")
    # # you can set experiment with above method or directly put a parameter in startrun method
    
    with mlflow.start_run(run_name = "testing", experiment_id= experiment_id) as run:
        # your ml code goes here
        
        mlflow.log_param("learning_rate", 0.01)
        
        # print info
        print()
        print("Run_ID : ", run.info.run_id)
        print("Experiment_ID : ", run.info.experiment_id)
        print("Status :", run.info.status)
        print("Start_time : ", run.info.start_time)
        print("End _ime : ", run.info.end_time)
        print("lifecycle_Stage : ", run.info.lifecycle_stage)