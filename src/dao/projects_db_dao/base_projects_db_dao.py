from abc import ABC, abstractmethod
from typing import List
from enum import Enum

class ProjectType(str, Enum):
    PERSONAL = 'PERSONAL'
    INDUSTRY = 'INDUSTRY'
    ACADEMIC = 'ACADEMIC'
    OPEN_SOURCE = 'OPEN_SOURCE'
    OTHER = 'OTHER'


class ProjectsDBDao(ABC):
    @abstractmethod
    def list_projects_by_type(self, project_type: ProjectType) -> List[dict]:
        pass
    
    @abstractmethod
    def get_project(self, project_type: ProjectType, name: str) -> dict:
        pass

