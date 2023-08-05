import logging
import sys
from pathlib import Path

__log_path = str(Path(__file__).parent.parent.parent / "run.log")


def _reset_logger(log: logging.Logger):
    for handler in log.handlers:
        handler.close()
        log.removeHandler(handler)
        del handler
    log.handlers.clear()
    log.propagate = False
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(
        logging.Formatter(
            "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d][%(funcName)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    file_handle = logging.FileHandler(__log_path, encoding="utf-8")
    file_handle.setFormatter(
        logging.Formatter(
            "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d][%(funcName)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    log.addHandler(file_handle)
    log.addHandler(console_handle)


def _get_logger():
    log = logging.getLogger("log")
    _reset_logger(log)
    log.setLevel(logging.DEBUG)
    return log


# log handler
logger = _get_logger()
