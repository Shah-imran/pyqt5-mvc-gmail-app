import logging
import os
from . import AppConfig

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(f"{os.path.join(os.getcwd(), AppConfig.base_dir)}/"
                                  f"{AppConfig.log_filename}.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)
