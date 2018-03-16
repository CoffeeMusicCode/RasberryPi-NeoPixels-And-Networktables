import sys
import time
import logging

from networktables import *

logging.basicConfig(level=logging.DEBUG)
NetworkTables.initialize()
nt = NetworkTables.getTable('RasberryPi')

state = 'Disabled'
toggle = 1
detaunt1 = 10
detaunt2 = 5

while True:
  nt.putString('state', state) # Disabled Auto TeleOp
  nt.putNumber('toggle', toggle) # 0 1
  nt.putNumber('detaunt1', detaunt1) # 0 - 10
  nt.putNumber('detaunt2', detaunt2) # 0 - 10
  print(state, toggle, detaunt1, detaunt2)
  time.sleep(1)
