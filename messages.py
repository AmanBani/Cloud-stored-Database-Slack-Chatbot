import json
from typing import List, Dict, Any, Tuple, Union, Optional

from logger_setup import logger

def create_error_message(message: str, details: Optional[Any] = None) -> Dict[str, Any]:
    response = {
        "type": "error",
        "data" : {
            "message": message
        }
    }
    
    if details:
        response["data"]["details"] = details
        
    logger.debug(f"Created error response : {message}")
    return response
