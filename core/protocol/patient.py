from typing import List
from typing import Protocol
from core.entity.patient import Patient as PatientDTO

class PatientProtocol(Protocol):
    def persist(self,patient) -> PatientDTO:
        ...

    def update(self,id,patient) -> None:
        ...
    
    def list(self) -> List[PatientDTO]:
        ...
    
    def delete(self,id) -> None:
        ...
    
    def getById(self,id: int) -> PatientDTO:
        ...
