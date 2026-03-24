from fastapi import APIRouter
from schemas.patients_schema import DoctorCreate
from services.doctor_services import create_doctor, get_all_doctors, update_doctor, delete_doctor

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/")
def create(doctor: DoctorCreate):
    return create_doctor(doctor)

@router.get("/")
def get_all():
    return get_all_doctors()

@router.put("/{id}")
def update(id: int, doctor: DoctorCreate):
    return update_doctor(id, doctor)

@router.delete("/{id}")
def delete(id: int):
    return delete_doctor(id)