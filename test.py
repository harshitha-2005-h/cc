import unittest
from app import add

class TestApp(unitest.TestCase):
    def Test_add(self):
        self.asserEqual(add(2,3),5)
        self.asserEqual(add(1,2),3)
        self.asserEqual(add(3,4),7)
        self.asserEqual(add(4,5),9)
        self.asserEqual(add(5,6),11)

if __name__ == '__main__':
    unittest.main()
