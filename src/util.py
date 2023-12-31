from omegaconf import OmegaConf

SKIP_MINOR_WARNINGS = False


def get_general_config(config_path: str = "tournament_settings.yaml"):
    info(f"Loading general config from {config_path}")
    conf = OmegaConf.load(config_path)
    global SKIP_MINOR_WARNINGS
    SKIP_MINOR_WARNINGS = conf.misc.skip_minor_warnings
    return conf["general"]


def get_sheet_config(config_path: str = "tournament_settings.yaml"):
    config = OmegaConf.load(f"{config_path}")
    stats_type = config.stats_sheet
    info(f"Loading sheet config {stats_type} from {config_path}")
    return config[stats_type]


def info(msg: str) -> None:
    print(f"[INFO]: {msg}")


def bwarning(origin: str, msg: str, is_minor: bool = False) -> None:
    if SKIP_MINOR_WARNINGS and is_minor:
        return
    print(f"[{'MINOR ' if is_minor else ''}WARNING] [{origin}]: {msg}")


def fancy_print(s: str) -> None:
    print("_" * 100)
    print(s)
    print("—" * 100)
