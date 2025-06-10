# app/log_config.py
import logging
import logging.config
import sys
from pathlib import Path
from datetime import datetime

# 确保日志目录存在
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# 当前日期作为文件名的一部分
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

def setup_logging():
    """配置应用程序日志记录"""
    
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            },
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "fmt": "%(asctime)s %(levelname)s %(name)s %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "standard",
                "stream": sys.stdout
            },
            "file_info": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "standard",
                "filename": LOG_DIR / f"app_{CURRENT_DATE}.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "encoding": "utf8"
            },
            "file_error": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "standard",
                "filename": LOG_DIR / f"error_{CURRENT_DATE}.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "encoding": "utf8"
            },
            "file_auth":{
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "filename": LOG_DIR / f"auth_{CURRENT_DATE}.log",
                "formatter": "standard",
                "maxBytes": 10*1024*1024,  # 10MB
                "backupCount": 5,
                "encoding": "utf8"
            }
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["console", "file_info", "file_error"],
                "level": "DEBUG",
                "propagate": True
            },
            "app":{
                "handlers": ["console", "file_info", "file_error"],
                "level": "DEBUG",
                "propagate": False
                },
            "app.auth":{
                "handlers": ["console", "file_auth", "file_error"],
                "level": "DEBUG",
                "propagate": False
                },
            "uvicorn": {
                "handlers": ["console", "file_info", "file_error"],
                "level": "INFO",
                "propagate": False
            },
            "uvicorn.error": {
                "level": "INFO",
                "propagate": False
            },
            "uvicorn.access": {
                "handlers": ["console", "file_info"],
                "level": "INFO",
                "propagate": False
            },
            "sqlalchemy": {
                "handlers": ["file_info"],
                "level": "WARNING",
                "propagate": False
            },
            "sqlalchemy.engine": {
                "handlers": ["file_error", "file_info"],
                "level": "INFO",
                "propagate": False
            },
            "sqlalchemy.pool": {
                "handlers": ["file_error"],
                "level": "INFO",
                "propagate": False
            }
        }
    } 
    logging.config.dictConfig(config)