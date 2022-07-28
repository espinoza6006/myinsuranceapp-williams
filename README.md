# My Insurance App

## Install Dependencies
- pip3 install -r requirements.txt
  - If you have old version of project: 
    - pip3 uninstall -r requirements.txt

## Init database (before running the server)
- python3 project/init/init_db.py

## Run the server 
- python3 runserver.py
  - Access web at: http://localhost:5000/
  - Access API at: http://localhost:5000/[Endpoint]

## Authentication
- For web and API use this user/password:
  - Email: jd@myinsuranceapp.com
  - Password: passwordjd

## API endpoints
- Authenticate: http://localhost:5000/api/v1/token
  - Method POST
  - Payload {email:[email_value],password:[pass_value]}
  - All endpoints require token in header in this way:
    - 'Authorization: Bearer [TOKEN]'
- Endpoints:
  - Users: 
    - GET|POST [BASE_URL]/api/v1/users/
    - GET|DELETE|POST [BASE_URL]/api/v1/users/[id]
    - GET [BASE_URL]//api/v1/users/[id]/products
  - Products: 
    - GET|POST [BASE_URL]/api/v1/products/
    - GET|DELETE|POST [BASE_URL]/api/v1/products/[id]
  - *By default [BASE_URL] = http://localhost:5000
    

## Testing
- Unit tests:
  -  python3 -m unittest discover -s tests/unit -v
- Acceptance tests from inside:
  - python3 -m unittest discover -s tests/acceptance-flask -v
- Acceptance tests from outside:
  - python3 -m unittest discover -s tests/acceptance-request -v
    - For this is necessary that the service be running
- Load Tests:
  - k6 run sample-load-test.js
    - For this is necessary that the service be running

# myinsuranceapp-williams
