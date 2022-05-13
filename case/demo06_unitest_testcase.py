import unittest

def add(a, b):
    return a + b

class TestCase01(unittest.TestCase):
    #子每条用例执行前执行一次
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    # 方法名必须以test开头
    def testcase_01(self):
        print("testcase_01")
        print("1 + 1 = ", add(1, 1))
        self.assertEqual(2, add(1,1))
    def testcase_02(self):
        print("testcase_02")
        self.assertEqual(3, add(1, 2))

    def testcase_03(self):
        print("testcase_03")
        print("3 + 3 = ", add(3, 3))


class TestCase02(unittest.TestCase):
    # 方法名必须以test开头
    def testcase_01(self):
        print("TestCase_01")

    def testcase_01(self):
        print("TestCase_02")

    def testcase_03(self):
        print("TestCase_03")


if __name__ == "__main__":
    unittest.main()
