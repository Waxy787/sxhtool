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
		print(Fore.RED + "Bakımda...")
	elif q == "7":
		print(Fore.RED + "Çıkış Yapılıyor... ")
		time.sleep(2)
		exit()
	else:
		print("Something went wrong! Please Enter a Valid Number !")
while True:
	sor()
