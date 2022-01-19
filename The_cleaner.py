import subprocess
import sys
import Destination
import Desktop_check
import Desktop_filter


class Clean():

    def __init__(self):

        self.Dest = Destination.Destination()
        self.Desk = Desktop_check.Desktop_Check()
        self.DesF = Desktop_filter.Filter()
        self.DesF.filter()






    def Clean_txt(self):

        try:
            for file in self.DesF.list_only_files:
                if (".txt" in file):
                    print(file)
                    self.respone = subprocess.Popen(
                        [f"cp {self.Dest.destination_to_clean}{file} {self.Dest.destination_dir_txt}"],
                        stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

                    stdout, stderr = self.respone.communicate()
        except:
            print("Something goes wrong")




    def Clean_pdf(self):

        try:
            for file in self.DesF.list_only_files:
                if(".pdf" in file):
                    print(file)
                    self.respone = subprocess.Popen([f"cp {self.Dest.destination_to_clean}{file} {self.Dest.destination_dir_pdf}"],
                                                    stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

                    stdout, stderr = self.respone.communicate()
        except:
            print("Something goes wrong")






if __name__ == "__main__":
    d = Clean()
    d.Clean_txt()