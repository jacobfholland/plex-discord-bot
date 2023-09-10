import coloredlogs
import logging
from config.config import Config


def setup_logger(name):

    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR
    }
    # Set up a logger
    logger = logging.getLogger(name)
    logger.setLevel(log_levels.get(Config.LOG_LEVEL))

    # Add colored handler for console output
    coloredlogs.install(level=Config.LOG_LEVEL, logger=logger)

    # Create a FileHandler for logging to a file
    file_handler = logging.FileHandler('mediarr.log')
    file_handler.setLevel(log_levels.get(Config.LOG_LEVEL))

    # Create a formatter and set it for the file handler
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger


logger = setup_logger("mediarr")
