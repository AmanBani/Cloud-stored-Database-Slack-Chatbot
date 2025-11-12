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


def create_success_response(data: Any, message: Optional[str] = None) -> Dict[str, Any];
    response = {
        "type":"success",
        "data":data
    }
    
    if message:
        response["mesage"] = message
    
    logger.debug("Created Success response")
    return response


def validate_event(body: Dict, user_manage) -> Union[Dict[str,str], None]:
    
