import logging

logger = logging.getLogger(__name__)

def Start(port):
    logger.debug(f"Starting server on port: {port}")
    logger.info("Server has started.")