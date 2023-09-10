from app.config import Config


def mask(input):
    if not Config.LOG_SENSITIVE_DATA:
        return '*' * len(input)
    return input


def vars(self):
    print(f"{self.__class__.__name__}" + "(")
    print("\t{")
    for k, v in self.__dict__.items():
        line = f"\t\t'{k}': "
        if isinstance(v, str):
            line += f"'{v}'"
        else:
            line = f"{line} {v}"
        print(line)
    print("\t}")
    print(")")
