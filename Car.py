import os
from dotenv import load_dotenv

import manage_log

load_dotenv()


class Car:
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
            self.m.write_to_log(os.getenv('START_STATUS') + os.getenv('FILE_NOT_FOUND_ERROR_EXCEPTION'), self.fuel,
                                self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
        self.gear = 0
        self.handbrake = True
        self.m.write_to_log(os.getenv('START_STATUS'), self.fuel, self.consumption_fuel, self.money, self.handbrake,
                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
        try:
            if (self.fuel <= self.capacity_fuel):
                self.drive()
                return 1
            else:
                self.m.write_to_log(os.getenv('START_STATUS') + os.getenv('FUEL_LARGE_THEN_FUEL_CAPACITY'), self.fuel, self.consumption_fuel, self.money,
                                    self.handbrake,
                                    self.capacity_fuel, self.liter_price, self.distance, self.speed)
        except ValueError:
            self.m.write_to_log(os.getenv('DRIVE_STATUS') + " " + os.getenv('VALUE_ERROR_EXCEPTION'), self.fuel,
                                self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
            return 0
        except OverflowError:
            self.m.write_to_log(os.getenv('DRIVE_STATUS') + " NEED CHARGE " + os.getenv('OVER_FLOW_ERROR_EXCEPTION'), self.fuel,
                                self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
            try:
                self.fuel_charge()
                return 1
            except OverflowError:
                self.m.write_to_log(os.getenv('FUEL_CHARGE_STATUS') + " NEED CHARGE " + os.getenv('OVER_FLOW_ERROR_EXCEPTION'),
                                    self.fuel, self.consumption_fuel, self.money, self.handbrake,
                                    self.capacity_fuel, self.liter_price, self.distance, self.speed)
                try:
                    self.stop()
                    return 0
                except Exception:
                    self.m.write_to_log(os.getenv("STOP_STATUS") + " " + os.getenv('EXCEPTION'), self.fuel,
                                self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
                    self.close_file()
                    return 0
        except Exception:
            self.m.write_to_log(os.getenv("DRIVE_STATUS") + " " + os.getenv('USER_NOT_HAVE_MONEY'), self.fuel, self.consumption_fuel, self.money, self.handbrake, self.capacity_fuel, self.liter_price, self.distance, self.speed)
            self.stop()

    def drive(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: drive user if distance < fuel,
                Return: Null"""
        self.ls = self.consumption_fuel.split("/")
        calc_liter_to_drive = int(self.distance / int(self.ls[1]))
        # if calc liters not int
        if not isinstance(calc_liter_to_drive, int):
            raise ValueError
        # if user don't have fuel to drive, user drive what he can and parent send him to charge
        elif calc_liter_to_drive > self.fuel and calc_liter_to_drive <= self.capacity_fuel:
            self.distance -= int((self.fuel * int(self.ls[1])))
            self.fuel -= self.fuel
            # if user need to drive and he don't have money
            if self.money == 0:
                raise Exception
            raise OverflowError
        # if user have fuel to drive, drive usually
        elif calc_liter_to_drive > self.fuel and calc_liter_to_drive > self.capacity_fuel:
            self.fuel -= self.capacity_fuel
            self.distance -= (self.capacity_fuel * int(self.ls[1]))
            self.stop()
            self.start()
        # if user don't need charge
        elif calc_liter_to_drive <= self.fuel:
            self.fuel -= calc_liter_to_drive
            self.distance -= (calc_liter_to_drive * int(self.ls[1]))
            ls_speed = self.speed.split(",")
            for i in ls_speed:
                if i != os.getenv('CHAR_STOP'):
                    try:
                        self.gear_update(int(i))
                    except OverflowError:
                        self.m.write_to_log(
                            os.getenv('GEAR_UPDATE_STATUS') + " GEAR YET 6 " + os.getenv('OVER_FLOW_ERROR_EXCEPTION'), self.fuel,
                            self.consumption_fuel, self.money,
                            self.handbrake,
                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
                    except ValueError:
                        self.m.write_to_log(os.getenv('GEAR_UPDATE_STATUS') + " " + os.getenv('VALUE_ERROR_EXCEPTION'),
                                            self.fuel, self.consumption_fuel, self.money,
                                            self.handbrake,
                                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
                else:
                    try:
                        self.stop()
                        break
                    except Exception:
                        self.m.write_to_log(os.getenv("STOP_STATUS") + " " + os.getenv('EXCEPTION'), self.fuel,
                                            self.consumption_fuel, self.money,
                                            self.handbrake,
                                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
                        self.close_file()

    def gear_update(self, speed):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: update the gear pear speed,
                Return: Null"""
        self.gear = round(speed // int(os.getenv('DISTANCE_BETWEEN_GEAR')))
        if not isinstance(self.gear, int):  # if num gear not int
            raise ValueError
        elif self.gear > int(os.getenv('NUMBERS_GEARS')):  # if user want to up from 6
            self.gear = 6
            raise OverflowError
        return 1

    def fuel_charge(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: charge full fuel car if user have money,
                Return: Null"""
        self.coffee_and_cake = int(os.getenv('COFFEE_AND_CAKE'))
        self.high_distance = int(os.getenv('HIGH_DISTANCE'))
        # if user have money and distance is high, he buy sale - Coffee and Cake
        if self.money > self.coffee_and_cake and self.distance >= self.high_distance:
            self.money -= self.coffee_and_cake
            self.m.write_to_log(os.getenv('FUEL_CHARGE_STATUS') + " " + os.getenv('TIME_OUT_ERROR_EXCEPTION'),
                                self.fuel, self.consumption_fuel, self.money, self.handbrake,
                                self.capacity_fuel, self.liter_price, self.distance, self.speed)
        liters_to_fuel = self.capacity_fuel - self.fuel
        # charge car ful tank (if user have money)
        if liters_to_fuel * self.liter_price <= self.money:
            self.fuel += liters_to_fuel
            self.money -= liters_to_fuel * self.liter_price
            try:
                self.start()
                return 1
            except Exception:
                self.m.write_to_log(os.getenv("START_STATUS") + " " + os.getenv('EXCEPTION'), self.fuel,
                                    self.consumption_fuel, self.money,
                                    self.handbrake,
                                    self.capacity_fuel, self.liter_price, self.distance, self.speed)
                try:
                    self.stop()
                    return 0
                except Exception:
                    self.m.write_to_log(os.getenv("STOP_STATUS") + " " + os.getenv('EXCEPTION'), self.fuel,
                                        self.consumption_fuel, self.money,
                                        self.handbrake,
                                        self.capacity_fuel, self.liter_price, self.distance, self.speed)
                    self.close_file()
                    return 0
        # charge car by money
        elif liters_to_fuel * self.liter_price > self.money:
            self.fuel += self.money / int(self.ls[1])
            self.money -= self.money
            self.start()
            return 1
        else:
            raise OverflowError

    def stop(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: stop engine,
                Return: Null"""
        self.gear = 0
        self.handbrake = False
        self.m.write_to_log(os.getenv("STOP_STATUS"), self.fuel, self.consumption_fuel, self.money, self.handbrake,
                            self.capacity_fuel, self.liter_price, self.distance, self.speed)
        self.close_file()
        return 1

    def close_file(self):
        self.m.close_log_file()
        return 1
