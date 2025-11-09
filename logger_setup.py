import os 
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()


ENV = os.getenv("ENV","LOCAL").lower()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INGO").upper()
BOT_NAME = os.getenv("BOT_NAME", os.getenv("CHATBOT_NAME", "CHATBOT")).lower()


logger = logging.getLogger(BOT_NAME)
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
logger.propagate = False

if not logger.handlers:
    fortmatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
    logger.addHandler(console_handler)
    
    if ENV in ("LOCAL", "DEV"):
        base_dir = os.path.dirname(__file__)
        log_dir = os.path.join(base_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, "slackbot.log")
        
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5_000_000, backupCount=3, encoding="utf-8"
        )
        
        file_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
        file_handler.setFormatter(fortmatter)
        logger.addHandler(file_handler)
        
    logger.info("Logging Initialized | env=%s | level=%s | bot=%s, ENV,LOG_LEVEL,BOT_NAME")
    
    
    
    