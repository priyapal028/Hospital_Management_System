from fastapi import APIRouter
from schemas.patients_schema import PatientCreate
from services.patient_services import create_patient, get_all_patients, update_patient, delete_patient

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/")
def create(patient: PatientCreate):
    return create_patient(patient)

@router.get("/")
def get_all():
    return get_all_patients()

@router.put("/{id}")
def update(id: int, patient: PatientCreate):
    return update_patient(id, patient)

@router.delete("/{id}")
def delete(id: int):
    return delete_patient(id)