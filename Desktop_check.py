import subprocess
import sys
import Destination


class Desktop_Check():

    def __init__(self):

        self.Dest = Destination.Destination()
        self.list_all_files = []





    def request(self):

        self.result = subprocess.Popen(["ls"], cwd=self.Dest.destination_to_clean, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for res in self.result.stdout.readlines():
            self.list_all_files.append(res.decode("utf-8").strip())

        if(len(self.list_all_files) <= 1):
            print("No Files found at your desktop")
            sys.exit(4)
