from dao.projects_db_dao.ddb_projects_db_dao import DDBProjectsDBDao 
from dao.projects_db_dao.base_projects_db_dao import ProjectsDBDao 


class ProjectService():
    
        def __init__(self, projects_db_dao: ProjectsDBDao = DDBProjectsDBDao()):
            self.projects_db_dao = projects_db_dao
    
        def list_projects_by_type(self, project_type):
            return self.projects_db_dao.list_projects_by_type(project_type)

        def get_project(self, project_type, name):
            pass
              
        