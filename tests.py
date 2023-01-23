import unittest
import manage_log
from Car import Car


class MyTestCaseUnittest(unittest.TestCase):
    c = None
    m = manage_log.Manage_log()

    def setUp(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: init car class
                Return: Null"""
        self.c = Car()

    def test_init_fuel(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: test init fuel variable
                Return: Null"""
        try:
            self.assertEqual(self.c.fuel, 30)
            self.m.write_exceptions_to_log("TEST INIT FUEL --- PASS !")
        except Exception as e:
            self.m.write_exceptions_to_log("TEST INIT FUEL --- FAILED !")

    def test_init_fuel_consumption(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: test init fuel consumption variable
                Return: Null"""
        try:
            self.assertEqual(self.c.consumption_fuel, "1/10")
            self.m.write_exceptions_to_log("TEST INIT FUEL CONSUMPTION --- PASS !")
        except Exception as e:
            self.m.write_exceptions_to_log("TEST INIT FUEL CONSUMPTION --- FAILED !")

    def test_init_money(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: test init money variable
                Return: Null"""
        try:
            self.assertEqual(self.c.money, 500)
            self.m.write_exceptions_to_log("TEST INIT MONEY --- PASS !")
        except Exception as e:
            self.m.write_exceptions_to_log("TEST INIT MONEY --- FAILED !")

    def test_open_file(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: test open file
                Return: Null"""
        try:
            self.assertEqual(self.m.open_file(), 1)
            self.m.write_exceptions_to_log("TEST OPEN FILE --- PASS !")
        except Exception as e:
            self.m.write_exceptions_to_log("TEST OPEN FILE --- FAILED !")

    def test_drive(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: test drive function
                Return: Null"""
        try:
            self.assertEqual(self.c.start(), 1)
            self.m.write_exceptions_to_log("TEST DRIVE --- PASS !")
        except Exception as e:
            self.m.write_exceptions_to_log("TEST DRIVE --- FAILED !")

    def test_gear_update(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: test gear update function
                Return: Null"""
        try:
            self.assertEqual(self.c.gear_update(20), 1)
            self.m.write_exceptions_to_log("TEST GEAR UPDATE --- PASS !")
        except Exception as e:
            self.m.write_exceptions_to_log("TEST GEAR UPDATE --- FAILED !")

    def test_fuel_charge(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: test fuel charge function
                Return: Null"""
        try:
            self.assertEqual(self.c.fuel_charge(), 1)
            self.m.write_exceptions_to_log("TEST FUEL CHARGE --- PASS !")
        except Exception as e:
            self.m.write_exceptions_to_log("TEST FUEL CHARGE --- FAILED !")
