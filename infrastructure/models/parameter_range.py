from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Parameter_Range(BaseMixin,Base):
    name = Column(String, nullable=False)
    parameter_id = Column(Integer,ForeignKey("parameter.id"))
    parameter = relationship("Parameter",backref="parameter_range")
    upper_limit = Column(Integer)
    lower_limit = Column(Integer)