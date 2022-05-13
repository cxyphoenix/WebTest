import unittest
discover = unittest.defaultTestLoader.discover("./case", pattern="*.py")

runner = unittest.TextTestRunner()
runner.run(discover)