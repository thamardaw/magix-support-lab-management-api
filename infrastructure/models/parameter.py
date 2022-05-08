from sqlalchemy import Column, String, Integer, JSON, Enum
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
import enum

class result_type_enum(str,enum.Enum):
    text = "text"
    number = "number"

class Parameter(BaseMixin,Base):
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    lab_test_id = Column(Integer,ForeignKey("lab_test.id",ondelete='CASCADE'))
    lab_test = relationship("Lab_Test",backref="parameter")
    result_type = Column(Enum(result_type_enum))
    result_default_text = Column(JSON)
    parameter_ranges = relationship("Parameter_Range", backref="parameter", passive_deletes=True)