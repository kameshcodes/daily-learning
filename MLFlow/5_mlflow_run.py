import mlflow

# allow you to log all the information associated with single run of experiment
# create a run in default

if __name__ == "__main__":
    
    ## MLFLow run 1
    mlflow.start_run()
    
    # your ml code goes here, currently default
    
    mlflow.log_param("learning rate", 0.01)
    
    # end the mlflow run 
    mlflow.end_run()   
    # Here we need mlflow.end_run to finish the run. We can use with statement to ensure that
    # the experiment we started will end properly.
