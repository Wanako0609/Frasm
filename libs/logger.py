from loguru import logger

def error_and_exit(instruction, message):
    logger.critical(f"{instruction} : {message}")
    exit(1)
