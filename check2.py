
import subprocess
import time



i = 0

total_sends = 100
def adb_command(command):
    subprocess.run(['adb', 'shell', command])



def long_click(x, y, z, q, duration=2000):
    adb_command(f'input touchscreen swipe {x} {y} {z} {q} {duration}')


def short_click(x, y):
    adb_command(f'input tap {x} {y}')


i = 0

while True == True:

  # short_click(280,500)
#   time.sleep(.3)
  short_click(335,830)
  time.sleep(.3)
#   short_click(651,1070)
  print(i)
  i+=1