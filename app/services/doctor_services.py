from app.database.database import SessionLocal
from app.models.doctor_model import Doctor

def create_doctor(data):
    db = SessionLocal()
    doctor = Doctor(name=data.name, specialization=data.specialization)
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def get_all_doctors():
    db = SessionLocal()
    return db.query(Doctor).all()

def update_doctor(id, data):
    db = SessionLocal()
    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if doctor:
        doctor.name = data.name
        doctor.specialization = data.specialization
        db.commit()
    return doctor

def delete_doctor(id):
    db = SessionLocal()
    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if doctor:
        db.delete(doctor)
        db.commit()
    return {"message": "Deleted"}