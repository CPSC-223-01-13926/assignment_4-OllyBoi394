import unittest
import io
import sys
from unittest.mock import patch

import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

class Test01_weather_read_data_errorhandle(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 **** FUNCTION CALL: weather.read_data(filename='test74653.dat') *** EXPECT: {} ***
        """
        import weather
        remove_file('test74653.dat')
        r = weather.read_data(filename='test74653.dat')
        self.assertEqual({}, r)
        remove_file('test74653.dat')

        print()

class Test02_weather_write_data(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 **** FUNCTION CALL: weather.write_data(data={"20210203075501": {"t": 55, "h": 87, "r": 0}}, filename='test74653.dat') THEN weather.read_data(filename='test74653.dat') *** EXPECT: {"20210203075501": {"t": 55, "h": 87, "r": 0}} ***
        """
        import weather
        remove_file('test74653.dat')
        weather.write_data(data={"20210203075501": {"t": 55, "h": 87, "r": 0}}, filename='test74653.dat')
        r = weather.read_data(filename='test74653.dat')
        self.assertEqual({"20210203075501": {"t": 55, "h": 87, "r": 0}}, r)
        remove_file('test74653.dat')
        print()

class Test03_max_temperature(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 **** FUNCTION CALL: weather.max_temperature(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205') *** EXPECT: 74 ***
        """
        import weather
        r = weather.max_temperature(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
        self.assertEqual(74, r)
        print()

class Test04_min_temperature(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 **** FUNCTION CALL: weather.min_temperature(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205') *** EXPECT: 57 ***
        """
        import weather
        r = weather.min_temperature(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
        self.assertEqual(57, r)
        print()

class Test05_max_humidity(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 **** FUNCTION CALL: weather.max_humidity(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205') *** EXPECT: 68 ***
        """
        import weather
        r = weather.max_humidity(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
        self.assertEqual(68, r)
        print()

class Test06_min_humidity(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 **** FUNCTION CALL: weather.min_humidity(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205') *** EXPECT: 56 ***
        """
        import weather
        r = weather.min_humidity(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
        self.assertEqual(56, r)
        print()

class Test07_tot_rain(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 **** FUNCTION CALL: weather.tot_rain(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205') *** EXPECT: 0.36 ***
        """
        import weather
        r = weather.tot_rain(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
        self.assertEqual(0.36, r)
        print()

class Test08_report_daily(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 **** FUNCTION CALL: weather.report_daily(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205') *** EXPECT: <look in test.py Test08 variable = report> ***
        """
        import weather
        r = weather.report_daily(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
        report =          "========================= DAILY REPORT ========================\n"
        report = report + "Date                      Time  Temperature  Humidity  Rainfall\n"
        report = report + "====================  ========  ===========  ========  ========\n"
        report = report + "February 5, 2021      04:44:06           57        68      0.01\n"
        report = report + "February 5, 2021      08:33:07           65        63      0.05\n"
        report = report + "February 5, 2021      12:22:08           73        56      0.11\n"
        report = report + "February 5, 2021      16:11:09           74        60      0.19\n"
        self.assertEqual(report, r)
        print()

class Test09_report_historical(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test09 **** FUNCTION CALL: weather.report_historical(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}) *** EXPECT: <look in test.py Test09 variable = report> ***
        """
        import weather
        r = weather.report_historical(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}})
        report =          "============================== HISTORICAL REPORT ===========================\n"
        report = report + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
        report = report + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
        report = report + "====================  ===========  ===========  ========  ========  ========\n"
        report = report + "February 3, 2021               55           72        69        87      0.00\n"
        report = report + "February 5, 2021               57           74        56        68      0.36\n"
        self.maxDiff = None
        self.assertEqual(report, r)
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
