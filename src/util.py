from omegaconf import OmegaConf


def get_tournament_config():
    return OmegaConf.load("config.yaml")
