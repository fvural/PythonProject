

def cls():
    import os
    os.system('cls')
    return
cls()

import time
starttime=time.time()

x=0
while True:

  import random
  from datetime import datetime

  adi = random.choice(['x', 'y', 'z', 'a', 'b'])
  soyadi = random.choice(['x', 'y', 'z', 'a', 'b'])
  no = random.randint(10, 99)
  date = str(datetime.now())

  x=x+1
  print( x,no,adi, soyadi,date)

  time.sleep(5.0 - ((time.time() - starttime) % 5.0))

