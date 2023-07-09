import subprocess
import customtkinter
import psutil
from CTkMessagebox import CTkMessagebox

app = customtkinter.CTk()
app.geometry("1055x250")
app.title("Valorant Instalocker by Ashhad776")
app.resizable("False", "False")
def disable_event():
    pass
app.protocol("WM_DELETE_WINDOW", disable_event)

PROCNAME1 = "Astra.exe"
PROCNAME2 = "Breach.exe"
PROCNAME3 = "Brimstone.exe"
PROCNAME4 = "Chamber.exe"
PROCNAME5 = "Cypher.exe"
PROCNAME6 = "Deadlock.exe"
PROCNAME7 = "Fade.exe"
PROCNAME8 = "Gekko.exe"
PROCNAME9 = "Harbor.exe"
PROCNAME10 = "Jett.exe"
PROCNAME11 = "KayO.exe"
PROCNAME12 = "Killjoy.exe"
PROCNAME13 = "Neon.exe"
PROCNAME14 = "Omen.exe"
PROCNAME15 = "Phoenix.exe"
PROCNAME16 = "Raze.exe"
PROCNAME17 = "Reyna.exe"
PROCNAME18 = "Sage.exe"
PROCNAME19 = "Skye.exe"
PROCNAME20 = "Sova.exe"
PROCNAME21 = "Viper.exe"
PROCNAME22 = "Yoru.exe"
PROCNAME23 = "VALORANT-Win64-Shipping.exe"

process_names = [
    "Astra.exe", "Breach.exe", "Brimstone.exe", "Chamber.exe", "Cypher.exe", "Deadlock.exe",
    "Fade.exe", "Gekko.exe", "Harbor.exe", "Jett.exe", "KayO.exe", "Killjoy.exe", "Neon.exe",
    "Omen.exe", "Phoenix.exe", "Raze.exe", "Reyna.exe", "Sage.exe", "Skye.exe", "Sova.exe",
    "Viper.exe", "Yoru.exe"
]

def optionmenu_callback(choice):
    customtkinter.set_appearance_mode(choice)
  
