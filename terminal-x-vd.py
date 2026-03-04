import subprocess
import time

subprocess.run("git add .", shell=True)
time.sleep(2)
subprocess.run('git commit -m \"auto commit\" ', shell=True)
time.sleep(2)
subprocess.run("git push origin main ", shell=True)
