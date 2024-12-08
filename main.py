import os
from keep_alive import keep_alive
os.system("chmod +x yt.sh")
os.system("bash yt.sh")
keep_alive()  # Starts a webserver to be pinged.