#!/usr/bin/python3

import sys
import os
import time
import sys

directory = "/media/sf_" + sys.argv[1]
xmlPath = directory + "/xmls"
scriptPath = directory + "/get_fileops.sh"

xmlsDone = []
os.system("sudo /home/spades/SPADE/bin/spade start")

dir_list = os.listdir(xmlPath)

file = dir_list[0]

ransomware = file.split('.')[0]

os.system(f''' echo {xmlPath}/{file}''')

os.system(f'''sudo {scriptPath} {directory} {ransomware}''')

os.system("sudo /home/spades/SPADE/bin/spade stop")

time.sleep(10)
