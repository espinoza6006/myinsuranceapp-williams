# My Insurance app: add product for client

## The endpoint
This endpoint allows adding a product to an user.
- URI: "/api/v1/users/&lt;id>/products"
- Request:
  - Method: POST
  - Token required: {Authorization: Bearer [TOKEN]}
  - Body: {"id": [PRODUCT_ID]}
  - Request example: next request adding product 3 to user 2
  ```
  curl -X POST "localhost:5000/api/v1/users/2/products" -H "Content-Type: application/json"  -H "Authorization: Bearer [TOKEN]" -d "{\"id\":3}" -v
  ```
- Reponse:
  - Status code: 200
  - Body: [{PRODUCT}]

## Getting the token
- URI: /api/v1/token
- Request:
  - Method: POST
  - Body: {"email":"[email_value]","password":"[pass_value]"}
    - Request example: next request get a token for email:"jd@myinsuranceapp.com" and password: "passwordjd"
    ```
    curl -X POST localhost:5000/api/v1/token -H "Content-Type: application/json" -d "{\"email\":\"jd@myinsuranceapp.com\",\"password\":\"passwordjd\"}" -v
    ```
- Response:
  - Status code: 200
  - Body: {"token": [TOKEN],"user_id": [ID]}

## Models:
- User:
    ```
    id: INTEGER PRIMARY KEY AUTOINCREMENT,
    created: TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fullname: TEXT NOT NULL,
    email: TEXT NOT NULL,
    birthdate: TIMESTAMP ,
    country: TEXT ,
    city: TEXT ,
    address: TEXT, 
    password: TEXT
    ```
- Product:
    ```
    id: INTEGER PRIMARY KEY AUTOINCREMENT,
    created: TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name: TEXT ,
    description: TEXT,
    cost: float ,
    is_active: boolean
    ```

## Available data:
Currently in the database, once inited, there are
- Users: 2, ids: 1,2
- Products 4, ids: 1,2,3,4