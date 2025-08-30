import time
import subprocess
from subprocess import call
import os
from terminaltexteffects.effects.effect_slide import Slide
from terminaltexteffects.effects.effect_sweep import Sweep
import random
from tkinter import *

def splash_screen():
    splash = Tk()
    splash.title("Life n' Crime Splash Screen")
    splash.geometry("300x200")
    splash.overrideredirect(True)
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width // 2) - (300 // 2)
    y = (screen_height // 2) - (200 // 2)
    splash.geometry(f"{300}x{200}+{x}+{y}")
    img = PhotoImage(file='launcher_files/splash.png')
    Label(splash, image=img).pack()
    splash.after(3000, lambda: (splash.destroy(), main()))
    splash.mainloop()

def main():
    os.system("title LIFE N' CRIME LAUNCHER") # --> yeah this will only work on windows i cba to figure out how to do this on linux or mac or any other os really so thats a TODO
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("\033[32mINITIALIZING KERNEL")
    print("\033[32m-------------------")
    time.sleep(0.3)
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("\033[32mINITIALIZING KERNEL")
    print("\033[32m==-----------------")
    time.sleep(0.1)
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("\033[32mINITIALIZING KERNEL")
    print("\033[32m======-------------")
    time.sleep(0.2)
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("\033[32mINITIALIZING KERNEL")
    print("\033[32m============------")
    time.sleep(0.3)
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("\033[32mINITIALIZING KERNEL")
    print("\033[32m==================-")
    time.sleep(0.5)
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("\033[32mKERNEL INITIALIZED")
    print("\033[32mPLEASE WAIT....")
    time.sleep(1)
    mainmenu()

def mainmenu():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    effect = Slide("Welcome to ELT OS! CELEBRATING 10 YEARS!")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    effect_two = Sweep("DON'T FORGET TO CHECK OUT THE BRAND NEW ENVRUN PC!!!")
    with effect_two.terminal_output() as terminal:
        for frame in effect_two:
            terminal.print(frame)
    effect_thr = Sweep("Coming soon to all tech stores in ZCity!")
    with effect_thr.terminal_output() as terminal:
        for frame in effect_thr:
            terminal.print(frame)
    print("")
    print("\033[32mType help for commands, and a list of available programs.")
    print("")
    elt_cnsl()
    
def elt_cnsl():
    command = input("\033[32mELT-CNSL:")
    if command == "help":
        help()
    if command == "launch lnc":
        lnc()
    if command == "launch assistant":
        print("\033[32mWe are extremely sorry, but this program is under maintenance, please try again later...")
        elt_cnsl()
    if command == "launch":
        print("\033[32mIncorrect usage of 'launch', use the 'help' command to see the list of available programs...")
        elt_cnsl()
    if command == "headline":
        headline_id = random.randint(1, 10) 
        match headline_id:
            case 1:
                print("\033[0mSHOCK! Popular chips brand pulled from store shelves all across ZCounty!")
            case 2:
                print("\033[0mENVRUN donates another 10M$ to charities. Awarded 'Coporation-of-the-year' award.")
            case 3:
                print("\033[0mENVRUN's new ACE series of equipment SHATTERS competition! \033[36m#sponsored #ad")
            case 4:
                print("\033[0mOver 1,000 ZCounty residents have lost their job to AI, ELT study shows...")
            case 5:
                print("\033[0mFederal Government speeds up the implemntation of AI in all of it's sectors.")
            case 6:
                print("\033[0mWe reviewed the GOLT 911 pistol... It's GREAT! \033[36m#sponsored #ad")
            case 7:
                print("\033[0mToday marks the 5th anniversary since the Atlantic Standard Bank heist... here is what they don't tell you...")
                print("\033[31mELT WEB SECURITY\033[33m MARKS THE ABOVE HEADLINE AS A CONSPIRACY THEORY.")
            case 8:
                print("\033[0mELT study shows that AI has caused over 50% of the creative industry professionals in ZCounty to loose their jobs.")
            case 9:
                print("\033[0m33yo woman found in acid bath. Husband arrested. \033[36m#crime")
            case 10:
                print("\033[0mWatch out for this new scam, FIA warns...")
            case _:
                print("\033[0mError retrieving headline... Please try again later...")
        elt_cnsl()
    if command == "info":
        print("\033[32mWe are extremely sorry, but this program is under maintenance, please try again later...")
        elt_cnsl()
    if command == "shutdown":
        print("\033[32mShutting down...")
        time.sleep(2)
        exit()
    else:
        print("\033[32mIncorrect command, check for typos and try again...")
        elt_cnsl()

def help():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("")
    print("\033[32mHELP MENU:")
    print("\033[32m- Commands:")
    print("\033[32m  + help             - Shows this menu")
    print("\033[32m  + launch [program] - launches a program")
    print("\033[32m  + info             - system information")
    print("\033[32m  + shutdown         - shutdown computer")
    print("\033[32m- Available programs:")
    print("\033[32m  + lnc              - 'life 'n crime computer game'")
    print("\033[32m  + assistant        - 'elt ai assistant powered by General Intelligence'")
    print("\033[32m  + file manager     - 'elt os filemanager'")
    print("")
    print("\033[32mAll ENVRUN affiliated PC's now support the HeadlineFetch™ feature!")
    print("\033[32mType 'headline' in your console, to see a random headline from today's news!")
    print("")
    elt_cnsl()

def lnc():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mLOADING 'LIFE N' CRIME...'")
    print("\033[32mPLEASE WAIT...'")
    time.sleep(2)
    lnc_main()
    
def lnc_main(): 
    print("\033[32mCOPYRIGHT Gas Tank Games 2025")
    print("")
    print("\033[32mTo launch life n' crime story mode type 'story-mode' and hit ENTER.")
    print("\033[32mTo launch life n' crime multiplayer type 'online-mode' and hit ENTER.")
    print("\033[32mTo launch life n' crime mod content type 'mods' and hit ENTER.")
    print("\033[32mFor launch options type 'options' and hit ENTER.")
    print("\033[32mTo see the life n' crime credits type 'credits' and hit ENTER.")
    print("\033[32mTo exit life n' crime type 'exit' and hit ENTER.")
    lnc_console()

def lnc_console():   
    lnc_command = input("LNC-CNSL:")
    if lnc_command == "story-mode":
        print("\033[32mLaunching Life n' Crime Story Mode...")
        time.sleep(1)
        subprocess.run("start files/lnc.exe -iwad gamefiles.ipk3" if os.name == "nt" else "", shell=True) # TODO: WRITE THE LINUX ONE AND MAC ONE
        exit()
    if lnc_command == "online-mode":
        print("\033[32mSorry! This menu is under construction....")
        lnc_console()
    if lnc_command == "mods":
        print("\033[32mSorry! This menu is under construction....")
        input("\033[32mPress any key to return to the Life n' Crime menu...")
        lnc_console()
    if lnc_command == "options":
        print("\033[32mSorry! This menu is under construction....")
        input("\033[32mPress any key to return to the Life n' Crime menu...")
        lnc_console()
    if lnc_command == "credits":
        credits_file = open('credits.txt', 'r')
        credits = credits_file.read()
        print("")
        print("\033[32m" + credits)
        print("")
        credits_file.close()
        lnc_console()
    if lnc_command == "exit":
        mainmenu()
    else:
        print("\033[32mIncorrect command...")
        lnc_console()

#######################################################################################################

splash_screen()