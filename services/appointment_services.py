from database.database import SessionLocal
from models.appointment_model import Appointment

def create_appointment(data):
    db = SessionLocal()
    appointment = Appointment(patient_id=data.patient_id, doctor_id=data.doctor_id, date=data.date)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def get_all_appointments():
    db = SessionLocal()
    return db.query(Appointment).all()

def update_appointment(id, data):
    db = SessionLocal()
    appointment = db.query(Appointment).filter(Appointment.id == id).first()
    if appointment:
        appointment.patient_id = data.patient_id
        appointment.doctor_id = data.doctor_id
        appointment.date = data.date
        db.commit()
    return appointment

def delete_appointment(id):
    db = SessionLocal()
    appointment = db.query(Appointment).filter(Appointment.id == id).first()
    if appointment:
        db.delete(appointment)
        db.commit()
    return {"message": "Deleted"}