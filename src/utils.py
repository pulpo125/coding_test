import logging
import time
from functools import wraps


# ==================================================
# Logger
# ==================================================

logger = logging.getLogger()

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# ==================================================
# Timer
# ==================================================

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Execution time of {func.__name__}(): {end - start:.4f} seconds")
        return result

    return wrapper