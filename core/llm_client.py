import json
import os
from typing import List, Dict

from openai import OpenAI
from openai.types.chat import ChatCompletion

import router
from core.user import User
from logger_setup import logger
from messages import create