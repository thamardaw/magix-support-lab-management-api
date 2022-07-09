from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class Lab_Result(BaseMixin,Base):
    lab_report_id = Column(Integer,ForeignKey("lab_report.id",ondelete='CASCADE'),nullable=False)
    parameter_name = Column(String)
    test_name = Column(String)
    test_id = Column(Integer,index=True)
    test = relationship('Lab_Test', primaryjoin="Lab_Result.test_id==foreign(Lab_Test.id)",uselist=False)
    parameter_id = Column(Integer,index=True)
    unit = Column(String)
    result = Column(String)
    upper_limit = Column(Float)
    lower_limit = Column(Float)
    remark = Column(String)  