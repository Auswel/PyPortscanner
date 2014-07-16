#----------------------------------------------------------------#
# PyPortScanner, by Auswel                              @auswel  #
# http://github.com/Auswel/PyPortScanner/                        #
#                                                                #
# scanner.py                                                     #
# MIT License                                                    #
#                                                                #
#----------------------------------------------------------------#

import socket, sys, os, thread
from datetime import datetime
os.system('clear')
sp            =  (int)(raw_input("Starting port: "))
ep            =  (int)(raw_input("Ending port:   "))
STARTING_PORT = sp
ENDING_PORT   = ep
pstt          = ENDING_PORT - STARTING_PORT + 1
pst           = 0
os.system('clear')
print("Thread 1 (" + (str)(STARTING_PORT) + " - " + (str)((ENDING_PORT/2)+(STARTING_PORT/2)) + ")")
print("Thread 2 (" + (str)((ENDING_PORT/2)+(STARTING_PORT/2)+1) + " - " + (str)(ENDING_PORT) + ")")
print("Total Ports: " + (str)(pstt))
rs    =  raw_input("\n\nEnter a remote host to scan:\n   > ")
os.system('clear')
rsip  = socket.gethostbyname(rs)
ps = []
tt = datetime.now()
socket.setdefaulttimeout(1)
print("+------------------+")
def s(pstart,pend):
  global pst
  try:
    for p in range(pstart,pend+1): 
      pst+=1
      sys.stdout.write("| Scanning remote host (" + rsip + ":" + (str)(p) +") <Ports scanned: " + (str)(pst) + ">\n")
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      r = s.connect_ex((rsip, p))
      if r == 0:
        ps.append((str)(p))
      s.close()
  except KeyboardInterrupt:
    os.system("clear")
    print("[MESSAGE] Keyboard interrupt triggered.")
    print("[MESSAGE] Exitting Port Scanner...")
    sys.exit()
  except socket.gaierror:
    os.system("clear")
    print("[ERROR]   Hostname could not be resolved.")
    print("[MESSAGE] Exitting Port Scanner...")
    sys.exit()
  except socket.error:
    os.system("clear")
    print("[ERROR]   Could not connect to server.")
    print("[MESSAGE] Exitting Port Scanner...")
    sys.exit()
try:
  thread.start_new_thread(s, (STARTING_PORT,STARTING_PORT/2+ENDING_PORT/2,))
  thread.start_new_thread(s,(STARTING_PORT/2+ENDING_PORT/2+1,ENDING_PORT,))
except:
   print("[ERROR]   Could not start threads.")
   sys.exit()
while pst != pstt:
  pass
tn = datetime.now()
td =  tn - tt
print("|")
print("+------------------+")
print("|Scanning complete. (" + (str)(td) + ")")
print("+------------------+")
print("| Remote host:")
print("|   " + rs)
print("|   " + rsip)
print("+------------------+")
print("| Open ports:")
xpos=0
tpos=0
o = ""
if len(ps) >= 3:
  for x in ps:
    if xpos == 0:
      o =  ("| " + (str)(x))
    if xpos != 0:
      o += (", " + (str)(x))
    xpos += 1
    tpos += 1
    if tpos == len(ps):
      print(o)
    if xpos == 4:
      print(o)
      xpos = 0
else:
  for x in ps:
    print("| " + (str)(x))
print("+------------------+")
print("| Total Open Ports: ")
print("|    " + (str)(len(ps)))
print("+------------------+")


