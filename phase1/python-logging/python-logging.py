""" this is the first set of logging method """

# import logging 

# # logging.basicConfig(level=logging.INFO)
# #                     # (format='%(asctime)s - %(levelname)s - %(levelno)d - %(name)s' 
# #                     # filename="test-log.log", 
# #                     # filemode="a")

# # logging.warning("This is the warning!")
# # logging.error("This is the error")
# # logging.critical("This is the critical message!")

# import logging

# logging.basicConfig(level = logging.DEBUG, 
#                     datefmt = '%d:%m:%Y %H:%M:%S',
#                     format = " %(asctime)s | %(name)s:%(lineno)d | %(levelname)s : %(message)s", 
#                     filename = "test-log.log", 
#                     filemode = "a")

# # logger = logging.getLogger("python-logging")
# logger = logging.getLogger("python-logging")


# logger.setLevel(logging.DEBUG)
# logger.debug("This is the message for info")
# logger.error("This is the error")
# logger.info("This is the message of information ")
# logger.warning("This is the Warning")
# logger.critical("This is critile message")

import logging

#Create Logger
logger = logging.getLogger("python-logging")
logger.setLevel(logging.DEBUG)

#Create Handler
file_handler = logging.FileHandler("test-log.log")
file_handler.setLevel(logging.DEBUG)

#Add Handler
logger.addHandler(file_handler)

#Write to file
logger.debug("Adding Debug message")
logger.info("Adding logger info")
logger.warning("Adding warning message")
logger.error("Adding error message")
logger.critical("Adding Critical")

