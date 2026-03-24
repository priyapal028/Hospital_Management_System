from pydantic import BaseModel

# Patient
class PatientCreate(BaseModel):
    name: str
    age: int
    disease: str

class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    disease: str

    class confid:
        from_attribute = True

# Doctor
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    

class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str

# Appointment
class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date: str

class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: str