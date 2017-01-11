import unittest 

from app import app
from flask_testing import TestCase


class MyViewTestCase(TestCase):
    def create_app(self):
        return app

    def test_get_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_index_template(self):
    	self.client.get('/')
    	self.assert_template_used('index.html')

if __name__ == '__main__':
    unittest.main()