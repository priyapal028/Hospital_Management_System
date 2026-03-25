from app.database.database import SessionLocal
from app.models.patient_model import Patient

def create_patient(data):
    db = SessionLocal()
    patient = Patient(name=data.name, age=data.age)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def get_all_patients():
    db = SessionLocal()
    return db.query(Patient).all()

def update_patient(id, data):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == id).first()
    if patient:
        patient.name = data.name
        patient.age = data.age
        db.commit()
    return patient

def delete_patient(id):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == id).first()
    if patient:
        db.delete(patient)
        db.commit()
    return {"message": "Deleted"}