import os
import logging

try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    logging.info("dotenv module not found. If this is logged in a dockerized container, this is intended.")

print(os.getenv("API_KEY"))
