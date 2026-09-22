from contextlib import contextmanager

from src.healthcare_agent.config import pool
from src.healthcare_agent.exceptions import QueryExecutionFailedException

# get the cursor
@contextmanager
def get_cursor():
    """contextmanager to safely borrow connection from pool and return back when done"""
    with pool.connection() as conn:
        with conn.cursor() as cur:
            yield cur

# DB method to execute a query
def execute_query(query: str, params: tuple = ()) -> bool:
    """
    Executes a query that modifies data (INSERT, UPDATE, DELETE).
    
    Arguments:
        sql: The SQL query to be executed containing placeholders.
        params: A Tuple containing data values to bind to the SQL query placeholders. Defaults to an empty tuple.
    
    Returns: True if query executes succesfully.
    """
    try:
        with get_cursor() as cur:
            cur.execute(query, params)
            return True
    except Exception as e:
        raise QueryExecutionFailedException(str(e))