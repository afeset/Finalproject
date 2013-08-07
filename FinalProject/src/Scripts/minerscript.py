'''
Created on Mar 11, 2013

@author: asaf
'''


#Original Miner script for insertion into DB (pre-object-oriented)
import subprocess
var=raw_input("Please enter your path to the miner")
string_to_use="/home/asaf/miner1.3/miner -f /home/asaf/Downloads/miner_script_pushToDB "+str(var)+" -o /home/asaf/Downloads/output.txt"
subprocess.call(string_to_use, stdin=None, stdout=None, stderr=None, shell=True)

'''
# Script for Creation of Lists of Objects from Miner:
import subprocess
var=raw_input("Please enter your path to the miner")
string_to_use="/home/asaf/miner1.3/miner -f /home/asaf/miner1.3/createListsScript "+str(var)+" -o /home/asaf/Downloads/output.txt"
subprocess.call(string_to_use, stdin=None, stdout=None, stderr=None, shell=True)
'''
'''
Use this as input:
/home/asaf/miner1.3/log-0000.20130212-010820.253.qbl
'''
