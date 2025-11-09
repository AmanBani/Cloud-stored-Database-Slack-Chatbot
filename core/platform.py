import os
import base64
import io

from fastapi import FastAPI
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from core.platform


class PlatformBase:
    
    def __init__(self):
        