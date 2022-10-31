# to override a given parameter
# python main.py parameter1=boo

# that being said, for ML Projects, my main is used to train a model
# and upload it to a place where prod can call the model

import hydra
from omegaconf import DictConfig, OmegaConf
import pandas as pd
from sklearn import datasets
import numpy as np
from src.data.SampleTransformer import SampleTransformer
from src.model.SampleModel import SampleModel
# I want to illustrate the use of pipeline
from sklearn.pipeline import Pipeline

@hydra.main(version_base=None, config_path="../config", config_name="config")
def main(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))    #we're just going to print out the config
    
    # Data loading scripts should be moved to library
    data = datasets.load_boston()
    X = pd.DataFrame(data['data'])
    X.columns = data['feature_names']
    y = pd.DataFrame(data['target'])
   
    # ML Data wrangling and predict should be 
    # done via a pipeline because then it's clear in one place
    # what the actual steps are
    # this also makes it a bit easier to refactor the code
    # going forward

    # Normally commandline arguments are to train a model, pickle
    # and upload to whatever model store 
    pipe = Pipeline(steps=[
        ('scale', SampleTransformer()),
        ('predict', SampleModel())])
    y_hat = pipe.fit_transform(X, y)
    print(np.corrcoef(y_hat, y[0]))

if __name__ == "__main__":
    main()