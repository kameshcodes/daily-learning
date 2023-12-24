import mlflow
from mlflow_utils import get_mlflow_experiment

if __name__ == "__main__":
    #retrieve ml flow experiments
    experiment = get_mlflow_experiment(experiment_name="testing_mlflow2")
    
    print()
    print(f"Name: {experiment.name}")
    print(f"Experiment ID: {experiment.experiment_id}")
    print(f"Artifact Location: {experiment.artifact_location}")
    print(f"Tags: {experiment.tags}")
    print(f"Lifecycle_stage:{experiment.lifecycle_stage}")
    print(f"Creating Timestamp: {experiment.creation_time}")