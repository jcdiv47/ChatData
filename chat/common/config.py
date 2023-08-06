import os
from chat.common.log import logger

try:
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
except KeyError:
    logger.info("OPENAI_API_KEY is not set up in environment variables")
    OPENAI_API_KEY = None

try:
    user = os.environ["MYSQL_USER"]
    password = os.environ["MYSQL_PASSWORD"]
    host = os.environ["MYSQL_HOST"]
    port = os.environ["MYSQL_PORT"]
    db = os.environ["MYSQL_DB"]
    DB_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
except KeyError:
    pass
