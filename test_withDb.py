from withDb import Products
import unittest
import withDb

class TestDb(unittest.TestCase):
    
    products = {'123': 'Product1', "456":"Product2"}
    
    def test_abortifNotExists(self):
        
        productId = "789"
        
        with self.assertRaises(Exception) as context:
            withDb.abort_ifNotExists(productId)
            
        self.assertEqual(context.exception.code, 404)
        self.assertNotIn(productId, self.products)
    
    def test_continueIfExists(self):
        productId = "123"
        
        self.products[productId]
        with self.assertRaises(Exception):
            withDb.abort_ifNotExists(productId)
        
        self.assertEqual(1, 1)
        self.assertEqual(self.products[productId], "Product1")

class testProducts(unittest.TestCase):
    expected_products = {"123": "product1", "456":"product2"}
    
    def test_get(self):
        # Sample productId
        productId = "123"

        # Instantiate the products class
        products_instance = Products()
        
        # Setting the products to be the expected products
        withDb.products = self.expected_products
        
        # Call the get method
        result = products_instance.get()
        
        # Assertions
        self.assertEqual(result, self.expected_products)
        self.assertEqual(self.expected_products[productId], "product1")
        
    def test_put(self):
        # Instantiate the products class
        product_instance = Products()
        
        # Mock the generate Id function
        def mock_generateId():
            return "123"
        
        # Mock the args to be parsed in the request body
        def mock_parseArgs():
            return {"name": "Product1", "price": 10, "desc": "Description1"}
        
        # Assign the mocks
        withDb.generateId = mock_generateId
        withDb.createProductArgs.parse_args = mock_parseArgs
        
        # Call the put method
        response = product_instance.put()
        
        # Assertions
        self.assertEqual(response[0], {"success": "Product created successfully"})
        self.assertEqual(response[1], 200)
        

if __name__ == "__main__":
    unittest.main()