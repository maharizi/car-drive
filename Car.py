import os
from dotenv import load_dotenv

import manage_log


class Car:
    load_dotenv()
    fuel = None
    consumption_fuel = None
    money = None
    gear = None
    handbrake = None
    capacity_fuel = None
    liter_price = None
    distance = None
    speed = None
    m = manage_log.Manage_log()

    def __init__(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: init the parameters,
                Return: Null"""
        self.fuel = int(os.getenv('FUEL'))
        self.consumption_fuel = os.getenv('CONSUMPTION_FUEL')
        self.money = int(os.getenv('MONEY'))
        self.handbrake = bool(os.getenv('HANDBRAKE'))
        self.capacity_fuel = int(os.getenv('CAPACITY_FUEL'))
        self.liter_price = int(os.getenv('LITER_PRICE'))
        self.distance = int(os.getenv('DISTANCE'))
        self.speed = os.getenv('SPEED')

    def start(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: start engine,
                Return: Null"""
        try:
            self.m.open_file()
        except FileNotFoundError:
            self.m.write_to_log("start *FileNotFoundError*", self.fuel, self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
        self.gear = 0
        self.handbrake = True
        self.m.write_to_log("start", self.fuel, self.consumption_fuel, self.money, self.handbrake,
                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
        try:
            self.drive()
            return 1
        except ValueError:
            self.m.write_to_log("drive *ValueError*", self.fuel, self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
            return 0
        except OverflowError:
            self.m.write_to_log("drive *OverflowError*", self.fuel, self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
            try:
                self.fuel_charge()
                return 1
            except OverflowError:
                self.m.write_to_log("fuel_charge *OverflowError*", self.fuel, self.consumption_fuel, self.money, self.handbrake,
                                    self.capacity_fuel, self.liter_price, self.distance, self.speed)
                try:
                    self.stop()
                    return 0
                except Exception:
                    self.m.write_to_log("stop *Exception*", self.fuel, self.consumption_fuel, self.money, self.handbrake,
                                        self.capacity_fuel, self.liter_price, self.distance, self.speed)
                    self.close_file()
                    return 0

    def drive(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: drive user if distance < fuel,
                Return: Null"""
        ls = self.consumption_fuel.split("/")
        calc_liter_to_drive = int(self.distance / int(ls[1]))
        if not isinstance(calc_liter_to_drive, int):
            raise ValueError
        elif calc_liter_to_drive > self.fuel:
            raise OverflowError
        elif calc_liter_to_drive <= self.fuel:
            self.fuel -= calc_liter_to_drive
            ls_speed = self.speed.split(",")
            for i in ls_speed:
                if i != 's':
                    try:
                        self.gear_update(int(i))
                    except OverflowError:
                        self.m.write_to_log("gear_update *OverflowError*", self.fuel, self.consumption_fuel, self.money,
                                            self.handbrake,
                                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
                    except ValueError:
                        self.m.write_to_log("gear_update *ValueError*", self.fuel, self.consumption_fuel, self.money,
                                            self.handbrake,
                                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
                else:
                    try:
                        self.stop()
                        break
                    except Exception:
                        self.m.write_to_log("stop *Exception*", self.fuel, self.consumption_fuel, self.money,
                                            self.handbrake,
                                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
                        self.close_file()

    def gear_update(self, speed):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: update the gear pear speed,
                Return: Null"""
        self.gear = round(speed // 20)
        if not isinstance(self.gear, int):
            raise ValueError
        elif self.gear > 6:
            self.gear = 6
            raise OverflowError
        return 1

    def fuel_charge(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: charge full fuel car if user have money,
                Return: Null"""
        liters_to_fuel = self.capacity_fuel - self.fuel
        if liters_to_fuel * self.liter_price <= self.money:
            self.fuel += liters_to_fuel
            self.money -= liters_to_fuel * self.liter_price
            try:
                self.start()
                return 1
            except Exception:
                self.m.write_to_log("start *Exception*", self.fuel, self.consumption_fuel, self.money,
                                    self.handbrake,
                                    self.capacity_fuel, self.liter_price, self.distance, self.speed)
                try:
                    self.stop()
                    return 0
                except Exception:
                    self.m.write_to_log("stop *Exception*", self.fuel, self.consumption_fuel, self.money,
                                        self.handbrake,
                                        self.capacity_fuel, self.liter_price, self.distance, self.speed)
                    self.close_file()
                    return 0
        else:
            raise OverflowError

    def stop(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: stop engine,
                Return: Null"""
        self.gear = 0
        self.handbrake = False
        self.m.write_to_log("stop", self.fuel, self.consumption_fuel, self.money, self.handbrake,
                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
        self.close_file()
        return 1

    def close_file(self):
        self.m.close_log_file()
        return 1
