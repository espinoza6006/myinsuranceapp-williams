import json
import unittest
from urllib import response
from project import app 

class TestApp(unittest.TestCase):

    token=''
   
    def test_1_getToken(self): 
        tester = app.test_client(self)    
        user_data={"email":"jd@myinsuranceapp.com","password":"passwordjd"}
        response= tester.post('/api/v1/token',content_type='application/json', json = user_data)
        data=json.loads(response.text)
        print(f"post token: {data}")
        self.assertEqual(response.status_code, 200)

        if response.status_code==200:
            TestApp.token=data['token']



    def test_2_get_user_products_valid_token(self):
        tester = app.test_client(self)
        
       
        print(f"token: {self.token}")

        
        headers = {"Authorization": f"Bearer {TestApp.token}"}

        # send a GET request to the endpoint, indicating that json is expected as a response data and
        # adding the previous defined headers
        # take into account that the endpoint is: /api/v1/users/<id>/products
        # here we are replacing "<id>" by a concrete user id, that is the user with id="1"
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)

        # see previous function comments for this part
        data=json.loads(response.text)        
        print(f"get_user_products: {data}")
        self.assertEqual(response.status_code, 200)

        # here we verify that the length of the array data is greater than 0, since the user 1, has at least one product assigned
        self.assertTrue(len(data)>0)

    def test_3_get_user_products_invalid_token(self):
        tester = app.test_client(self)
        
        # this is a fake/invalid token, so it smust not work for accessing restricted area
        ivalid_fake_token='CfDJ8OW5OI0CPGJBgSNlGwO0x4YF7qbYKVv7KOO-N0eFtDUzXOrL7F9Xd9W1otVi4ueJOkAmAhuoHFWNkqRaFD7zvAMHMSKncl6Vo5QXKmpvy6vqxOKxSURdIey8aZPRi3Nnhp2p9la-Al5xrVKz0lignRdcCHf3O7pF9zv_sNx_c_T7pUe3WsxaJEPX3t_9FO2Wjw'

        headers = {"Authorization": f"Bearer {ivalid_fake_token}"}
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)
        data=json.loads(response.text)
        print(f"get_user_products: {data}")

        # we expect the response code to be some 4XX code, that means that the request is invalid
        # this is true, since we send a invalida token
        self.assertTrue(response.status_code > 400)



