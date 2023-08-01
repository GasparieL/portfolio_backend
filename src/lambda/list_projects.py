import json
from service.project_service import ProjectService
 
def handler(event, context):
  project_service = ProjectService()
  projects = project_service.list_projects_by_type(event['queryStringParameters']['projectType'])
 
  return {
    "statusCode": 200,
    "headers": {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*"
    },
    "body": json.dumps(projects)
  }