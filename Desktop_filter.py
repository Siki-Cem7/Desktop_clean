import subprocess
import sys
import Destination
import Desktop_check


class Filter():

    def __init__(self):

        self.Dest = Destination.Destination()
        self.Desk = Desktop_check.Desktop_Check()


        #
        #
        #
        #
        self.Desk.request()
        #
        #
        #
        #


    def filter(self):

        # File filter for txt data-files
        for file in self.Desk.list_all_files:
            if(".png" in file or ".jpeg" in file or ".wpeb" in file or ".ico" in file):
                print(file)


if __name__ == "__main__":
    filt = Filter()
    filt.filter()
