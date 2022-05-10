from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.test_category import Test_Category
from infrastructure.models.lab_test import Lab_Test
from infrastructure.models.parameter import Parameter
from infrastructure.models.parameter_range import Parameter_Range
from core.entity.test_category import Test_Category as Test_CategoryDTO
from core.entity.lab_test import Lab_Test as Lab_TestDTO
from core.entity.parameter import Parameter as ParameterDTO
from core.entity.parameter_range import Parameter_Range as Parameter_RangeDTO
from exceptions.repo import SQLALCHEMY_ERROR
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

class TestCategoryRepository(BaseRepo):
    def persist(self,test_category) -> Test_CategoryDTO:
        new_test_category = Test_Category(**test_category.dict())
        new_test_category = self.create(new_test_category)
        return Test_CategoryDTO.from_orm(new_test_category)
    
    def update(self,id,test_category) -> None:
        test_category_orm = self.read(Test_Category,id)
        if type(test_category) is dict:
            super().update(test_category_orm,test_category)
        else:
            super().update(test_category_orm,test_category.dict())
        return

    def list(self) -> List[Test_CategoryDTO]:
        test_categorys = self.read_all(Test_Category)
        return [Test_CategoryDTO.from_orm(test_category) for test_category in test_categorys]
    
    def delete(self,id) -> None:
        self.read(Test_Category,id)
        super().delete(Test_Category,id)
        return 
        
    def getById(self,id: int) -> Test_CategoryDTO:
        test_category_orm = self.read(Test_Category,id)
        return Test_CategoryDTO.from_orm(test_category_orm)

    def persistLabTest(self,lab_test) -> Lab_TestDTO:
        new_lab_test = Lab_Test(**lab_test.dict())
        new_lab_test = self.create(new_lab_test)
        return Lab_TestDTO.from_orm(new_lab_test)

    def updateLabTest(self,id,lab_test) -> None:
        lab_test_orm = self.read(Lab_Test,id)
        if type(lab_test) is dict:
            super().update(lab_test_orm,lab_test)
        else:
            super().update(lab_test_orm,lab_test.dict())
        return

    def listLabTest(self) -> List[Lab_TestDTO]:
        lab_tests = self.read_all(Lab_Test)
        return [Lab_TestDTO.from_orm(lab_test) for lab_test in lab_tests]

    def listLabTestOpTestCategoryId(self,test_category_id: int) -> List[Lab_TestDTO]:
        try:
            lab_tests = self._db.query(Lab_Test).filter(or_(test_category_id == None,Lab_Test.test_category_id == test_category_id))\
                .order_by(Lab_Test.id.desc()).all()
            return [Lab_TestDTO.from_orm(lab_test) for lab_test in lab_tests]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def deleteLabTest(self,id) -> None:
        self.read(Lab_Test,id)
        super().delete(Lab_Test,id)
        return 

    def getLabTestById(self,id: int) -> Lab_TestDTO:
        lab_test_orm = self.read(Lab_Test,id)
        return Lab_TestDTO.from_orm(lab_test_orm)

    def persistParameter(self,parameter) -> ParameterDTO:
        if type(parameter) is dict:
            new_parameter = Parameter(**parameter)
        else:
            new_parameter = Parameter(**parameter.dict())
        new_parameter = self.create(new_parameter)
        return ParameterDTO.from_orm(new_parameter)

    def updateParameter(self,id,parameter) -> None:
        parameter_orm = self.read(Parameter,id)
        if type(parameter) is dict:
            super().update(parameter_orm,parameter)
        else:
            super().update(parameter_orm,parameter.dict())
        return

    def listParameter(self) -> List[ParameterDTO]:
        parameters = self.read_all(Parameter)
        return [ParameterDTO.from_orm(parameter) for parameter in parameters]

    def listParameterByLabTestId(self,lab_test_id: int) -> List[ParameterDTO]:
        try:
            parameters = self._db.query(Parameter).filter(or_(lab_test_id == None,Parameter.lab_test_id == lab_test_id))\
                .order_by(Parameter.id.desc()).all()
            return [ParameterDTO.from_orm(parameter) for parameter in parameters]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def deleteParameter(self,id) -> None:
        self.read(Parameter,id)
        super().delete(Parameter,id)
        return

    def getParameterById(self,id: int) -> ParameterDTO:
        parameter_orm = self.read(Parameter,id)
        return ParameterDTO.from_orm(parameter_orm)

    def persistParameterRange(self,parameter_range) -> Parameter_RangeDTO:
        if type(parameter_range) is dict:
            new_parameter_range = Parameter_Range(**parameter_range)
        else:
            new_parameter_range = Parameter_Range(**parameter_range.dict())
        new_parameter_range = self.create(new_parameter_range)
        return Parameter_RangeDTO.from_orm(new_parameter_range)

    def updateParameterRange(self,id,parameter_range) -> None:
        parameter_range_orm = self.read(Parameter_Range,id)
        if type(parameter_range) is dict:
            super().update(parameter_range_orm,parameter_range)
        else:
            super().update(parameter_range_orm,parameter_range.dict())
        return

    def listParameterRange(self) -> List[Parameter_RangeDTO]:
        parameter_ranges = self.read_all(Parameter_Range)
        return [Parameter_RangeDTO.from_orm(parameter_range) for parameter_range in parameter_ranges]

    def listParameterRangeByParameterId(self,parameter_id: int) -> List[Parameter_RangeDTO]:
        try:
            parameter_ranges = self._db.query(Parameter_Range).filter(or_(parameter_id == None,Parameter_Range.parameter_id == parameter_id))\
                .order_by(Parameter_Range.id.desc()).all()
            return [Parameter_RangeDTO.from_orm(parameter_range) for parameter_range in parameter_ranges]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def deleteParameterRange(self,id) -> None:
        self.read(Parameter_Range,id)
        super().delete(Parameter_Range,id)
        return

    def getParameterRangeById(self,id: int) -> Parameter_RangeDTO:
        parameter_range_orm = self.read(Parameter_Range,id)
        return Parameter_RangeDTO.from_orm(parameter_range_orm)