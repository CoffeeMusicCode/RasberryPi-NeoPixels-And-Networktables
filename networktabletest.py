import sys
import time
import logging

from networktables import *

logging.basicConfig(level=logging.DEBUG)
NetworkTables.initialize()
nt = NetworkTables.getTable('RasberryPi')

while True:
  nt.putString('state', 'Disabled') # Disabled Auto TeleOp
  nt.putNumber('toggle', 1) # 0 1
  nt.putNumber('detaunt1', 1) # 0 - 10
  nt.putNumber('detaunt2', 5) # 0 - 10
  time.sleep(1)
