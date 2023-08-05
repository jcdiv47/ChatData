import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
port = os.environ["MYSQL_PORT"]
db = os.environ["MYSQL_DB"]

DB_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
