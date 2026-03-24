from fastapi import APIRouter
from schemas.patients_schema import AppointmentCreate
from services.appointment_services import create_appointment, get_all_appointments, update_appointment, delete_appointment

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/")
def create(appointment: AppointmentCreate):
    return create_appointment(appointment)

@router.get("/")
def get_all():
    return get_all_appointments()

@router.put("/{id}")
def update(id: int, appointment: AppointmentCreate):
    return update_appointment(id, appointment)

@router.delete("/{id}")
def delete(id: int):
    return delete_appointment(id)