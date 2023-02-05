from random import randint
from time import sleep
from os import name, system
from colorama import Fore, init, Back
from threading import Thread
from tty import setcbreak
from termios import tcgetattr,tcsetattr,TCSAFLUSH
from sys import stdin

init()
places = ["parti salonu", "ön koridor", "mutfak",
    "kostüm odası", "sol koridor", "sağ koridor", "ofis"]

night = 1

"""def cls():
    system('cls' if name == 'nt' else 'clear')

cls()"""
system('cls' if name == 'nt' else 'clear')
def getch(stxt):
    print(stxt,end='')
    fd = stdin.fileno()
    try:
        setcbreak(fd)
        return stdin.read(1)
    finally:
        tcsetattr(fd, TCSAFLUSH, tcgetattr(fd))

def clock():
   global t
   t = 1
   while True:
        sleep(40)
        t += 1

class tool:
    def __init__(self, name):
        self.name = name
        self.status = randint(5, 7)

    def zarar_ver(self):
        self.status -= 1

    def now_status(self):
        if self.status < 2:
            return False

        else:
            return True

    def tamir_et(self):
        print("{}{} tamir ediliyor..{}".format(
            Fore.YELLOW, self.name, Fore.RESET))
        sleep(randint(2, 4))
        self.status = randint(5, 7)

vent = tool("havalandırma sistemi")
ses_sistemi = tool("ses sistemi")
kamera = tool("kamera sistemi")

class character:

    def __init__(self, name):
        self.name = name
        self.room = places.index("parti salonu")

    def ilerle(self):
            if self.room+1 >= len(places):
                pass
            else:
                self.room += 1
    def geri(self):
    	    if self.room-1 < 0:
    	    	pass
    	    else:
    	    	self.room -= 1

    def call(self, room):
            if places[places.index(room)+1] == places[self.room] or places[places.index(room)-1] == places[self.room]:
                self.room = places.index(room)

def clear_line(n=1):
    #LİNE_UP = '\033[1A'
    #LİNE_CLEAR = '\x1b[2K'
    for _ in range(n):
        print('\033[1A', end='\x1b[2K')
        
def power_minus():
	global power,pmr,minus_speed
	minus_speed = 4.5
	pmr=True
	power = 100
	while pmr:
		sleep(minus_speed)
		power -= 1
		
menu_busy = True

clocker = Thread(target=clock)
clocker.start()

def main():
    while True:
        if t==6:
        	clear_line(6)
        	print("""
        	###############
        ##    YOU WİN!      ##
        	###############""")
        	break
        if places[sp.room]=="ofis":
        	clear_line(6)
        	print("""\n
            ****************************
            ******     İT'S ME    ******
            ****************************""")
        	break
        if randint(0, int(37/night)) == 14:
            sp.ilerle()
        sleep(0.3)
        if menu_busy:
            if power < 35:
                text = """
            Saat {}
            Power : {}{}{}{}{}
            C: Cameras
            P: Tools panel
            """.format(t, Back.LIGHTRED_EX, Fore.BLACK, power, Fore.RESET, Back.RESET)
            elif power > 35 and power < 70:
                text = """
            Saat {}
            Power : {}{}{}{}{}
            C: Cameras
            P: Tools panel
            """.format(t, Back.LIGHTYELLOW_EX, Fore.BLACK, power, Fore.RESET, Back.RESET)
            else:
                text = """
            Saat {}
            Power : {}{}{}{}{}
            C: Cameras
            P: Tools panel
            """.format(t, Back.LIGHTGREEN_EX, Fore.BLACK, power, Fore.RESET, Back.RESET)
            print(text)
            clear_line(6)


sp = character("Springtrap")

main_thread = Thread(target=main)
main_thread.start()
power_minuser = Thread(target=power_minus)
power_minuser.start()

while True:
  if places[sp.room]=="ofis" or t==6:
  	break
  req = getch('')
  if req.lower() == "c":
     menu_busy = None
     clear_line(6)
     minus_speed -= 1
     if kamera.now_status():
        print(f"{Fore.GREEN}\n\tSpringtrap {Fore.RESET}-->{Fore.YELLOW}",places[sp.room], "{}".format(Fore.RESET))
        kamera.zarar_ver()
        if randint(0,2)==2:
        	vent.zarar_ver()
        places_counter = 0
        for p in places:
            places_counter += 1
            if places_counter != 2:
                print(f"{places.index(p)} {p}",end="\t|\t")
            elif places_counter == 2:
                print(f"{places.index(p)} {p}")
                places_counter = 0
        places_counter=None
        if ses_sistemi.now_status():
           try:
                req=int(getch("\n{}-->{}".format(Fore.MAGENTA,Fore.RESET)))
                sp.call(places[req])
                ses_sistemi.zarar_ver()
           except ValueError:
            	#print("{}Sayısal değer gir!{}".format(Fore.LIGHTRED_EX,Fore.RESET))
            	pass
           except IndexError:
                print("{}Bilinmeyen oda!{}".format(Fore.LIGHTRED_EX,Fore.RESET))
                ses_sistemi.zarar_ver()
                sleep(0.19)
        else:
        	getch('')
     else:
        print(f"{Fore.GREEN}\n\tSpringtrap {Fore.RESET}-->{Fore.RED}Error{Fore.RESET}")
        print("""Err \t|\t rror
        E4ror \t|\t Error
        E5rar \t|\t Errar
        Ərror \t
        """)
        if ses_sistemi.now_status():
           try:
                req=int(getch("\n{}-->{}".format(Fore.MAGENTA,Fore.RESET)))
                sp.call(places[req])
                ses_sistemi.zarar_ver()
           except ValueError:
            	#print("{}Sayısal değer gir!{}".format(Fore.LIGHTRED_EX,Fore.RESET))
            	pass
           except IndexError:
                print("{}Bilinmeyen oda!{}".format(Fore.LIGHTRED_EX,Fore.RESET))
                ses_sistemi.zarar_ver()
                sleep(0.19)
        else:
        	getch('')
     minus_speed += 1
     system('cls' if name == 'nt' else 'clear')
     menu_busy = True
     
  elif req.lower()=="p":
        clear_line(6)
        menu_busy=None
        if randint(0,2)==2:
        	vent.zarar_ver()
        minus_speed -= 1
        if ses_sistemi.now_status():
            print(f"Ses sistemi{Fore.GREEN} iyi. {Fore.BLUE}{ses_sistemi.status}")
        else:
            print(f"{Fore.RESET}Ses sistemi{Fore.RED} arızalı!")
        if vent.now_status():
            print(f"{Fore.RESET}Havalandırma sistemi {Fore.GREEN}iyi. {Fore.BLUE}{vent.status}")
        else:
            print(f"{Fore.RESET}Havalandırma {Fore.RED}arızalı!")
        if kamera.now_status():
            print(f"{Fore.RESET}Kamera sistemi {Fore.GREEN}iyi. {Fore.BLUE}{kamera.status}\n")
        else:
            print(f"{Fore.RESET}Kamera sistemi {Fore.RED}arızalı!\n")
        req=getch("\n{}-->{}".format(Fore.MAGENTA,Fore.RESET))
        if req.lower()=='k' or req.lower()=='c':
            kamera.tamir_et()
        elif req.lower()=='s' or req.lower()=='a':
            ses_sistemi.tamir_et()
        elif req.lower()=='h' or req.lower()=='v':
            vent.tamir_et()
        minus_speed+=1
        clear_line(6)
        menu_busy=True
exit()
