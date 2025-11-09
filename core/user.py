import os
from collections import deque
from dotenv import load_dotenv

from logger_setup import logger

class User:
    
    def __init__(
        self,
        user_id: str,
        user_name: str,
        bot_name: str = None,
        user_role: str = None,
        user_context: str = None,
        max_history: int = 100,
        
        ):
            load_dotenv()
            
            
            self.user_id = user_id
            self.user_name = user_name
            self.history = deque(maxlen=max_history)
            
            self.bot_name = bot_name or os.getenv("BOT_NAME","JARVIS")
            self.user_role = user_role or os.getenv("USER_ROLE", "A excellent personal assistant")
            self.user_context = user_context or os.getenv(
                "USER_CONTEXT",
                "A batabse based on particular user output results that provides context of information ofbout a particluart company"
            )
            
    def add_message(self, role: str, content: str):
        func = "add_message"
        logger.info(f"entered {func} \n")
        self.history.append({"role":role,"content":content})
    
    
    def get_history(self):
        func = "get_history"
        logger.info(f"enetered {func} \n")
        return list(self.history)
    
    def get_name(self):
        func = "get_name"
        logger.info(f"entered {func} \n")
        return self.user_name
    
    def updated_user_role(self, user_role:str):
        func = "updated_user_role"
        logger.info(f"entere {func} \n")
        self.user_role = user_role
    
    def updated_user_context(self, user_context: str):
        func = "updated_user_context"
        logger.info(f"entered {func} \n")
        self.user_context = user_context
        
                