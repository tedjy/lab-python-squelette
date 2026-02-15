import logging

def setup_logger(name: str = "mon_projet", level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  
    logger.setLevel(level.upper())

    handler = logging.StreamHandler()
    fmt = logging.Formatter("[%(asctime)s] %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(fmt)

    logger.addHandler(handler)
    return logger
