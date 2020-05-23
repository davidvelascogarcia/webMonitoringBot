'''
 * ************************************************************
 *      Program: Web Monitoring Bot
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */
'''


# Libraries
from bs4 import BeautifulSoup
import configparser
import datetime
import os
import platform
import requests
import sys
import time

# Also use (pip) pushbullet.py (apt) python3-notify2 (pip) win10toast


print("**************************************************************************")
print("**************************************************************************")
print("                     Program: Web Monitoring Bot                          ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")

print("")
print("Loading Web Monitoring Bot engine ...")

print("")
print("Initializing webMonitoringBot engine ...")

# Get system configuration
print("")
print("Detecting system and release version ...")
systemPlatform = platform.system()
systemRelease = platform.release()
print(" ")
print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

# Read website URL
print("")
print("Please, introduce website URL to be monitoring")
print("Waiting for input url ...")

webURL = input()

print("")
print("")
print("**************************************************************************")
print("Monitoring URL:")
print("**************************************************************************")
print("")
print("[INFO] Website to be monitorized: "+ str(webURL))

print("")
print("")
print("**************************************************************************")
print("Monitor selection type:")
print("**************************************************************************")
print("")
print("Do you want to monitor full website or a block?")

# Control user input
loopControl=0

while loopControl==0:
    # Selected option
    print("")
    print("Enter number selection: ")
    print("1. Full website")
    print("2. Only a block")

    print("")
    monitorSelection = input()

    if int(monitorSelection)==1 or int(monitorSelection)==2:
        loopControl=1
    else:
        print("")
        print("[ERROR] Sorry option not supported, enter available options ...")

print("")
print("[INFO] You have selected option number: "+ monitorSelection)

# Only a block
if int(monitorSelection)==2:

    print("")
    print("Only a block was selected")

    print("")
    print("")
    print("**************************************************************************")
    print("Selective monitoring:")
    print("**************************************************************************")
    # Selected block type
    print("")
    print("Do you want to analyze by id or other elements like class name or headers ...?")

    # Selected user Control
    loopControlBlockType=0

    while loopControlBlockType==0:
        # Selected option
        print("")
        print("Enter number selection: ")
        print("1. By id")
        print("2. Other elements")

        print("")
        blockTypeSelection = input()

        if int(blockTypeSelection)==1 or int(blockTypeSelection)==2:
            loopControlBlockType=1
        else:
            print("")
            print("[ERROR] Sorry option not supported, enter available options ...")

    # Enter find object name
    print("")
    print("[INFO] You have selected option number "+blockTypeSelection)

    # ID type
    if int(blockTypeSelection)==1:

        print("Please, introduce div id name to monitor")
        print("")
        monitorIDBlock = input()

        print("")
        print("[INFO] Selected block is: "+monitorIDBlock)

    # Other blocks
    if int(blockTypeSelection)==2:

        print("")
        print("[INFO] You have selected other configuration")
        print("")

        # Enter object type
        print("First you have to enter object type, like: section, div, h1, h2 ...")
        monitorOtherBlockObject = input()
        print("[INFO] You have selected: "+ monitorOtherBlockObject)

        # Enter class name
        print("")
        print("Now enter class name...")
        monitorOtherBlockClass = input()
        print("[INFO] You have selected: "+ monitorOtherBlockClass)

# Full website
else:
    print("")
    print("[INFO] Full website was selected")

print("")
print("Initializing monitoring system ...")

# Control first loop
originalBackup = 0

# Backup first run
backupFullWebsiteParsed = "null"
backupAnalyzedIDResults = "null"
backupAnalyzedOtherResults = "null"

# Control tracking
endTracking = 0

print("")
print("")
print("**************************************************************************")
print("Check cicle time:")
print("**************************************************************************")
print("")
print("Please, enter check cicle time in minutes ...")
checkTimeMin = input()
checkTime = int(checkTimeMin)*60

print("")
print("")
print("**************************************************************************")
print("Pushbullet notification service:")
print("**************************************************************************")
# Enable Pushbullet notification
print("")
print("Do you want to add Pushbullet push notifications? By default system notification is enabled.")

# Control loop
loopPushBulletControl = 0

