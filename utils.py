from json import dump, load


CONFIG_PATH = "./config.json"


def config_read(path: str = CONFIG_PATH):
    with open(path) as fh:
        config = load(fh)

    return config


def config_write(data, path: str = CONFIG_PATH):
    with open(path, "w") as outfile:
        dump(data, outfile)

    return data


def config_get(parameter: str, path: str = CONFIG_PATH):
    config = config_read(path)

    return config[parameter] if parameter in config else None


def config_get_params(parameters: list, path: str = CONFIG_PATH):
    config = config_read(path)

    result = [config[parameter] for parameter in parameters]

    return result


def config_set(parameter, value, path: str = CONFIG_PATH):
    config = config_read(path)

    config[parameter] = value

    config_write(config)

    return config[parameter] if parameter in config else None


def md5(string):
    from hashlib import md5 as _md5

    return _md5(string.encode("utf-8")).hexdigest()


class _AutoInit:
    def __init__(self, **kwargs) -> None:
        for key, value in list(kwargs.items()):
            self.__dict__[key] = value


class PrintData:
    def __init__(self, professor_name, subject_name) -> None:
        pass

