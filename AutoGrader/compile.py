import os
import subprocess
def compilee():
  subprocess.call("rm -f ./a.out", shell=True)
  retcode = subprocess.call("/usr/bin/g++ walk.cc", shell=True)
  if retcode:
     print("failed to compile walk.cc")
  exit
  subprocess.call("rm -f ./output", shell=True)
  retcode = subprocess.call("./test.sh", shell=True)
  temp=""
  print("*************Original submission*************")
  with open('walk.cc','r') as fs:
    for line in fs:
      temp=temp+line+'<br>'
  temp=temp+str(retcode)
  return temp



