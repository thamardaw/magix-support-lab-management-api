from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Parameter_Range(BaseMixin,Base):
    parameter_id = Column(Integer,ForeignKey("parameter.id",ondelete='CASCADE'))
    parameter_ = relationship("Parameter",backref="parameter_range")
    upper_limit = Column(Integer)
    lower_limit = Column(Integer)
    low_remark = Column(String)
    high_remark = Column(String)
    normal_remark = Column(String)