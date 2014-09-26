from django.test import TestCase, Client
from logincounter.models import User
import json

class TestUsers(TestCase):
    def setUp(self):
    	self.client = Client()
        self.user1 = User.objects.create(user="user1", password="password")
        self.user2 = User.objects.create(user="user2", password="password")   
        
    def testDefault(self):
        self.assertEquals(self.user1.login_count, 1)
        self.assertEquals(self.user2.login_count, 1)
		
    def testLogin(self):
    	response = self.client.post('/users/login/', data = json.dumps({'user': self.user1.user, 'password': self.user1.password}), content_type="application/json")
    	print response.content
    	self.assertEquals(200, response.status_code)
		
	
