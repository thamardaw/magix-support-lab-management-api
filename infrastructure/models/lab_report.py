from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship, foreign
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Lab_Report(BaseMixin,Base):
    patient_id = Column(Integer,nullable=False,index=True)
    patient = relationship('Patient', primaryjoin="Lab_Report.patient_id==foreign(Patient.id)",uselist=False)
    doctor_name = Column(String)
    sample_id = Column(Integer)
    sample_type = Column(String)
    patient_type = Column(String)
    test_date = Column(Date)
    lab_results = relationship("Lab_Result", backref="lab_report", passive_deletes=True)
    