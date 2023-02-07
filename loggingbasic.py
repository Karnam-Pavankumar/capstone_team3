import logging
logging.basicConfig(filename="log.txt",level=logging.WARNING)
print("Log Demo")
logging.debug("Debug information")
logging.info("Info Information")
logging.warning("warning information")
logging.error("Error Information")
logging.critical("Critical Information")