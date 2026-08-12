import logging 

logging.basicConfig(level=logging.INFO)
                    # (format='%(asctime)s - %(levelname)s - %(levelno)d - %(name)s' 
                    # filename="test-log.log", 
                    # filemode="a")

logging.warning("This is the warning!")
logging.error("This is the error")
logging.critical("This is the critical message!")