while loopPushBulletControl==0:
    # Selected option
    print("")
    print("Enter your selection y/n: ")

    print("")
    pushbulletSelection = input()

    if str(pushbulletSelection)=="y":

        #import pushbullet
        from pushbullet import Pushbullet

        print("")
        print("[INFO] You have decided to use Pushbullet notification service.")
        print("")
        print("Getting user and token from ../config/authentication.ini ...")

        loopControlFileExists = 0

        while int(loopControlFileExists)==0:
            try:
                # Get autentication data
                print("")
                print("Getting authentication data ...")
                authenticationObject = configparser.ConfigParser()
                authenticationObject.read('../config/authentication.ini')
                authenticationObject.sections()

                userID = authenticationObject['Authentication']['user-id']
                accessToken = authenticationObject['Authentication']['access-token']
                loopControlFileExists = 1

            except:
                print("")
                print("[ERROR] Sorry, athentication.ini not founded, waiting 4 seconds to the next check ...")
                print("")
                time.sleep(4)

        print("[INFO] Data obtained correctly.")
        print("")
        print("Selected user: "+ str(userID))

        print("Configure pushbullet service with user token ...")
        pushbulletNotification = Pushbullet(str(accessToken))

        # Exit loop
        loopPushBulletControl = 1

    elif str(pushbulletSelection)=="n":
        print("")
        print("[INFO] You have decided not use Pushbullet notification service.")

        # Exit loop
        loopPushBulletControl = 1
    else:
        print("")
        print("[ERROR] Sorry option not supported, enter available options ...")

