from sqlalchemy import Column, String
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class Test_Category(BaseMixin,Base):
    name = Column(String, nullable=False)
    lab_tests = relationship("Lab_Test", backref="test_category", passive_deletes=True)