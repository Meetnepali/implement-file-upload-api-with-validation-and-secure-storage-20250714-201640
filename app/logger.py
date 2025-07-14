import logging
import sys
import json

def get_audit_logger():
    logger = logging.getLogger("audit")
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger

class JsonFormatter(logging.Formatter):
    def format(self, record):
        if isinstance(record.msg, dict):
            return json.dumps(record.msg)
        return record.getMessage()
