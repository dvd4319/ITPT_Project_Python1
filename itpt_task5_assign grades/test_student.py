import unittest
from Student import Student 

class TestStudent(unittest.TestCase):

    def test_Student(self):
        student1 = Student(100,'Madonna','Ciccone', 75)
        student2 = Student(100,'Maria','Asaftei', 35)
        init1 = student1.initials()
        init2 = student2.initials()
        percent1 = student1.percent()
        percent2 = student2.percent()
        Mark1 =student1.mark1(75)
        Mark2 = student2.mark1(75)
        self.assertTrue(Mark1, 100)




if __name__ == '__main__':
    unittest.main()