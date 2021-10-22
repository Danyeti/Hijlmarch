import pyautogui as pyautogui
import win32gui, win32con, time, keyboard, os
from threading import Thread
from PIL import Image
import pyttsx3, time, pygame.mixer, pygame.time, mixer, bs4, regex, requests
from playsound import playsound
import pygame
pygame.init()
pygame.mixer.init()

EldrolodDLCActive = False

#Eldrolod DLC Validation
if os.path.exists('G:\Hijlmarch I - The Queen Of Validor\EldrolodDLC.py'):
    from EldrolodDLC import CODE
    code = input("Your Activation Code For The Eldrolod DLC?: ")
    if code == CODE:
        EldrolodDLCActive = True
        print("okay, carry on")
        
    if code != CODE:
        print("You have not entred a valid code, please restart and try again")
        time.sleep(3)
        quit()
mixer = pygame.mixer
mixer.init()
tada = mixer.Sound('assets/music/2019-07-29_-_Elven_Forest_-_FesliyanStudios.com_-_David_Renda.mp3')
tada.set_volume(0.02)
run = True
def func1():
    pyautogui.alert(text='(IMPORTANT) Check files for other resorces \n Files: \n Hijlmarch.jpg = Full Map \n *Other settings/files*', title='Hijlmarch I: The Queen Of Validor', button ='EXIT')#!# Add files w/ info and game name

    
def func2():
    time.sleep(1)
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
    while True:
        tada.play()

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()


while run:
    ##
    runLoop = 0
    choiceValidation = 0
    ##
    time.sleep(1)
    if runLoop != 1:
        if EldrolodDLCActive == False:
            while choiceValidation <1:
                ok = pyautogui.prompt(text="During the story, there will be options e.g.'what is your gender? [1]Female [2]Male' you will answer these using the numbers that match your answer. Do you understand? [1]Yes [2]Of course", title='Hijlmarch I: The Queen Of Validor' , default='')
                runLoop = 0
                if ok == "1" or ok == "2":
                    choiceValidation = 1
                if ok < "1" or ok > "2":
                    print("Invalid responce")
                    choiceValidation = 0
    time.sleep(1)

    if runLoop != 1:
        if EldrolodDLCActive == False:
            choiceValidation = 0
            while choiceValidation < 1:
                choice_0 = pyautogui.prompt(text="'It's dark in this room and i don't like it. My father, King Val, won't let me take his place when he dies just because I'm a woman, I'll show him what a woman can do when i run away. Now, how do I escape this room before his servant comes to collect me?' [1]Escape from the window [2]Run out the door", title='Hijlmarch I: The Queen Of Validor' , default='')
                runLoop = 0
                if choice_0 == "1" or choice_0 == "2":
                    choiceValidation = 1
                if choice_0 <"1" or choice_0 > "3":
                    print("Invalid responce")
                    choiceValidation = 0
                if choice_0 == "1":
                    choice_1 = pyautogui.prompt(text="Luckily I'm on ground level, I just have to find a way to open the window. [1]Smash through [2]Pick the lock", title="Hijlmarch I: The Queen Of Validor", default="")
                    if choice_1 == "1" or choice_1 == "2":
                        choiceValidation = 1
                    if choice_1 <"1" or choice_1 > "3":
                        print("Invalid responce")
                        choiceValidation = 0
                    if choice_1 == "1":
                        choice_2 = pyautogui.prompt(text='You smash through the window, causing such a noise that you alert the guards, what do you do? [1]Hide outside away from them [2]Act like it was a robbery', title='Hijlmarch I: The Queen Of Validor' , default='')
                        if choice_2 == "1" or choice_2 == "2":
                            choiceValidation = 1
                        if choice_2 <"1" or choice_2 > "3":
                            print("Invalid responce")
                            choiceValidation = 0
                        if choice_2 == "1":
                            pyautogui.alert(text="You successfully hide away from the guards but they know that you've escaped. 'Theres a small farm  village near by, I'll go there, at least i have my sword to protect me through this forest.'", title='Hijlmarch I: The Queen Of Validor' , button='Next')#LEFT OFF
                                                   
                        if choice_2 <"1" or choice_2 > "3":
                            print("Invalid responce")
                            choiceValidation = 0

                        if choice_2 == "2":
                            pyautogui.alert(text="The guards unlock and open your door to find you on your bed scared.You say 'Someone smashed my window! They stole my jewlery! Help!' The guards take you to King Val to see what must happen about this.\n The King says 'For your own protection, princess, you must go to validor farms and live with a resedent there for a while until we find the theif. You get guided out the castle and are given a horse to ride and you keep your sword  for protection through the coming forest.' ", title='Hijlmarch I: The Queen Of Validor' , button='Next')
                            pyautogui.prompt(text="", title='Hijlmarch I: The Queen Of Validor' , default='')#!# continue to validor
                            
                    if choice_1 == "2":
                        pyautogui.alert(text="You take the lock pick from your pocket and attempt to pick the lock....", title='Hijlmarch I: The Queen Of Validor' , button='Next')
                        pyautogui.alert(text="You picked the lock successfully!", title='Hijlmarch I: The Queen Of Validor' , button='Next')
                        pyautogui.alert(text="You quietly open the window and sneak out. 'Okay, i remember the way to validor farms, it's not far, as long as i keep my sword out, I'll be fine throughout this coming forest.", title='Hijlmarch I: The Queen Of Validor' , button='Next')
            
                if choice_0 == "2":
                    pyautogui.alert(text="You attempt to open the door, but it's locked...", title="Hijlmarch I: The Queen Of Validor", button="Next")
                    choiceValidation = 0
            
        choice_0 = pyautogui.prompt(text="", title="Hijlmarch I: The Queen Of Validor", default="")
            #ELDROLOD
        if EldrolodDLCActive == True:
            Choice_0 = pyautogui.prompt(text="", title='Hijlmarch I: The Queen Of Validor' , default='')
            runLoop = 0
        
