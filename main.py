import subprocess
import time


#Search folder for new CSV Data files
subprocess.call("./search.sh")
time.sleep(5)


##############################

#Open found CSV an read out Data
