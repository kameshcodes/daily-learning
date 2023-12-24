import mlflow

# Experiment in ML context is execution of a ML Workflow 
# ML workflow could be training a ml model on a partiular dataset using a specific set of parameters and configurations
# MLflow will track all those parameter, config and artifect that a workflow is generating
# artifect are all the object and files that are being generated while running the workflow

if __name__ == "__main__":
    mlflow.create_experiment(
        name = "testing_mlflow1", 
        artifact_location="testing_mlflow_artifacts",
        tags = {"env":"dev", "version":"1.0.0"}
    )
    
