
from fastapi import FastAPI
from database.database import Base, engine

from database.routes.patient_routes import router as patient_router
from database.routes.doctor_routes import router as doctor_router
from database.routes.appointment_routes import router as appointment_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)