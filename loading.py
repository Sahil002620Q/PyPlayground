import sys
import time

for i in range(30):
    dots = "." * (i % 4)
    sys.stdout.write("\rSearching" + dots + "   ")
    sys.stdout.flush()
    time.sleep(0.3)

print("\Scan complete!")