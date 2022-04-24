from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Parameter(BaseMixin,Base):
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    lab_test_id = Column(Integer,ForeignKey("lab_test.id"))
    lab_test = relationship("Lab_Test",backref="parameter")