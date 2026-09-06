{
  "info": {
    "_postman_id": "1386514f-b6dc-486d-a1a2-7efefcdb4b8f",
    "name": "divar-project",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    "_exporter_id": "42911537"
  },
  "item": [
    {
      "name": "user registration",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"username\":\"amirhosein2424\",\n    \"email\":\"amirhosein.hydri1382212@gmail.com\",\n    \"password\":\"amirhosein13\",\n    \"phone_number\":\"09966935704\"\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "localhost:8000/api/user/signup/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "user",
            "signup",
            ""
          ]
        }
      },
      "response": []
    },
    {
      "name": "user login",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"username\":\"amirhosein2\",\n    \"password\":\"amirhosein13\"\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "localhost:8000/api/user/login/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "user",
            "login",
            ""
          ]
        }
      },
      "response": []
    },
    {
      "name": "list and create category",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4NzA1MTYyLCJpYXQiOjE3ODg2OTc5NjIsImp0aSI6IjNkZDVmMGY4ODA4ODQ2ZTU4OThkNWRjYTQ5NjRkNDM0IiwidXNlcl9pZCI6IjYifQ.G3rnOs-WtsVQLWfqPCUxPYUZdt8ZXMe1O1LvmXR78kw",
            "type": "text"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"name\":\"job\",\n    \"slug\":\"job-123\"\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "localhost:8000/api/category/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "category",
            ""
          ]
        }
      },
      "response": []
    },
    {
      "name": "get and update category",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "method": "GET",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4NzA1MTYyLCJpYXQiOjE3ODg2OTc5NjIsImp0aSI6IjNkZDVmMGY4ODA4ODQ2ZTU4OThkNWRjYTQ5NjRkNDM0IiwidXNlcl9pZCI6IjYifQ.G3rnOs-WtsVQLWfqPCUxPYUZdt8ZXMe1O1LvmXR78kw",
            "type": "text"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"name\":\"it-job\"\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "localhost:8000/api/category/1/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "category",
            "1",
            ""
          ]
        }
      },
      "response": []
    },
    {
      "name": "delete and retrieve category",
      "request": {
        "method": "DELETE",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4NzA1MTYyLCJpYXQiOjE3ODg2OTc5NjIsImp0aSI6IjNkZDVmMGY4ODA4ODQ2ZTU4OThkNWRjYTQ5NjRkNDM0IiwidXNlcl9pZCI6IjYifQ.G3rnOs-WtsVQLWfqPCUxPYUZdt8ZXMe1O1LvmXR78kw",
            "type": "text"
          }
        ],
        "url": {
          "raw": "localhost:8000/api/category/1/delete/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "category",
            "1",
            "delete",
            ""
          ]
        }
      },
      "response": []
    },
    {
      "name": "create and list listings",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4NzA1MTYyLCJpYXQiOjE3ODg2OTc5NjIsImp0aSI6IjNkZDVmMGY4ODA4ODQ2ZTU4OThkNWRjYTQ5NjRkNDM0IiwidXNlcl9pZCI6IjYifQ.G3rnOs-WtsVQLWfqPCUxPYUZdt8ZXMe1O1LvmXR78kw",
            "type": "text"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"title\":\"book\",\n    \"description\":\"sifi book for teens\",\n    \"price\":18,\n    \"location\":\"tehran, tajrish\",\n    \"category\":2\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "localhost:8000/api/list/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "list",
            ""
          ]
        }
      },
      "response": []
    },
    {
      "name": "list and update and get listings",
      "request": {
        "method": "GET",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4NzA1MTYyLCJpYXQiOjE3ODg2OTc5NjIsImp0aSI6IjNkZDVmMGY4ODA4ODQ2ZTU4OThkNWRjYTQ5NjRkNDM0IiwidXNlcl9pZCI6IjYifQ.G3rnOs-WtsVQLWfqPCUxPYUZdt8ZXMe1O1LvmXR78kw",
            "type": "text"
          }
        ],
        "url": {
          "raw": "localhost:8000/api/list/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "list",
            ""
          ]
        }
      },
      "response": []
    },
    {
      "name": "delete and update listings",
      "request": {
        "method": "DELETE",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4NzA1MTYyLCJpYXQiOjE3ODg2OTc5NjIsImp0aSI6IjNkZDVmMGY4ODA4ODQ2ZTU4OThkNWRjYTQ5NjRkNDM0IiwidXNlcl9pZCI6IjYifQ.G3rnOs-WtsVQLWfqPCUxPYUZdt8ZXMe1O1LvmXR78kw",
            "type": "text"
          }
        ],
        "url": {
          "raw": "localhost:8000/api/list/1/delete/",
          "host": [
            "localhost"
          ],
          "port": "8000",
          "path": [
            "api",
            "list",
            "1",
            "delete",
            ""
          ]
        }
      },
      "response": []
    }
  ]
}