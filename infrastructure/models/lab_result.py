from ast import In
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Lab_Result(BaseMixin,Base):
    lab_report_id = Column(Integer,ForeignKey("lab_report.id",ondelete='CASCADE'),nullable=False)
    parameter_name = Column(String)
    parameter_id = Column(Integer,index=True)
    unit = Column(String)
    result = Column(Float)
    upper_limit = Column(Integer)
    lower_limit = Column(Integer)
    remark = Column(String)  