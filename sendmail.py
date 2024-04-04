import smtplib
import re
from email.mime.text import MIMEText
import aescipher
import re

def mkpw():

	autokey = [0x10, 0x01, 0x15, 0x1B, 0xA1, 0x11, 0x57, 0x72, 0x6C, 0x21, 0x56, 0x57, 0x62, 0x16, 0x05, 0x3D,
        0xFF, 0xFE, 0x11, 0x1B, 0x21, 0x31, 0x57, 0x72, 0x6B, 0x21, 0xA6, 0xA7, 0x6E, 0xE6, 0xE5, 0x3F]

	aesc = aescipher.AESCipher(bytes(autokey))
	pw = aesc.decrypt('비밀번호')
	#pw2 = aesc.encrypt('elduebkfjktqwoho')
	del aesc

	return pw.decode('utf-8') 


def sendmail(list):
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()      # say Hello
	smtp.starttls()  # TLS
	smtp.login('메일주소', mkpw())
	resul=re.sub('x1b[0-9][0-9]m','',list.replace('[','').replace(r'\n','\n').replace('  ',' ').replace('\\','|'))
	pp = resul.split('\n')
	
#	for index , x in enumerate(pp):
#		tt=pp[index].replace('\\',r'\\')
#		print(tt.split(r'\\'))

	msg = MIMEText(resul)
	
	msg['Subject'] = 'Dash board rasberypi'
#	msg['send'] = 'yayoye118@gmail.com'
	msg['send'] = 'noreply@gmail.com'
	msg['To'] = '받을주소'
	#msg['To2'] = 'yossaco@naver.com'
	#print(msg.as_string().replace('[',''))
	smtp.sendmail(msg['send'], msg['To'], msg.as_string())
	#smtp.sendmail(msg['send'], msg['To2'], msg['msg'])
	smtp.quit()


def sendmail2(mailto, mailfrom ,sub,cont):
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()      # say Hello
	smtp.starttls()  # TLS

	smtp.login('SMTP주소', mkpw())
	msg = MIMEText(cont,'html')
	msg['Subject'] = sub
	msg['send'] = mailto
	msg['To'] = mailfrom
	msg['From'] = mailto
	smtp.sendmail(msg['From'], msg['To'], msg.as_string())

	smtp.quit
