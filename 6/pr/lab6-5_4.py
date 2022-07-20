# 4

from datetime import datetime
import time
from my_module import q

f = open("input.txt")
f2 = open("output.txt", 'w')
vremya = time.time()
f2.write(str(datetime.fromtimestamp(vremya)) + '\n')
f2.write(str(q(int(f.readline()))) + '\n')
f2.write(str(time.time() - vremya))
f.close()
f2.close()
