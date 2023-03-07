def arm(num):

 count = 0
 temp = num

 while temp > 0:
   count += 1
   temp //= 10

 sum = 0
 temp = num
 while temp > 0:
   digit = temp % 10
   power = 1
   for i in range(count):
      power *= digit
   sum += power
   temp //= 10

 if num == sum:
   return True
 else:
   return False
 

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = arm(371)
        expected = True
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = arm(1)
        expected = True
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = arm(45)
        expected = False
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = arm(123456789)
        expected = False
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)

