from functools import partial
import logging
from app.log import logger
from config.config import Config


def bind_methods(obj, methods):
    logger.debug(f"[UTILS] Binding class methods on {obj.__class__.__name__}")
    for method in methods:
        logger.debug(
            f"[UTILS] Binding {method.__name__} to {obj.__class__.__name__}")
        setattr(obj, method.__name__, partial(method, obj))


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


def pretty_print_element(element, indent=0):
    """
    Pretty print the keys (tags) and values (text) of an xml.etree.ElementTree.Element.

    :param element: Element to be pretty printed.
    :param indent: Current indentation level for nice formatting.
    """

    # Print the current element
    print('  ' * indent +
          f'Tag: {element.tag}, Text: {element.text.strip() if element.text else None}')

    # Iterate over child elements and pretty print them, increasing the indentation
    for child in element:
        pretty_print_element(child, indent + 1)
