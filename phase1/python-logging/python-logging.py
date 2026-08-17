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

# import logging

# #Create Logger
# logger = logging.getLogger("python-logging")
# logger.setLevel(logging.DEBUG)

# #Create Handler
# file_handler = logging.FileHandler("test-log.log")
# file_handler.setLevel(logging.DEBUG)

# #Add Handler
# logger.addHandler(file_handler)

# #Write to file
# logger.debug("Adding Debug message")
# logger.info("Adding logger info")
# logger.warning("Adding warning message")
# logger.error("Adding error message")
# logger.critical("Adding Critical")

# import logging

# #Create logger
# logger = logging.getLogger("python-logging")
# logger.setLevel(logging.DEBUG)


# # create console handler
# console_log = logging.StreamHandler()
# console_log.setLevel(logging.DEBUG)

# #add handler
# logger.addHandler(console_log)

# logger.debug("Console_Logs - This is debug message")
# logger.info("Console_logs - This is info logs")
# logger.warning("COnsole_logs - This is warning logs")

# #Create file handler
# file_handler = logging.FileHandler("test-log.log")
# file_handler.setLevel(logging.DEBUG)

# #adding handler
# logger.addHandler(file_handler)

# # logger.debug("Adding Debug message to logs")
# # logger.info("Adding info to logs")
# # logger.warning("Adding wrning message to logs")


# import logging

# # creating logger - L
# logger = logging.getLogger("python-logging")
# logger.setLevel(logging.DEBUG)

# # Creating handler - H
# file_handler = logging.FileHandler("test-log.log")
# file_handler.setLevel(logging.DEBUG)

# # Creating console handler
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# #Adding handler in logger
# logger.addHandler(file_handler)
# logger.addHandler(console)

# #creating formatter - F
# formater = logging.Formatter(
#     '%(asctime)s : %(levelname)s | %(name)s | %(message)s'
# )
# # formater.setLevel(logging.DEBUG)

# #Adding formatter to handler
# file_handler.setFormatter(formater)

# logger.debug("This message is to write debug.")

import logging

def set_logger(name, logger_level = logging.ERROR, file_name = "setup_logs.log"):

    #Creating logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    #creating file handler
    filehandler = logging.FileHandler(file_name)
    filehandler.setLevel(logging.DEBUG)

    #creating console handler
    console = logging.StreamHandler()
    console.setLevel(logger_level)

    #creating formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s: %(name)s | %(message)s'
    ) 

    #Adding formatter to handler
    filehandler.setFormatter(formatter)
    console.setFormatter(formatter)

    #Adding handler to logger
    logger.addHandler(filehandler)
    logger.addHandler(console)

    return logger

logger = set_logger("python-logging")

logger.debug("This message to debug.")
logger.info("This message to add information")
logger.error("This is the error message")

