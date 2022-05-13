import unittest

def add(a, b):
    return a + b

class TestCase01(unittest.TestCase):
    def testcase_01(self):
        print("testcase_01")
        try:
            self.assertEqual(2, add(1, 3))
        except AssertionError as e:
            print("报错信息", e)
            raise

    def testcase_02(self):
        print("testcase_02")
        print("2 + 2 = ", add(2, 2))
        try:
            self.assertIn("124", "123456")
        except AssertionError as e:
            print(e)
            raise



if __name__ == "__main__":
    unittest.main()


