import inspect
import logging
def test_loggingDemo():
    loggername = inspect.stack([1][3])
    logger = logging.getLogger(loggername)
    fileHandler = logging.FileHandler('Logfile.log')
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s:%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    logger.debug("debug log")
    logger.info("information")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

test_loggingDemo()