from pydantic import BaseModel, Field
from datetime import date, time


class Appointment(BaseModel):
    """Structured schema for a verified medical appointment record."""
    id: int = Field(
        description="The unique database primary key for the appointment")
    patient_id: str = Field(description="The validated uppercase patient ID")
    doctor: str = Field(description="The physician's name")
    appointment_date: date = Field(
        description="The scheduled date of the visit")
    appointment_time: time = Field(description="The scheduled time slot")
    appointment_type: str = Field(
        description="The category of medical visit (e.g., Checkup)")
