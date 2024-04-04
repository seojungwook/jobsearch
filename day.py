
import sendmail

import subprocess

cmd = ["pm2 list","vcgencmd measure_temp","last -f /var/log/btmp","last"]
result = ""
a = []
for i in range(0,len(cmd),1):
	if i==0:
		result=result+str(subprocess.check_output(cmd[i],shell=True).decode("utf-8"))
		#print(result)
	else :
		result=result+str(subprocess.check_output(cmd[i],shell=True))
	if i==1 :
		a = result.split("=")
	result=result+"-"*50+"\n"
b = a[1].split("'")
#if float(b[0]) > 50:
#	sendmail.sendmail(result)
sendmail.sendmail(result)
