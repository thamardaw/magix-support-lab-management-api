from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Lab_Test(BaseMixin,Base):
    name = Column(String, nullable=False)
    test_category_id = Column(Integer,index=True)
    test_category_ =  relationship('Test_Category', primaryjoin="Lab_Test.test_category_id==foreign(Test_Category.id)",uselist=False)
    test_category_name = Column(String)
    parameters = relationship("Parameter", backref="lab_test", passive_deletes=True)
    