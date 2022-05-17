from typing import List
from typing import Protocol
from core.entity.lab_report import Lab_Report as Lab_ReportDTO
from core.entity.lab_result import Lab_Result as Lab_ResultDTO

class LabReportProtocol(Protocol):
    def persist(self,lab_report) -> Lab_ReportDTO:
        ...

    def update(self,id,lab_report) -> None:
        ...
    
    def list(self) -> List[Lab_ReportDTO]:
        ...
    
    def delete(self,id) -> None:
        ...
    
    def getById(self,id: int) -> Lab_ReportDTO:
        ...

    def persistLabResult(self,lab_result) -> Lab_ResultDTO:
        ...

    def updateLabResult(self,id,lab_result) -> None:
        ...

    def deleteLabResult(self,id) -> None:
        ...
        
