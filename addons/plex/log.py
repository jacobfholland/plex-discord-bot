from app.log import setup_logger
from addons.plex.config import Config

logger = setup_logger(f"{Config.APP_NAME.lower()}.plex", Config)
