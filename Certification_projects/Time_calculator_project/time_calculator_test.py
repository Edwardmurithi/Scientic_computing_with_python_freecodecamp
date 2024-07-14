#!/usr/bin/python3
import unittest
from time_calculator import add_time

class TestTimeCalculator(unittest.TestCase):
    
    def test_add_time(self):
        # test time when following time is provided
        self.assertAlmostEqual(add_time('3:00 PM', '3:10'), '6:10 PM')
        self.assertAlmostEqual(add_time('11:30 AM', '2:32', 'Monday'), '2:02 PM, Monday')
        self.assertAlmostEqual(add_time('11:43 AM', '00:20'), '12:03 PM')
        self.assertAlmostEqual(add_time('10:10 PM', '3:30'), '1:40 AM (next day)')
        self.assertAlmostEqual(add_time('11:43 PM', '24:20', 'tueSday'), '12:03 AM, Thursday (2 days later)')
        self.assertAlmostEqual(add_time('6:30 PM', '205:12'), '7:42 AM (9 days later)')


unittest.main()
