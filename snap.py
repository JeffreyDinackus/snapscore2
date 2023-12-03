
import subprocess
import time



i = 0

total_sends = 400
def adb_command(command):
    subprocess.run(['adb', 'shell', command])



def long_click(x, y, z, q, duration=2000):
    adb_command(f'input touchscreen swipe {x} {y} {z} {q} {duration}')


def short_click(x, y):
    adb_command(f'input tap {x} {y}')

while i < 400:

  short_click(542,1777)


  time.sleep(1.5)





  short_click(931,2063)

  time.sleep(1.5)

  short_click(978, 1226)
  time.sleep(1.5)


  short_click(1017,2059)

  time.sleep(1.5)


  long_click(919, 1250, 400, 1300, 1000)


  time.sleep(1.5)
  i+=1