import time

# ANSI escape codes
BLINK = '\033[5m'
RESET = '\033[0m'

print(f"{BLINK}This text is blinking!{RESET}")
print("This text is normal.")