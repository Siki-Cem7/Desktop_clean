import subprocess
import sys
import Destination
import Desktop_check


class Filter():



    def __init__(self):

        self.Dest = Destination.Destination()
        self.Desk = Desktop_check.Desktop_Check()
        self.list_only_files = []
        self.Desk.request()



    def filter(self):

        for file in self.Desk.list_all_files:

            if(".png" in file or ".jpeg" in file or ".wpeb" in file
            or ".ico" in file or ".txt" in file or ".docx" in file
            or not "." in file or ".pdf" in file):
                if(file == "Windows 10" or file == "Kali Linux 2021.1 ARM64"):
                    None
                else:
                    self.list_only_files.append(file)
