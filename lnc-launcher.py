import time
import subprocess
import os
import sys
from terminaltexteffects.effects.effect_slide import Slide
from terminaltexteffects.effects.effect_sweep import Sweep
from terminaltexteffects.effects.effect_print import Print
import random
from tkinter import *
from Color_Console import *

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
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("\033[32mCOPYRIGHT ELT, Inc. 1998-2008")
    print("\033[32mINITIALIZING KERNEL")
    load_effect = Print("===================")
    with load_effect.terminal_output() as terminal:
        for frame in load_effect:
            terminal.print(frame)
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
    if command.lower() == "help":
        help()
    if command.lower() == "launch lnc":
        lnc()
    if command.lower() == "launch assistant":
        print("\033[32mWe are extremely sorry, but this program is under maintenance, please try again later...")
        elt_cnsl()
    if command.lower() == "launch":
        print("\033[32mIncorrect usage of 'launch', use the 'help' command to see the list of available programs...")
        elt_cnsl()
    if command.lower() == "headline":
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
    if command.lower() == "info":
        print("\033[32mWe are extremely sorry, but this program is under maintenance, please try again later...")
        elt_cnsl()
    if command.lower() == "shutdown":
        print("\033[32mShutting down...")
        time.sleep(1)
        exit()
    if command.lower() == "restart":
        print("\033[32mRestarting...")
        time.sleep(1)
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        time.sleep(2)
        main()
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
    print("\033[32m  + restart          - restart computer")
    print("\033[32m- Available programs:")
    print("\033[32m  + lnc              - 'life 'n crime computer game'")
    print("\033[32m  + youtopia         - 'the most modern edutainment game of the 90's'")
    print("\033[32m  + assistant        - 'elt ai assistant powered by General Intelligence'")
    print("\033[32m  + file manager     - 'elt os filemanager'")
    print("")
    print("\033[35mAll ENVRUN affiliated PC's now support the \033[33mHeadlineFetch™\033[35m feature!")
    print("\033[35mType 'headline' in your console, to see a random headline from today's news!")
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
    print("\033[32mThis version of the launcher is designed to work with LIFE N' CRIME DEMO 1")
    print("")
    print("\033[32mTo launch life n' crime story mode type 'story-mode' and hit ENTER.")
    print("\033[32mTo launch life n' crime multiplayer type 'online-mode' and hit ENTER.")
    print("\033[32mTo launch life n' crime mod content type 'mods' and hit ENTER.")
    print("\033[32mTo setup/configure the life n' crime gamejolt integration type 'gamejolt' and hit ENTER.")
    print("\033[32mFor launch options type 'options' and hit ENTER.")
    print("\033[32mTo see the life n' crime credits type 'credits' and hit ENTER.")
    print("\033[32mTo exit life n' crime type 'exit' and hit ENTER.")
    print("")
    print("\033[32mPlease note that when playing with mods loaded, Gamejolt integration is disabled...")
    print("\033[32mAlso, multiplayer is pretty bare-bones as of now, missing tons of planned maps, modes and most of the GameJolt integration stuff...")
    print("")
    lnc_console()

def lnc_console():   
    lnc_command = input("LNC-CNSL:")
    if lnc_command.lower() == "story-mode":
        print("\033[32mLaunching Life n' Crime Story Mode...")
        time.sleep(1)
        extras = ""
        if os.path.exists("lnc_gj_credts"):
            if os.path.getsize("lnc_gj_credts") > 0:
                print("\033[32mPlugging gamejolt integration...")
                extras = extras + " -gamejolt"
        subprocess.run("start files/lnc.exe -iwad gamefiles.ipk3 -is_launcher_launched +multiplayer_current_mode 0 +r_deathcamera false" + extras if os.name == "nt" else "", shell=True) # TODO: WRITE THE LINUX ONE AND MAC ONE
        # if ur making ur own custom launcher u need to also use the -is_launcher_launched arguement and you can bite me about that...
        exit()
    if lnc_command.lower() == "online-mode":
        print("\033[32mLaunching life n' crime online launcher...")
        subprocess.run("start lnc_mp.exe" if os.name == "nt" else "", shell=False) # TODO: WRITE THE LINUX ONE AND MAC ONE
        lnc_console()
    if lnc_command.lower() == "mods":
        print("\033[32mSorry! This menu is under construction....")
        input("\033[32mPress any key to return to the Life n' Crime menu...")
        lnc_console()
    if lnc_command.lower() == "gamejolt":
        gj_want = input("\033[32mDo you want Life n' Crime to integrate with your GameJolt Account (Y/N/Cancel):")
        if gj_want.lower() == "y":
            print("\033[32mGas Tank Games is not affiliated with GameJolt in any way, shape or form.")
            gj_username = input("\033[32mEnter your GameJolt username:")
            gj_token = input("\033[32mEnter your GameJolt game token:")
            with open("lnc_gj_credts", "w") as gj_creds:
                gj_creds.truncate(0)
                gj_creds.write(gj_username +"\n")
                gj_creds.write(gj_token)
                gj_creds.close()
            print("\033[32mGameJolt settings updated!")
            lnc_console()
        if gj_want.lower() == "n":
            with open("lnc_gj_credts", "r+") as gj_creds:
                if os.path.exists("lnc_gj_credts"):
                    gj_creds.truncate(0)
                    gj_creds.close()
            lnc_console()
        else:
            lnc_console()
    if lnc_command.lower() == "options":
        print("\033[32mSorry! This menu is under construction....")
        input("\033[32mPress any key to return to the Life n' Crime menu...")
        lnc_console()
    if lnc_command.lower() == "credits":
        credits_file = open('credits.txt', 'r')
        credits = credits_file.read()
        print("")
        print("\033[32m" + credits)
        print("")
        credits_file.close()
        lnc_console()
    if lnc_command.lower() == "exit":
        mainmenu()
    else:
        print("\033[32mIncorrect command...")
        lnc_console()

#######################################################################################################

if os.name == 'nt':
    os.system("title LIFE N' CRIME LAUNCHER")
else:
    sys.stdout.write("\x1b]2;LIFE N' CRIME LAUNCHER\x07")
color(bg = "black")
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
print("!!!DO NOT CLOSE THIS WINDOW!!!!")
splash_screen()