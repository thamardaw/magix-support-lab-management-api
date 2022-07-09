from sqlalchemy import Column, String
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Test_Category(BaseMixin,Base):
    name = Column(String, nullable=False)