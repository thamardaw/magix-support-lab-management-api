from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.lab_report import Lab_Report
from infrastructure.models.lab_result import Lab_Result
from core.entity.lab_report import Lab_Report as Lab_ReportDTO
from core.entity.lab_result import Lab_Result as Lab_ResultDTO

class LabReportRepository(BaseRepo):
    def persist(self,lab_report) -> Lab_ReportDTO:
        new_lab_report = Lab_Report(**lab_report.dict())
        new_lab_report = self.create(new_lab_report)
        return Lab_ReportDTO.from_orm(new_lab_report)
    
    def update(self,id,lab_report) -> None:
        lab_report_orm = self.read(Lab_Report,id)
        if type(lab_report) is dict:
            super().update(lab_report_orm,lab_report)
        else:
            super().update(lab_report_orm,lab_report.dict())
        return

    def list(self) -> List[Lab_ReportDTO]:
        lab_reports = self.read_all(Lab_Report)
        return [Lab_ReportDTO.from_orm(lab_report) for lab_report in lab_reports]
    
    def delete(self,id) -> None:
        self.read(Lab_Report,id)
        super().delete(Lab_Report,id)
        return 
        
    def getById(self,id: int) -> Lab_ReportDTO:
        lab_report_orm = self.read(Lab_Report,id)
        return Lab_ReportDTO.from_orm(lab_report_orm)

    def persistLabResult(self,lab_result) -> Lab_ResultDTO:
        if type(lab_result) is dict:
            new_lab_result = Lab_Result(**lab_result)
        else:
            new_lab_result = Lab_Result(**lab_result.dict())
        new_lab_result = self.create(new_lab_result)
        return Lab_ResultDTO.from_orm(new_lab_result)

    def updateLabResult(self,id,lab_result) -> None:
        lab_result_orm = self.read(Lab_Result,id)
        if type(lab_result) is dict:
            super().update(lab_result_orm,lab_result)
        else:
            super().update(lab_result_orm,lab_result.dict())
        return

    def deleteLabResult(self,id) -> None:
        self.read(Lab_Result,id)
        super().delete(Lab_Result,id)
        return 
