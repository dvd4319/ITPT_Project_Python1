import unittest
from athletes import athletes  

class TestAthletes(unittest.TestCase):

    def test_selection(self):
        athlet1 = athletes('Madonna','Ciccone', 45,48)
        athlet2 = athletes('Rodica','Mandache', 56, 71)
        athlet1.selection()
        athlet2.selection()



if __name__ == '__main__':
    unittest.main()