from src.healthcare_agent.config import pool
from src.healthcare_agent.config import logger
from src.healthcare_agent.database import get_cursor
from src.healthcare_agent.data.appointments import fetch_patient_appointments

def test_db_connection():
    logger.info("Connecting to PostgreSQL...")
    try:
        fetch_patient_appointments('PAT-001')
        # with get_cursor() as cursor:
            # cursor.execute("SELECT version();") 
            # version_result = cursor.fetchone()
            # logger.info(f"DB VERSION ==> {version_result}\n")
    except Exception as e:
        logger.error(f"DB connection failed {e}")


if __name__ == "__main__":
    test_db_connection()