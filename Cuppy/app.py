#Saucy22 on GitHub 2024-2025

#Importing built-in libraries at runtime
import os, time, io
from operator import truediv

#Variables
isUbuntu = False
isFedora = False
isDNF5 = False
isArch = False

#Checking for windows, if windows is found the program will give an error and quit
if os.name in ("nt", "dos", "ce"):
    os.system('CLS')
    print('This program is meant to be run on linux. This program is not compatible with Mac or Windows.')
    print('This program will quit in 10 seconds')
    time.sleep(10)
    quit()

#Welcome
os.system('clear')

print('Welcome to cupd! (Calebs Updater)')
time.sleep(1)
print('What distro do you use?')

#Distro selection
#TO DO: Shave off a second or two by adding an automated OS checker
while True:
    print('Press 1 for Ubuntu/Linux Mint, 2 for Fedora, or 3 for Arch/Endeavouros')
    distro = input()

    if distro == '1':
        isUbuntu = True
        break
    elif distro == '2':
        isFedora = True
        while True:
            print("Would you like to use dnf5? y/N")
            dnf5 = input()
            if dnf5 == 'Y' or if dnf5 == 'y':
                isDNF5 = True
                break
            else:
                isDNF5 = False
                break
        break
    elif distro == '3':
        isArch = True
        break
    else:
        os.system('clear')
        print('Error: cant recognise command, please try again')
        
#System Updater
os.system('clear')
print('Updating your system')

if isUbuntu == True:
    os.system('sudo apt update && sudo apt upgrade; pacstall -U; flatpak update; snap refresh')
    os.system('clear')
    print('Successfully updated your system! You can now close this window.')
elif isFedora == True:
    if isDNF5 == True:
        os.system('sudo dnf5 upgrade; flatpak update; snap refresh')
        os.system('clear')
        print('Successfully updated your system! You can now close this window.')
    else:
        os.system('sudo dnf upgrade; flatpak update; snap refresh')
        os.system('clear')
        print('Successfully updated your system! You can now close this window.')
elif isArch == True:
    os.system('yay; flatpak update; snap refresh; pacman -Syu')
    os.system('clear')
    print('Successfully updated your system! You can now close this window.')


