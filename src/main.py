import logging
import sys

infoFileHandler = logging.FileHandler('./logs/info_logs.log')
infoFileHandler.setLevel(logging.INFO)

debugFileHandler = logging.FileHandler('./logs/debug_logs.log')
debugFileHandler.setLevel(logging.DEBUG)

stdoutHandler = logging.StreamHandler(sys.stdout)
stdoutHandler.setLevel(logging.INFO)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding='utf-8', level=logging.DEBUG,
    handlers=[infoFileHandler, debugFileHandler, stdoutHandler]
    )

try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    logging.info("dotenv module not found. If this is logged in a dockerized container, this is intended.")

import bot_main