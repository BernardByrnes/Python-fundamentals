import unittest
import main

class TestMain(unittest.TestCase):
  def test_do_stuff(self):
    test_param = 10
    result = main.do_stuff(test_param)
    self.assertEqual(result, 15)
    
class TestMain(unittest.TestCase):
  def test_do_stuff(self):
    test_param = "batman"
    result = main.do_stuff(test_param)
    self.assertEqual(result, ValueError)
    

unittest.main()