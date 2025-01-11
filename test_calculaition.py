import unittest
from calculations import *

class TestArthimeticOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,1),0)
    def test_subtract(self):
        self.assertEqual(subtract(1,2),-1)
        self.assertEqual(subtract(-1,1),-2)
    def test_multiply(self):
        self.assertEqual(multiply(10,5),50)
        self.assertEqual(multiply(-1,1),-1)
    def test_divide(self):
        self.assertEqual(divide(10,5),2)
        self.assertEqual(divide(-1,1),-1)
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)
class TestStasticalOperations(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1,2,3,4,5]),3)

    def test_median_odd(self):
        self.assertEqual(median([1,2,3,4,5]),3)
    def test_median_even(self):
        self.assertEqual(median([1,2,3,4]),2.5)
    def test_median_unsorted(self):
        self.assertEqual(median([5,3,1,2,4]),3)
    def test_mode_single(self):
        self.assertEqual(mode([1,2,2,3,4,4,4,5]),[4])
    def test_mode_multiple(self):
        self.assertEqual(mode([1,1,2,3,4,4,5,5]),[1,4,5])

# def make_suite():
#     arthimetic_suite=[
#         TestArthimeticOperations("test_add"),
#         TestArthimeticOperations("test_subtract"),
#         TestArthimeticOperations("test_multiply"),
#         TestArthimeticOperations("test_divide")
#     ]
#     return unittest.TestSuite(tests=arthimetic_suite)
# def make_suite():
#     arthimetic_suite=unittest.TestSuite()
#     arthimetic_suite.addTest(TestArthimeticOperations("test_add"))
#     arthimetic_suite.addTest(TestArthimeticOperations("test_subtract"))
#     arthimetic_suite.addTest(TestArthimeticOperations("test_multiply"))
#     arthimetic_suite.addTest(TestArthimeticOperations("test_divide"))
#     return arthimetic_suite
# def make_suite():
#     statistical_tests=[
#         TestStasticalOperations("test_mean"),
#         TestStasticalOperations("test_median_odd"),
#         TestStasticalOperations("test_median_even"),
#         TestStasticalOperations("test_median_unsorted"),
#         TestStasticalOperations("test_mode_single"),
#         TestStasticalOperations("test_mode_multiple")
#     ]
#     statistical_suite=unittest.TestSuite()
#     statistical_suite.addTests(statistical_tests)
#     return statistical_suite

def load_tests(loader,standar_tests,pattern):
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestArthimeticOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestStasticalOperations))
    return suite



if __name__ == '__main__':
    unittest.main()