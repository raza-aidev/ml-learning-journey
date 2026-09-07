import logging

logger = logging.getLogger(__name__)

def connect(Host):
    logger.debug(f"Connecting to Host: {Host}")

    logger.info(f"Database is connected!")