from omegaconf import OmegaConf

SKIP_MINOR_WARNINGS = False


def get_general_config(config: str = "tournament_settings.yaml"):
    conf = OmegaConf.load(config)
    global SKIP_MINOR_WARNINGS
    SKIP_MINOR_WARNINGS = conf.misc.skip_minor_warnings
    print(SKIP_MINOR_WARNINGS)
    return conf["general"]


def get_sheet_config(config: str = "tournament_settings.yaml"):
    config = OmegaConf.load(f"{config}")
    stats_type = config.stats_sheet
    return config[stats_type]


def bwarning(origin: str, msg: str, is_minor: bool = False):
    if SKIP_MINOR_WARNINGS:
        return
    print(f"[{'MINOR ' if is_minor else ''}WARNING | {origin}]: {msg}")


def fancy_print(s: str) -> None:
    print("-" * 30)
    print(s)
    print("-" * 30)
