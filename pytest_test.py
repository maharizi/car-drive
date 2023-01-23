import pytest
import manage_log
from Car import Car


m = manage_log.Manage_log()


@pytest.fixture
def car():
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: init car class
            Return: Null"""
    return Car()


def test_init_fuel(car):
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: test init fuel variable
            Return: Null"""
    try:
        assert car.fuel == 30
        m.write_exceptions_to_log("TEST INIT FUEL --- PASS !")
    except Exception:
        m.write_exceptions_to_log("TEST INIT FUEL --- FAILED !")


@pytest.mark.one
def test_init_fuel_consumption(car):
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: test init fuel consumption variable
            Return: Null"""
    try:
        assert car.consumption_fuel == "1/10"
        m.write_exceptions_to_log("TEST INIT FUEL CONSUMPTION--- PASS !")
    except Exception:
        m.write_exceptions_to_log("TEST INIT FUEL CONSUMPTION--- FAILED !")


def test_init_money(car):
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: test init money variable
            Return: Null"""
    try:
        assert car.money == 500
        m.write_exceptions_to_log("TEST INIT MONEY--- PASS !")
    except Exception:
        m.write_exceptions_to_log("TEST INIT MONEY--- FAILED !")


def test_open_file(car):
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: test open file
            Return: Null"""
    try:
        assert car.open_file() == 1
        m.write_exceptions_to_log("TEST OPEN FILE --- PASS !")
    except Exception:
        m.write_exceptions_to_log("TEST OPEN FILE --- FAILED !")


def test_drive(car):
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: test drive function
            Return: Null"""
    try:
        assert car.start() == 1
        m.write_exceptions_to_log("TEST DRIVE --- PASS !")
    except Exception:
        m.write_exceptions_to_log("TEST DRIVE --- FAILED !")


def test_gear_update(car):
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: test gear update function
            Return: Null"""
    try:
        assert car.gear_update(20) == 1
        m.write_exceptions_to_log("TEST GEAR UPDATE --- PASS !")
    except Exception:
        m.write_exceptions_to_log("TEST GEAR UPDATE --- FAILED !")

    with pytest.raises(OverflowError):
        car.gear_update(200)


def test_fuel_charge(car):
    """Author: Maor Maharizi,
            Created: 22.01.2023,
            Detail: test fuel charge function
            Return: Null"""
    try:
        assert car.fuel_charge() == 1
        m.write_exceptions_to_log("TEST FUEL CHARGE --- PASS !")
    except Exception:
        m.write_exceptions_to_log("TEST FUEL CHARGE --- FAILED !")
