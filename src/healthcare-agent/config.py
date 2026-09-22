from dotenv import load_dotenv
import os
import sys
import atexit
import logging

from psycopg_pool import ConnectionPool
from psycopg.rows import dict_row

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# load the environment variables
load_dotenv()

MODEL = os.environ['MODEL']
MODEL_PROVIDER = os.environ['MODEL_PROVIDER']

# get all db configuration variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


if not all([DB_NAME, DB_PASSWORD, DB_USER]):
    raise Exception("ERROR: missing database configuration variables in environment.")
    sys.exit()

# construct a connection string 
# e.g. postgresql://[user]:[password]@[host]:[port]/[dbname]?sslmode=[mode]
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# intialize a connection pool globally
pool = ConnectionPool(
    conninfo=DATABASE_URL,
    min_size=2,
    max_size=10,
    # auto returns clean dict instead of tuples postgres (bydefault returns rows tuple)
    kwargs={"row_factory": dict_row}
)

# automatically close the connection pool when the interpreter shuts down
@atexit.register
def close_db_pool():
    logger.info("Closing shared db connection pool...")
    pool.close()