def button_callback1():
    procAstra = subprocess.Popen([".\\AHKScripts\\Astra.exe"], stdin=subprocess.PIPE, close_fds=True)
    procAstra.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 1!")
    processes_to_kill = [
        PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
      
def button_callback2():
    procBreach = subprocess.Popen([".\\AHKScripts\\Breach.exe"], stdin=subprocess.PIPE, close_fds=True)
    procBreach.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 2")
    processes_to_kill = [
        PROCNAME1, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback3(): 
    procBrimstone = subprocess.Popen([".\\AHKScripts\\Brimstone.exe"], stdin=subprocess.PIPE, close_fds=True)
    procBrimstone.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 3")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback4():
    procChamber = subprocess.Popen([".\\AHKScripts\\Chamber.exe"], stdin=subprocess.PIPE, close_fds=True)
    procChamber.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 4")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
    
def button_callback5():
    procCypher = subprocess.Popen([".\\AHKScripts\\Cypher.exe"], stdin=subprocess.PIPE, close_fds=True)
    procCypher.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 5")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback6():
    procDeadlock = subprocess.Popen([".\\AHKScripts\\Deadlock.exe"], stdin=subprocess.PIPE, close_fds=True)
    procDeadlock.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 6")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback7():
    procFade = subprocess.Popen([".\\AHKScripts\\Fade.exe"], stdin=subprocess.PIPE, close_fds=True)
    procFade.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 7")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
  
def button_callback8():
    procGekko = subprocess.Popen([".\\AHKScripts\\Gekko.exe"], stdin=subprocess.PIPE, close_fds=True)
    procGekko.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 8")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback9():
    procHarbor = subprocess.Popen([".\\AHKScripts\\Harbor.exe"], stdin=subprocess.PIPE, close_fds=True)
    procHarbor.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 9")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback10():
    procJett = subprocess.Popen([".\\AHKScripts\\Jett.exe"], stdin=subprocess.PIPE, close_fds=True)
    procJett.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 10")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback11():
    procKayO = subprocess.Popen([".\\AHKScripts\\KayO.exe"], stdin=subprocess.PIPE, close_fds=True)
    procKayO.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 1 and Row 11")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback12():
    procKilljoy = subprocess.Popen([".\\AHKScripts\\Killjoy.exe"], stdin=subprocess.PIPE, close_fds=True)
    procKilljoy.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 1")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
  
def button_callback13():
    procNeon = subprocess.Popen([".\\AHKScripts\\Neon.exe"], stdin=subprocess.PIPE, close_fds=True)
    procNeon.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 2")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
  
def button_callback14():
    procOmen = subprocess.Popen([".\\AHKScripts\\Omen.exe"], stdin=subprocess.PIPE, close_fds=True)
    procOmen.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 3")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback15():
    procPhoenix = subprocess.Popen([".\\AHKScripts\\Phoenix.exe"], stdin=subprocess.PIPE, close_fds=True)
    procPhoenix.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 4")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback16():
    procRaze = subprocess.Popen([".\\AHKScripts\\Raze.exe"], stdin=subprocess.PIPE, close_fds=True)
    procRaze.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 5")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback17():
    procReyna = subprocess.Popen([".\\AHKScripts\\Reyna.exe"], stdin=subprocess.PIPE, close_fds=True)
    procReyna.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 6")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
 
def button_callback18():
    procSage = subprocess.Popen([".\\AHKScripts\\Sage.exe"], stdin=subprocess.PIPE, close_fds=True)
    procSage.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 7")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME19, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback19():
    procSkye = subprocess.Popen([".\\AHKScripts\\Skye.exe"], stdin=subprocess.PIPE, close_fds=True)
    procSkye.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 8")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME20, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback20():
    procSova = subprocess.Popen([".\\AHKScripts\\Sova.exe"], stdin=subprocess.PIPE, close_fds=True)
    procSova.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 9")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME21, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()

def button_callback21():
    procViper = subprocess.Popen([".\\AHKScripts\\Viper.exe"], stdin=subprocess.PIPE, close_fds=True)
    procViper.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 10")
    processes_to_kill = [
        PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME22
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
     
def button_callback22():
    procYoru = subprocess.Popen([".\\AHKScripts\\Yoru.exe"], stdin=subprocess.PIPE, close_fds=True)
    procYoru.stdin.close()
    CTkMessagebox(title="Info", message="Instalock is set for postion:Column 2 and Row 11")
    processes_to_kill = [
        PROCNAME1, PROCNAME1 , PROCNAME2, PROCNAME3, PROCNAME4, PROCNAME5, PROCNAME6, PROCNAME7, PROCNAME8, PROCNAME9, PROCNAME10, PROCNAME11, PROCNAME12, PROCNAME13, PROCNAME14, PROCNAME15, PROCNAME16, PROCNAME17, PROCNAME18, PROCNAME19, PROCNAME20, PROCNAME21
    ]

    for proc in psutil.process_iter():
        if proc.name() in processes_to_kill:
            proc.kill()
    
def show_info():
    msg = CTkMessagebox(title="Change app format?", message="Do you want to change the app format from 'All agents unlocked' to 'Some agents locked'?", icon="question", option_1="No", option_2="Yes")
    response = msg.get()    
    if response =="Yes":
        procAllAgentsUnlocked = subprocess.Popen([".\\Valorant Instalocker.exe"], stdin=subprocess.PIPE, close_fds=True)
        procAllAgentsUnlocked.stdin.close()
        app.destroy()      
    else:
        return 

def ask_question():
    msg = CTkMessagebox(title="Exit?", message="Do you want to exit the application?", icon="question", option_1="No", option_2="Yes")
    response = msg.get()    
    if response =="Yes":
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] in process_names:
                proc.kill()
        app.destroy()      
    else:
        return 

def ask_question1():
    msg = CTkMessagebox(title="Kill Processes?", message="Do you want to kill all processes.\n\nThis is recommended in case of stuck, lag and bugs", icon="question", option_1="No", option_2="Yes")
    response = msg.get()    
    if response =="Yes":
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] in process_names:
                proc.kill()

optionmenu_var = customtkinter.StringVar(value="Style")

valofont = customtkinter.CTkFont(family="DINNextW05", size=15, weight="bold")
buttonfont = customtkinter.CTkFont(size=24, weight="bold")

button = customtkinter.CTkButton(app, text="1 x 1" ,width=80 ,height=80, command=button_callback1, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=0, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 2" ,width=80 ,height=80, command=button_callback2, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=1, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 3" ,width=80 ,height=80, command=button_callback3, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=2, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 4" ,width=80 ,height=80, command=button_callback4, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=3, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 5" ,width=80 ,height=80, command=button_callback5, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=4, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 6" ,width=80 ,height=80, command=button_callback6, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=5, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 7" ,width=80 ,height=80, command=button_callback7, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=6, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 8" ,width=80 ,height=80, command=button_callback8, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=7, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 9" ,width=80 ,height=80, command=button_callback9, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=8, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 10" ,width=80 ,height=80, command=button_callback10, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=9, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="1 x 11" ,width=80 ,height=80, command=button_callback11, fg_color="#FE4557", font = buttonfont)
button.grid(row=1, column=10, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 1" ,width=80 ,height=80, command=button_callback12, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=0, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 2" ,width=80 ,height=80, command=button_callback13, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=1, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 3" ,width=80 ,height=80, command=button_callback14, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=2, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 4" ,width=80 ,height=80, command=button_callback15, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=3, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 5" ,width=80 ,height=80, command=button_callback16, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=4, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 6" ,width=80 ,height=80, command=button_callback17, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=5, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 7" ,width=80 ,height=80, command=button_callback18, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=6, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 8" ,width=80 ,height=80, command=button_callback19, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=7, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 9" ,width=80 ,height=80, command=button_callback20, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=8, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 10" ,width=80 ,height=80, command=button_callback21, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=9, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="2 x 11" ,width=80 ,height=80, command=button_callback22, fg_color="#FE4557", font = buttonfont)
button.grid(row=2, column=10, padx = 7, pady= 7, sticky = "ew")

button = customtkinter.CTkButton(app, text="Locked Agents?",width=90 ,height=40, command= show_info, fg_color="#FE4557", font= valofont)
button.grid(pady=6, padx=45, row=3,column = 2, columnspan = 3, sticky = "w")

button = customtkinter.CTkButton(app, text="Kill Process",width=90 ,height=40, command= ask_question1, fg_color="#FE4557", font=valofont)
button.grid(pady=6, padx=90, row=3, column=3, columnspan = 3, sticky = "w")

button = customtkinter.CTkButton(app, text="Close",width=90 ,height=40, command= ask_question, fg_color="#FE4557", font=valofont)
button.grid(pady=6, padx=10,row=3, column=5, columnspan = 3, sticky = "w")

button = customtkinter.CTkButton(app, text="Toggle: F1",width=90 ,height=40, fg_color="#FE4557", font=valofont, state = "disabled")
button.grid(pady=6, padx=20, row=3, column=7, columnspan = 3, sticky = "w")

optionmenu = customtkinter.CTkOptionMenu(app,values=["dark", "light", "system"], command=optionmenu_callback, variable=optionmenu_var, width=90 ,height=40, font=valofont, fg_color="#FE4557", button_color="#962834")
optionmenu.grid(padx = 15, row=3, column=6, columnspan = 3, sticky = "w")

app.mainloop()