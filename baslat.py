k = requests.get("https://raw.githubusercontent.com/Waxy787/sxhtool/main/baslat.py").text
with open("baslat.py", "r") as f:
	read = f.read()
if read == k:
	try:
		import os
		import requests
		import json
		get = requests.get("https://sxapi.waxy787.repl.co/key")
		get = json.loads(get.text)
		while 1:
			print("You Must Verify! Please Enter the Given Code")
			inp = input("---> ")
			if inp == get['key']:
				os.system("cls||clear")
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
{Fore.RED}[ 1 ] {Fore.YELLOW}DDoS
{Fore.RED}[ 2 ] {Fore.YELLOW}IpFounder
{Fore.RED}[ 3 ] {Fore.YELLOW}MatrixScreen
{Fore.RED}[ 4 ] {Fore.YELLOW}Bomber
{Fore.RED}[ 5 ] {Fore.YELLOW}IP -> Location
{Fore.RED}[ 6 ] {Fore.YELLOW}Port Scanner
{Fore.RED}[ 7 ] {Fore.YELLOW}Setup
{Fore.RED}[ 8 ] {Fore.YELLOW}Exit""".replace(".","\\"))
				def ddos():
					import resources.ddosattack
				def ipf():
					import resources.ipfounder
				def sor():
					global q
					q = input(f"{Fore.CYAN}~root@waxy787>  {Fore.RESET}")
			
					if q == "1":
						return ddos()
					elif q == "2":
						return ipf()
					elif q == "3":
						import resources.matrixscreen
					elif q == "4":
						import resources.endlosspanel
					elif q == "5":
						import bomber.sxbomber
					elif q == "6":
						import resources.iploc
					elif q == "7":
						import resources.portscanner
					elif q == "8":
						print(Fore.RED + "Checking Out... ")
						time.sleep(2)
						exit()
					else:
						print("Something went wrong! Please Enter a Valid Number !")
				while True:
					sor()
		
			else:
				print("Verification Code Incorrect! Please try again")
	except:
		from colorama import Fore
		print(Fore.RED + "An error has occurred, try again later" + Fore.RESET)
else:
	print(Fore.RED + "Update in progress")
	time.sleep(3)
	with open("baslat.py", "w") as f:
		f.write(k)
	print("Update Successful, Please restart the program.")
