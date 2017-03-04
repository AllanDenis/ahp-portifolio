import unittest
import distutils.spawn

class Api(unittest.TestCase):

    def test_tool(self):
        self.assertTrue(distutils.spawn.find_executable("pong") is not None)

if __name__ == '__main__':
    unittest.main()
