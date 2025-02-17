import time

from hubspot.crm.contacts.exceptions import ApiException
from config.logger import logger
from config.settings import RATE_LIMIT_MAX_RETRIES, RATE_LIMIT_BASE_WAIT

def retry_on_rate_limit(func):
    def wrapper(*args, **kwargs):
        for attempt in range(RATE_LIMIT_MAX_RETRIES):
            try:
                return func(*args, **kwargs)
            except ApiException as e:
                if e.status == 429:
                    wait_time = RATE_LIMIT_BASE_WAIT * (2 ** attempt)
                    logger.warning(f"Rate limit reached. Retrying in {wait_time:.2f} seconds... (Attempt {attempt + 1}/{RATE_LIMIT_MAX_RETRIES})")
                    time.sleep(wait_time)
                else:
                    logger.error(f"API Exception: {e}")
                    return {"error": str(e)}
        return {"error": "Max retries reached. Failed to process request."}
    return wrapper
