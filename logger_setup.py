import os 
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()


ENV = os.getenv("ENV","LOCAL").lower()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INGO").upper()


