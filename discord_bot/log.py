from app.config import Config
from app.log import setup_logger

logger = setup_logger(f"{Config.APP_NAME.lower()}.discord", Config)
