import unittest
from wsgiref import headers
from main import create_app
from config import TestConfig
from exts import db 


class APITestCase(unittest.TestCase):
    def setUp(self):
        """Setup Stage"""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client(self)
        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()

    def test_signup(self):
        """Test Signup"""
        signup_response = self.client.post(
            "/auth/signup",
            json = {
                "username":"testuser",
                "email":"testemail@gmail.com",
                "password":"Abcd@1234"
            }
        )
        status_code = signup_response.status_code
        self.assertEqual(status_code, 201)

    def test_login(self):
        """Test Login"""
        signup_response = self.client.post(
            "/auth/signup",
            json = {
                "username":"testuser",
                "email":"testemail@gmail.com",
                "password":"Abcd@1234"
            }
        )
        login_response = self.client.post(
            "/auth/login",
            json = {
                "username":"testuser",
                "password":"Abcd@1234"
            }
        )
        status_code = login_response.status_code
        self.assertEqual(status_code, 200)

    def test_get_all_notes(self):
        """Test get all notes"""
        response = self.client.get("/note/notes")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_get_one_note(self):
        id = 1
        response = self.client.get(f"/note/note/{id}")
        status_code = response.status_code
        self.assertEqual(status_code, 404)    
    
    def test_create_note(self):
        """Test create a note"""
        signup_response = self.client.post(
            "/auth/signup",
            json = {
                "username":"testuser",
                "email":"testemail@gmail.com",
                "password":"Abcd@1234"
            }
        )
        login_response = self.client.post(
            "/auth/login",
            json = {
                "username":"testuser",
                "password":"Abcd@1234"
            }
        )
        access_token = login_response.json["access_token"]
        create_note_response = self.client.post(
            "/note/notes",
            json = {
                "title": "Banh mi",
                "description": "An sang"
            },
            headers = {
                "Authorization":f"Bearer {access_token}"
            }
        )
        status_code = create_note_response.status_code
        print("Create new note: ",create_note_response.json)
        self.assertEqual(status_code, 201)

    def test_update_note(self):
        """Test update a note"""
        signup_response = self.client.post(
            "/auth/signup",
            json = {
                "username":"testuser",
                "email":"testemail@gmail.com",
                "password":"Abcd@1234"
            }
        )
        login_response = self.client.post(
            "/auth/login",
            json = {
                "username":"testuser",
                "password":"Abcd@1234"
            }
        )
        access_token = login_response.json["access_token"]
        create_note_response = self.client.post(
            "/note/notes",
            json = {
                "title": "Banh mi",
                "description": "An sang"
            },
            headers = {
                "Authorization":f"Bearer {access_token}"
            }
        )
        id = 1
        update_response = self.client.put(
            f"/note/note/{id}",
            json = {
                "title": "Pho xao",
                "description": "An trua"
            },
            headers = {
                "Authorization":f"Bearer {access_token}"
            }
        )
        print("Updated note: ", update_response.json)
        status_code = update_response.status_code
        self.assertEqual(status_code, 200)

    def test_delete_note(self):
        """Test delete a note"""
        signup_response = self.client.post(
            "/auth/signup",
            json = {
                "username":"testuser",
                "email":"testemail@gmail.com",
                "password":"Abcd@1234"
            }
        )
        login_response = self.client.post(
            "/auth/login",
            json = {
                "username":"testuser",
                "password":"Abcd@1234"
            }
        )
        access_token = login_response.json["access_token"]
        create_note_response = self.client.post(
            "/note/notes",
            json = {
                "title": "Banh mi",
                "description": "An sang"
            },
            headers = {
                "Authorization":f"Bearer {access_token}"
            }
        )
        id = 1
        delete_response = self.client.delete(
            f"/note/note/{id}",
            headers = {
                "Authorization":f"Bearer {access_token}"
            }
        )
        print("Deleted note: ", delete_response.json)
        status_code = delete_response.status_code
        self.assertEqual(status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__=="__main__":
    unittest.main()