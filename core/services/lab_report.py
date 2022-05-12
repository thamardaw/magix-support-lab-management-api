from core.protocol.lab_report import LabReportProtocol
from core.entity.lab_report import Lab_Report
from exceptions.http import BAD_REQUEST
from typing import List

class LabReportService:
    def __init__(self,lab_report_repo:LabReportProtocol)->None:
        self.lab_report_repo = lab_report_repo
    
    def getAllLabReport(self) -> List[Lab_Report]:
        return self.lab_report_repo.list()
    
    def getLabReport(self,id:int) -> Lab_Report:
        return self.lab_report_repo.getById(id)
    
    def createLabReport(self,lab_report) -> None:
        self.lab_report_repo.persist(lab_report)
        return 
    
    def updateLabReport(self,id:int,lab_report) -> None:
        self.lab_report_repo.update(id,lab_report)
        return
    
    def deleteLabReport(self,id:int) -> None:
        try:
            self.lab_report_repo.delete(id)
        except:
            raise BAD_REQUEST("Lab Report cannot be deleted.")
        return 

    def deleteMulitpleLabReport(self,ids) -> None:
        for id in ids:
            try:
                self.lab_report_repo.delete(id)
            except:
                raise BAD_REQUEST(f"Lab Report with id {id} cannot be deleted.")
        return 

    def addLabResult(self,lab_report_id,lab_result) -> None:
        lab_report_orm = self.lab_report_repo.getById(lab_report_id)
        lab_result = dict(lab_result,lab_report_id=lab_report_orm.id)
        self.lab_report_repo.persistLabResult(lab_result)
        return

    def removeLabResult(self,id) -> None:
        self.lab_report_repo.deleteLabResult(id)
        return

    def updateLabResult(self,id:int,lab_result) -> None:
        self.lab_report_repo.updateLabResult(id,lab_result)
        return