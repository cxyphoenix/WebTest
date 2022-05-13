import unittest

from demo06_unitest_testcase import TestCase01, TestCase02
#实例化TestSuite类
suite = unittest.TestSuite()

suite.addTest(TestCase01("testcase_01"))
# suite.addTest(TestCase01("testcase_02"))
# suite.addTest(TestCase02("testcase_02"))

suite.addTest(unittest.makeSuite(TestCase01))
suite.addTest(unittest.makeSuite(TestCase02))

runner = unittest.TextTestRunner()
runner.run(suite)
