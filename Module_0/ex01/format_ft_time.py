from datetime import datetime as d
import time


epoch = time.time()
print("Seconds since January 1, 1970: {:,.4f} or {:1.2e} "
      "in scientific notation".format(epoch, epoch))


time = d.now()
print(f"{time.strftime('%b %d %Y')}")