while int(endTracking==0):

    print("")
    print("")
    print("**************************************************************************")
    print("Downloading website:")
    print("**************************************************************************")

    try:
        # Get HTML website
        print("")
        print("Geting "+ webURL +" HTML website ...")
        websiteHTML = requests.get(webURL)
        print("[INFO] Website downloaded")
    except:
        # Website not available
        print("")
        print("[ERROR] Error, website not available.")
        websiteHTML ="null"
        endTracking = 1
        print("")
        print("[INFO] Press any key to close program.")
        print("")
        exitProgram = input()
        sys.exit()


    print("")
    print("")
    print("**************************************************************************")
    print("Analysis website:")
    print("**************************************************************************")
    print("")
    print("Analyzing website ...")

    # **************
    # Full analysis
    # **************
    if int(monitorSelection)==1:

        # Parse HTML web
        print("")
        print("Analyzing full website ...")
        fullWebsiteParsed = BeautifulSoup(websiteHTML.content, 'html.parser')

        # Create backup first run
        if int(originalBackup)==0:
            backupFullWebsiteParsed=fullWebsiteParsed
            originalBackup=1

        # Analyze changes
        else:
            if str(backupFullWebsiteParsed)==str(fullWebsiteParsed):
                print("")
                print("[INFO] Analyzed website has not changes")
            else:
                print("")
                print("")
                print("**************************************************************************")
                print("ALERT:")
                print("**************************************************************************")
                print("")
                print("[INFO] ¡¡¡Changes detected!!!")
                print("")
                print("Sending notifications ...")

                # Push notification system
                if str(systemPlatform)=="Linux":
                    import notify2
                    messageLinux = "webMonitoringBot has detected changes on "+str(webURL)+" website."
                    notify2.init("")
                    notificationLinux = notify2.Notification("[webMonitoringBot] Alert: Changes detected", messageLinux)
                    notificationLinux.show()

                if str(systemPlatform)=="Windows":
                    from win10toast import ToastNotifier
                    messageWindows = "webMonitoringBot has detected changes on "+str(webURL)+" website."
                    notificationWindows = ToastNotifier()
                    notificationWindows.show_toast("[webMonitoringBot] Alert: Changes detected", messageWindows)

                if str(pushbulletSelection)=="y":

                    print("")
                    print("")
                    print("**************************************************************************")
                    print("Send Pushbullet push:")
                    print("**************************************************************************")
                    print("")
                    print("Sending Pushbullet notification ...")
                    pushbulletTitle="[webMonitoringBot] Alert: Changes detected"
                    pushbulletMessage = "webMonitoringBot has detected changes on "+str(webURL)+" website."
                    pushbulletRequest = pushbulletNotification.push_note(str(pushbulletTitle), str(pushbulletMessage))
                    print("")
                    print("[INFO] Push sent")
                    time.sleep(2)

                endTracking = 1

    # ***************
    # Block analysis
    # ***************
    else:

        # Parse HTML website
        print("")
        print("Analyzing block ...")
        blockWebsiteParsed = BeautifulSoup(websiteHTML.content, 'html.parser')

        #************
        # Find by ID
        # ***********
        if int(blockTypeSelection)==1:

            try:
                # Find id class name
                analyzedIDResults = blockWebsiteParsed.find(id=str(monitorIDBlock))

                print("")
                print("")
                print("**************************************************************************")
                print("Analysis results:")
                print("**************************************************************************")

                # Print analyzedResult
                print("")
                print("[RESULTS] Request results: ")
                print(analyzedIDResults.prettify())

            except:
                # Website not available
                print("")
                print("[ERROR] Error, ID not founded.")
                endTracking = 1
                print("")
                print("Press any key to close program.")
                print("")
                exitProgram = input()
                sys.exit()

            # Create backup first run
            if int(originalBackup)==0:
                backupAnalyzedIDResults=analyzedIDResults
                originalBackup=1

            # Analyze changes
            else:
                if str(backupAnalyzedIDResults)==str(analyzedIDResults):
                    print("")
                    print("Analyzed block has not changes")
                else:

                    print("")
                    print("")
                    print("**************************************************************************")
                    print("ALERT:")
                    print("**************************************************************************")
                    print("")
                    print("[INFO] ¡¡¡Changes detected!!!")
                    print("")
                    print("Sending notifications ...")

                    # Push notification system
                    if str(systemPlatform)=="Linux":
                        import notify2
                        messageLinux = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorIDBlock)+" ID block."
                        notify2.init("")
                        notificationLinux = notify2.Notification("[webMonitoringBot] Alert: Changes detected", messageLinux)
                        notificationLinux.show()

                    if str(systemPlatform)=="Windows":
                        from win10toast import ToastNotifier
                        messageWindows = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorIDBlock)+" ID block."
                        notificationWindows = ToastNotifier()
                        notificationWindows.show_toast("[webMonitoringBot] Alert: Changes detected", messageWindows)

                    if str(pushbulletSelection)=="y":

                        print("")
                        print("")
                        print("**************************************************************************")
                        print("Send Pushbullet push:")
                        print("**************************************************************************")
                        print("")
                        print("Sending Pushbullet notification ...")
                        pushbulletTitle="[webMonitoringBot] Alert: Changes detected"
                        pushbulletMessage = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorIDBlock)+" ID block."
                        pushbulletRequest = pushbulletNotification.push_note(str(pushbulletTitle), str(pushbulletMessage))
                        print("")
                        print("[INFO] Push sent")
                        time.sleep(2)

                    endTracking = 1

        # ***************************
        # Find by other configuration
        # ***************************
        else:

            try:
                analyzedOtherResults = blockWebsiteParsed.find(str(monitorOtherBlockObject), class_=str(monitorOtherBlockClass))

                print("")
                print("")
                print("**************************************************************************")
                print("Analysis results:")
                print("**************************************************************************")
                print("")
                print("[RESULTS] Request results:")
                print(str(analyzedOtherResults.text))

            except:
                # Website not available
                print("")
                print("[ERROR] Error, elements not founded.")
                endTracking = 1
                print("")
                print("Press any key to close program.")
                print("")
                exitProgram = input()
                sys.exit()

            # Create backup first run
            if int(originalBackup)==0:
                backupAnalyzedOtherResults=analyzedOtherResults
                originalBackup=1

            # Analyze changes
            else:
                if str(backupAnalyzedOtherResults)==str(analyzedOtherResults):
                    print("")
                    print("[INFO] Analyzed block has not changes")
                else:


                    print("")
                    print("")
                    print("**************************************************************************")
                    print("ALERT:")
                    print("**************************************************************************")
                    print("")
                    print("[INFO] ¡¡¡Changes detected!!!")
                    print("")
                    print("Sending notifications ...")

                    # Push notification system
                    if str(systemPlatform)=="Linux":
                        import notify2
                        messageLinux = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorOtherBlockObject)+" object "+ monitorOtherBlockClass+" class."
                        notify2.init("")
                        notificationLinux = notify2.Notification("[webMonitoringBot] Alert: Changes detected", messageLinux)
                        notificationLinux.show()

                    if str(systemPlatform)=="Windows":
                        from win10toast import ToastNotifier
                        messageWindows = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorOtherBlockObject)+" object "+ monitorOtherBlockClass+" class."
                        notificationWindows = ToastNotifier()
                        notificationWindows.show_toast("[webMonitoringBot] Alert: Changes detected", messageWindows)

                    if str(pushbulletSelection)=="y":

                        print("")
                        print("")
                        print("**************************************************************************")
                        print("Send Pushbullet push:")
                        print("**************************************************************************")
                        print("")
                        print("Sending Pushbullet notification ...")
                        pushbulletTitle="[webMonitoringBot] Alert: Changes detected"
                        pushbulletMessage = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorOtherBlockObject)+" object "+ monitorOtherBlockClass+" class."
                        pushbulletRequest = pushbulletNotification.push_note(str(pushbulletTitle), str(pushbulletMessage))
                        print("")
                        print("[INFO] Push sent")
                        time.sleep(2)

                    endTracking = 1

    print("Waiting "+ str(checkTime) +" seconds to next check ...")
    time.sleep(checkTime)

    print("")
    print("")
    print("**************************************************************************")
    print("Monitoring finished:")
    print("**************************************************************************")
    print("")
    print("[INFO] Website analyzed and monitorig done correctly.")
