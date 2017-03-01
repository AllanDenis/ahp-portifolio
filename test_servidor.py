import unittest
import distutils.spawn

class Dependencias(unittest.TestCase):

  def test_tool(self):
      self.assertTrue(distutils.spawn.find_executable("apache"))

if __name__ == '__main__':
    unittest.main()
