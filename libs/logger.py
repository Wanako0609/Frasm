from loguru import logger
import sys

class FrasmExecutionError(Exception):
    def __init__(self, categorie, message):
        super().__init__(f"[{categorie}] {message}")

logger.remove()  # retire la config par défaut
logger.add(sys.stdout,
           format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                  "<level>{level: <8}</level> | "
                  "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                  "<level>{message}</level>",
           colorize=True,
           level="INFO")

def error_and_exit(instruction, message):
    raise FrasmExecutionError(instruction, message)