#!/use/bin/evn python3
# https://github.com/aynencano
# Author - Sajjad

from zipfile import ZipFile
import sys
import os

argv=False
try:
	if (sys.argv[1]=="-version" or sys.argv[1]=="--version"):
		print("Zipcrack - version 1.0")
		argv=True
	else:
		pass
except:
	pass

def print_help():
	print("""
	
     zipfile          :   Zip dosyasını yaz.
     password list    :   Parola listesini belirtin.
     help             :   yardım göster.
     quit             :   Tooldan çıkış yap.
     --version        :   Zipcrack sürümünü görüntüleyin.
     --help           :   Show help.
	""")


try:
	if (sys.argv[1]=="-help" or sys.argv[1]=="--help"):
		print_help()
		argv=True
	else:
		pass
except:
	pass

if (argv==True):
	sys.exit()
else:
	pass

os.system("clear")

print("""\033[1;96m

                 CHANNEL @ROLEX_HACK
                  ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇
                  ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇
                  ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇
                  ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇
                  ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇
                  ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇
                  ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇
                  ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇
                     👇 DEVELOPER 👇
                     😁 DİYARREAL😁
                                      


\033[0;0m""")

while(True):
	try:
		exit=False
		action=input("\nDosya İsmini Gir Cano </> ")
		if(action=="quit"):
			exit=True
			break
		elif(action=="help"):
			print_help()
		else:
			pass
		try:
			zip=ZipFile(action,"r")
			break
		except:
			if(action=="" or action=="help"):
				pass
			else:
				print("\n\033[0;91m[!] Zip dosyası bulunamadı!\033[0;0m")
	except:
		pass


if (exit==True):
	sys.exit()
else:
	pass

list=input("\nWordlist Gir Cano </> ")

try:
	word=open(list,"rb")
	count=open(list,"r")
except:
	print("\n\033[0;91m[!] Parola listesi bulunamadı!\033[0;0m")
	sys.exit()

print("\n")
line=count.readline()
condition=0
while(line):
	password=word.readline()
	try:
		zip.extractall(path="Çıkarmak",pwd=password.strip())
		print("\n[Gözün aydın şifreniz ] :: {}".format(password.decode()))
		condition+=1
		break
	except:
		print(password.decode())
	line=count.readline()
	
if(condition==0):
	print("\n[Şifreniz Bulunamadı]")
else:
	pass

zip.close()
word.close()
count.close()

