# to override a given parameter
# python main.py parameter1=boo

import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="../config", config_name="config")
def main(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))    #we're just going to print out the config

if __name__ == "__main__":
    main()