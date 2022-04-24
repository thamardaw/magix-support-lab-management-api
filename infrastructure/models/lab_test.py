from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Lab_Test(BaseMixin,Base):
    name = Column(String, nullable=False)
    test_category_id = Column(Integer,ForeignKey("test_category.id"))
    test_category = relationship("Test_Category",backref="lab_test")
    