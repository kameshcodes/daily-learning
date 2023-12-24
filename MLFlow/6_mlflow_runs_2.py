import mlflow

# allow you to log all the information associated with single run of experiment
# create a run in default

if __name__ == "__main__":
    
    # # Above we need mlflow.end_run() to finish the run. We can use with statement to ensure that
    # # the experiment we started will end properly.
    
    # MLFlow run 2
    with mlflow.start_run(run_name = "mlflow_runs2") as run: #we are assigning the output of method to run variable
        # you ML code here
        mlflow.log_param("lr", 0.01)
        
        print("RUN ID :", run.info.run_id)
        print(run.info)