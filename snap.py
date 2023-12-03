
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

while i < total_sends:

  short_click(542,1777)


  time.sleep(.75)





  short_click(931,2063)

  time.sleep(1)

  short_click(978, 1226)
  # time.sleep(.5)


  # short_click(984, 1500)
  # time.sleep(.5)
  # short_click(966, 1655)



  time.sleep(.75)


  short_click(1017,2059)

  time.sleep(.75)


  long_click(919, 1250, 400, 1300, 500)


  time.sleep(.75)
  i+=1
  print(i)