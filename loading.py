import sys
import time

for i in range(30):                   #replace range(n) with n and the process will happen n/3 time
    dots = "." * (i % 4)
    sys.stdout.write("\rSearching" + dots + "   ")
    sys.stdout.flush()
    time.sleep(0.3)

print("\nDone!")