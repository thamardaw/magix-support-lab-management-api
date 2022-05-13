from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.lab_report import Lab_Report
from schemas.lab_result import Lab_Result
from core.services.lab_report import LabReportService
from core.entity.lab_report import Lab_Report as Lab_ReportDTO
from typing import List
from infrastructure.repository.lab_report import LabReportRepository

router = APIRouter(prefix="/lab_reports", tags=["Lab Reports"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[Lab_ReportDTO])
def get_all_lab_reports(repo=Depends(LabReportRepository)):
    return LabReportService(repo).getAllLabReport()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=Lab_ReportDTO)
def get_lab_report(id: int, repo=Depends(LabReportRepository)):
    return LabReportService(repo).getLabReport(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Lab_ReportDTO)
def create_lab_report(request: Lab_Report, repo=Depends(LabReportRepository)):
    return LabReportService(repo).createLabReport(request)

@router.post("/result/{lab_report_id}", status_code=status.HTTP_200_OK, response_model=Message)
def add_lab_result(lab_report_id: int,request: Lab_Result, repo=Depends(LabReportRepository)):
    LabReportService(repo).addLabResult(lab_report_id,request)
    return {"detail": "Lab result added."}

@router.delete("/result/{lab_result_id}",status_code=status.HTTP_200_OK, response_model=Message)
def remove_lab_result(lab_result_id: int, repo=Depends(LabReportRepository)):
    LabReportService(repo).removeLabResult(lab_result_id)
    return {"detail": "Lab result removed."}

@router.put("/result/{lab_result_id}",status_code=status.HTTP_200_OK, response_model=Message)
def update_lab_result(lab_result_id: int,request:Lab_Result, repo=Depends(LabReportRepository)):
    LabReportService(repo).updateLabResult(lab_result_id,request)
    return {"detail": "Lab result updated."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update_lab_report(id: int, request: Lab_Report,repo=Depends(LabReportRepository)):
    LabReportService(repo).updateLabReport(id,request)
    return {"detail": "Lab Report update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete_lab_report(id: int, repo=Depends(LabReportRepository)):
    LabReportService(repo).deleteLabReport(id)
    return {"detail": "Lab Report delete successful."}

@router.post("/bulk_delete",status_code=status.HTTP_200_OK, response_model=Message)
def delete_multiple_lab_reports(ids: List[int], repo=Depends(LabReportRepository)):
    LabReportService(repo).deleteMulitpleLabReport(ids)
    return {"detail": "Lab Reports delete successful."}
