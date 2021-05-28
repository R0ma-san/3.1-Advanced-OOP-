import unittest
from advanced_oop import Rectangle, Triangle, Circle

class Test(unittest.TestCase):
    r1 = Rectangle(10, 10)
    t = Triangle(10, 10)
    c = Circle(10)

    

    
    def test_common_color(self):
        self.assertEqual(self.r1.show_color(), 'Black')
        self.assertEqual(self.t.show_color(), 'Black')
        self.assertEqual(self.c.show_color(), 'Black')
    
    r2 = Rectangle(10, 10, 'red')
    def test_new_color(self):
        self.assertEqual(self.r2.show_color(), 'red')



if __name__ == '__main__':
    unittest.main()
