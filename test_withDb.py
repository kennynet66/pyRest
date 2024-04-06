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
    
    

if __name__ == "__main__":
    unittest.main()