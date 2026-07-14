import os
import logging
from datetime import datetime
import structlog

# Project root = two levels up from this file (logger/ -> research_and_analysts/ -> project root)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CustomLogger:
    def __init__(self, log_dir="logs"):
        # logs/ folder at project root level
        self.logs_dir = os.path.join(PROJECT_ROOT, log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        log_file = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

    def get_logger(self, name=__file__):
        logger_name = os.path.basename(name)

        stdlib_logger = logging.getLogger(logger_name)
        stdlib_logger.setLevel(logging.INFO)

        if not stdlib_logger.handlers:
            formatter = logging.Formatter('%(message)s')

            file_handler = logging.FileHandler(self.log_file_path)
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            stdlib_logger.addHandler(file_handler)
            stdlib_logger.addHandler(console_handler)

        structlog.configure(
            processors=[
                structlog.stdlib.add_log_level,
                structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
                structlog.processors.EventRenamer(to="event"),
                structlog.processors.JSONRenderer(),
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )

        return structlog.get_logger(logger_name)

