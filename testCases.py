import unittest
import json
from api import app 

class TestSupplierAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_suppliers(self):
        response = self.app.get('/suppliers')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list) 

    def test_add_supplier(self):
        new_supplier_data = {'name': 'Test Supplier', 'location': 'Test Location'}
        response = self.app.post('/suppliers', json=new_supplier_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('supplier_id', data)
      
    def test_update_supplier(self):
    
        supplier_id = 'valid_supplier_id'
        updated_data = {'name': 'Updated Supplier Name'}
        response = self.app.put(f'/suppliers/{supplier_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('message', data)
       

    def test_delete_supplier(self):
       
        supplier_id = 'valid_supplier_id'
        response = self.app.delete(f'/suppliers/{supplier_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('message', data)
       

    def test_search_suppliers(self):
        search_data = {'search_by': 'name', 'search_txt': 'Test'}
        response = self.app.post('/suppliers/search', json=search_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list) 

if __name__ == '__main__':
    unittest.main()
