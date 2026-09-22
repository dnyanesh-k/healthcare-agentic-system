from typing import Optional

from src.healthcare_agent.database import fetch_one, fetch_all
from src.healthcare_agent.config import logger
from src.healthcare_agent.models import Appointment

def fetch_patient_appointments(patient_id: str) -> list[dict]:
    """Queries database for all scheduled appointments of a specific patient.
    
    Arguments: 
        patient_id: unique identifier of a specific patient.
    
    Returns:
        A list of dictionaries containing apoointment rows, ordered by scheduled date and time.
        Returns an empty list if no records found.
    """
    sql = """
        SELECT id, doctor, appointment_date, appointment_time, appointment_type FROM appointments WHERE patient_id = %s ORDER BY appointment_date ASC, appointment_time ASC;
    """
    # clean the patient id remove leading and trailing spaces and change case to upper
    patient_id = patient_id.strip().upper()

    records = fetch_all(sql, (patient_id,))

    if not records:
        logger.info(f"System Record: No appointments found for Patient {patient_id}.")
        return []
    # print(records)
    for r in records:
        print(f"{r['id']}--> {r['doctor']}--> {r['appointment_type']}")
    return records

def book_appointment(doctor: str, date: str, time: str, appt_type: str) -> Optional[Appointment]:
    pass
