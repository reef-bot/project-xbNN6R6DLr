# logging.py

import logging

class ModerationLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('ModerationLogger')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_moderation_action(self, action_type, user_id, reason):
        self.logger.info(f'{action_type} - User ID: {user_id} - Reason: {reason}')

    def log_chat_activity(self, message):
        self.logger.info(f'Chat Activity - Message: {message}')

# End of logging.py