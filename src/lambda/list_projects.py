import json
 
def handler(event, context):
  projects = [
    {
      "title": "Title1",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "startDate": 'June 2021',
      "endDate": 'June 2023',
      "skills": [
        {
          "type": 'PROGRAMMING_LANGUAGE',
          "name": 'Python'
        },
        {
          "type": 'LIBRARY_OR_FRAMEWORK',
          "name": 'AWS',
        }
      ]
    },
    {
      "title": "Title2",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "startDate": 'June 2021',
      "endDate": 'June 2023',
      "skills": [
        {
          "type": 'PROGRAMMING_LANGUAGE',
          "name": 'Python'
        },
        {
          "type": 'LIBRARY_OR_FRAMEWORK',
          "name": 'AWS',
        }
      ]
    },
    {
      "title": "Title3",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "startDate": 'June 2021',
      "endDate": 'June 2023',
      "skills": [
        {
          "type": 'PROGRAMMING_LANGUAGE',
          "name": 'Python'
        },
        {
          "type": 'LIBRARY_OR_FRAMEWORK',
          "name": 'AWS',
        }
      ]
    },
    {
      "title": "Title4",
      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "startDate": 'June 2021',
      "endDate": 'June 2023',
      "skills": [
        {
          "type": 'PROGRAMMING_LANGUAGE',
          "name": 'Python'
        },
        {
          "type": 'LIBRARY_OR_FRAMEWORK',
          "name": 'AWS',
        }
      ]
    }
  ]
 
  return {
    "statusCode": 200,
    "headers": {
      "Content-Type": "application/json",
    },
    "body": json.dumps(projects)
  }