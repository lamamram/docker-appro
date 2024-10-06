import unittest
from bank.client import Client

class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.client = Client(1)
    
    def testFullName(self):
        self.assertEqual("Michel LEFEBVRE", self.client.get_full_name())

    
if __name__ == "__main__":
    unittest.main()