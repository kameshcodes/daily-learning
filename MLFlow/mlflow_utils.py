import mlflow
from typing import Any

def create_mlflow_experiment(experment_name: str, artifact_location: str, tags:dict[str,Any]) -> str:
    """
    Creates a new new ML flow experiment with given attributes

    Args:
        experment_name (str): take the name of experiment
        artifact_location (str): location of artifects
        tags (dict[str,Any]): take a the tags in form of a dict

    Returns:
        str: experiment id 
    """
    try:
        experment_id = mlflow.create_experiment(
            name = experment_name,
            artifact_location=artifact_location,
            tags=tags
        )
    except:
        print(f"Experiment {experment_name} already exists.")
        experment_id = mlflow.get_experiment_by_name(experment_name).experiment_id
    return experment_id

def get_mlflow_experiment(experiment_id:str=None, experiment_name:str=None) -> mlflow.entities.Experiment:
    """
    Retrieve the mlflow experiment with given id or name.

    Args:
        experiment_id (str, optional): the Id of the experiment. Defaults to None.
        experiment_name (str, optional): the name of the experiment. Defaults to None.

    Returns:
      experiment: mlflow.entities.Experiment: The mlflow experiment with given id or name.
    """
    if experiment_id is not None:
        experiment = mlflow.get_experiment(experiment_id)
    elif experiment_name is not None:
        experiment = mlflow.get_experiment_by_name(experiment_name)
    else:
        raise ValueError("Either experiment_id or experiment_name must be provided.")
    return experiment
