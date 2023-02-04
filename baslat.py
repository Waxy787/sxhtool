from colorama import Fore
import time
print(Fore.GREEN)
ascii = f"""
  ______  ___   _ _____ ___   ___  _     
 / ___. ./ / | | |_   _/ _ . / _ .| |    
 \___ ..  /| |_| | | || | | | | | | |    
  ___) /  .|  _  | | || |_| | |_| | |___ 
 |____/_/._._| |_| |_| \___/ \___/|_____|
                               {Fore.CYAN}by {Fore.RED}@waxy787
   """

ascii = ascii.replace(".","\\")
print(ascii)
print(f"""
{Fore.RED}
[1] DDoS            [2] IpFounder
[3] MatrixScreen    [4] EndlossPanel
[5] Bomber          [6] IP -> Location
[7] Exit""".replace(".","\\"))

def sor():
	global q
	q = input(f"{Fore.CYAN}>> {Fore.RESET}")
	
	if q == "1":
		import resources.ddosattack
	elif q == "2":
		import resources.ipfounder
	elif q == "3":
		import resources.matrixscreen
	elif q == "4":
		import resources.endlosspanel
	elif q == "5":
		import resources.sxbomber
	elif q == "6":
		with open("resources/iploc.py", "w") as f:
			f.write(from json import loads
from requests import get, post
from sys import exit
from time import sleep
from random import choice
from colorama import Fore
import colorama
import colored

api_key = "ba8484c0c2706202049aa0bab48e9b9e"

ascii = f"""
  ______  ___   _ _____ ___   ___  _     
 / ___. ./ / | | |_   _/ _ . / _ .| |    
 \___ ..  /| |_| | | || | | | | | | |    
  ___) /  .|  _  | | || |_| | |_| | |___ 
 |____/_/._._| |_| |_| \___/ \___/|_____|
                               {Fore.CYAN}by {Fore.RED}@waxy787
   """

ascii = ascii.replace(".","\\")

def identify(target_ip):
    
    try:
        data = f"http://api.ipstack.com/{target_ip}?access_key={api_key}&format=1" 
        res = get(url = data)
        jtext = res.text
        jtext = loads(jtext)
        
        # data:
        ip = jtext["ip"]
        city = jtext["city"]
        ip_type = jtext["type"]
        latitude = jtext["latitude"]
        longitude = jtext["longitude"]
        region_code = jtext["region_code"]
        region_name = jtext["region_name"]
        country_code = jtext["country_code"]
        country_name = jtext["country_name"]
        capital = jtext["location"]["capital"]
        continent_code = jtext["continent_code"]
        continent_name = jtext["continent_name"]
        calling_code = jtext["location"]["calling_code"]
        language_code = jtext["location"]["languages"][0]["code"]
        language_name = jtext["location"]["languages"][0]["name"]
        flag_pic = f"http://assets.ipstack.com/flags/{country_code.lower()}.svg"
        
        print(f"""
        ______________________
        |IP:                  {ip_type:20} {ip} 
        |Continent:           {continent_code:20} {continent_name}
        |Country:             {country_code:20} {country_name}
        |Region:              {region_code:20} {region_name}
        |City:                {city}
        |latitude:            {latitude}
        |longitude:           {longitude}
        |Capital:             {capital}
        |language:            {language_code:20} {language_name}
        |calling code:        {calling_code}
        |Flag photo link:     {flag_pic}
        -----------------------
        """)
    except KeyboardInterrupt:
        print("[!]Çıkıldı")
        exit()
    except:
        print("[!] zaman aşımı !")



def get_my_ip_server1():
    takeip = post("https://api.myip.com", timeout=3)    
    myipjson = takeip.text
    myip = str(loads(myipjson)["ip"])
    mycountry = str(loads(myipjson)["country"])
    ipaddr = "* IP Addresi : "+myip+"
* country : "+mycountry+""
    return ipaddr

def get_my_ip_server2():
    myip = get("https://api.ipify.org", timeout=3).text
    ipaddr = f"* public IP addresiniz: {myip}"
    return ipaddr

def get_my_ip_server3():
    myip = get("https://ident.me", timeout=3).text
    ipaddr = f"* public IP addresiniz: {myip}"
    return ipaddr



def getmyip():
    
    try:
        return get_my_ip_server1()
    except KeyboardInterrupt:
        print("[!]Çıkı")
        exit()
    except:
        
       
        try:
            return get_my_ip_server2()
        except KeyboardInterrupt:
            print("[!] Çıkıldı")
            exit()
        except:

           
            try:
                return get_my_ip_server3()
            except KeyboardInterrupt:
                print("[!] Çıkıldı")
                exit()
            
            
            except:
                print("[!] Hata Internete Bağlı mısın?")
                return 


print(ascii)
   
print(f"[+] youre ip:
{getmyip()}
")

while True:
        
	try:
		target_ip = input(str("[>] IP Geolocation [IP veya Q]
>> "))

		if target_ip.lower() == "q":
			print("[!] Çıkış!")
			exit()
		else:
			identify(target_ip)

	except KeyboardInterrupt:
		print("[!] Çıkıldı")
		exit()''')
		import resources.iploc
	elif q == "7":
		print(Fore.RED + "Çıkış Yapılıyor... ")
		time.sleep(2)
		exit()
	else:
		print("Something went wrong! Please Enter a Valid Number !")
while True:
	sor()
