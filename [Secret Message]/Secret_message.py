__author__ = 'Ahmed_EL_Atari'

import os
def Secert_msg():
    # Get File names
    file_list = os.listdir(r"C:\OOP\prank")
    # Change Directory
    os.chdir(r"C:\OOP\prank")
    # List & Change Files
    for file_name in file_list:
        #Rename files by trancate the numeric part
        os.rename(file_name,file_name.translate(None,"1234567890"))


# Function Call
rename_files()
