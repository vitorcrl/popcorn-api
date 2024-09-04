# app/logger.py
from loguru import logger

# Configuração básica do Loguru
logger.add("logs/debug.log", rotation="500 MB", level="DEBUG", retention="10 days")
