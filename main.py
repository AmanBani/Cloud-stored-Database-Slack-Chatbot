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