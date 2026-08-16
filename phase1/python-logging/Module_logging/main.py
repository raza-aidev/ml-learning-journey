import logging
import server
import database

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(module)s : %(filename)s | %(message)s',
    filename = "./logs/logs.log",
    filemode = "a"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

filehandler = logging.FileHandler("./logs/logs.log")
filehandler.setLevel(logging.DEBUG)

logger.addHandler(filehandler)


if __name__ == "__main__":
    server.Start(8080)
    database.connect("localhost")