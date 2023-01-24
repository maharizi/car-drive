import os
from datetime import datetime


class Manage_log:
    f = None
    f_e = None
    time = datetime.now().strftime(" %d/%m/%Y %H:%M:%S ")

    def open_file(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: open logs file
                Return: Null"""
        try:
            self.f = open('logs', 'a')
            return 1
        except FileExistsError:
            raise FileNotFoundError

    def write_to_log(self, status, fuel, consumption_fuel, money, handbrake,
                     capacity_fuel, liter_price, distance, speed):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: write to logs file
                Return: Null"""
        self.f.write(f"\n car {status} ! --- " + self.time)
        self.f.write(f"fuel:{fuel}, consumption fuel:{consumption_fuel}, money:{money}, handbrake:{handbrake}, "
                     f"capacity fuel:{capacity_fuel}, liter_price:{liter_price}, distance:{distance}, speed:{speed}")
        self.f.write("")
        self.f.flush()

    def write_exceptions_to_log(self, string_exceptions):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: write to logs file
                Return: Null"""
        self.f_e = open('logs', "a")
        self.f_e.write("\n"+string_exceptions + "---" + self.time)
        self.f_e.flush()
        self.f_e.close()

    def close_log_file(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: close logs file
                Return: Null"""
        self.f.close()
