import os
import io
import cProfile
import pstats

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


# from logger_setup import logger
# from core.platform import Platf


def create_app():
    func = 'create_app'
    load_dotenv()
    env = os.getenv("ENV", "LOCAL")
    logger.info(f" in {func} ENV {env} loaded\n")
    VALID_ENVS = {"LOCAL", "DEV", "STAGING", "PROD"}
    
    
    if env not in VALID_ENVS:
        logger.error("Invalid ENV Value")
        
    install_missing_or_missmatched()
    
    ai_provider = os.getenv("AI Provider")
    if ai_provider != test_llm_connection(ai_provider)