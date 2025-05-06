import logging
from datetime import datetime
import os
import sys

class ChatLogger:
    def __init__(self):
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)
        self._setup_logger()
    
    def _setup_logger(self):#sistema de log
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        log_file = f"{self.log_dir}/nunes_chat_{datetime.now().strftime('%Y%m%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger('nunes_chat')
    
    def log_interaction(self, user_input: str, bot_response: str):#registra interações
        self.logger.info(f"USER: {user_input}")
        self.logger.info(f"BOT: {bot_response}")
    
    def log_error(self, error: Exception):#erros
        self.logger.error(f"ERROR: {str(error)}", exc_info=True)

logger = ChatLogger()