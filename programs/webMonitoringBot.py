'''
 * ************************************************************
 *      Program: Web Monitoring Bot
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
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

print("")
print("Loading Web Monitoring Bot engine ...")
print("")

print("")
print("Initializing webMonitoringBot engine ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("**************************************************************************")
print("URL monitoring:")
print("**************************************************************************")
print("")

# Read website URL
print("")
print("[INFO] Please, introduce website URL to be monitoring")
print("")
print("[INFO] Waiting for input url ...")
print("")

webURL = input()

print("")
print("**************************************************************************")
print("Monitoring URL:")
print("**************************************************************************")
print("")
print("[INFO] Website to be monitorized: " + str(webURL))

print("")
print("**************************************************************************")
print("Monitor selection type:")
print("**************************************************************************")
print("")
print("Do you want to monitor full website or a block?")
print("")

# Control user input
loopControl = 0

while int(loopControl) == 0:

    # Selected option
    print("")
    print("Enter number selection: ")
    print("1. Full website")
    print("2. Only a block")
    print("")

    monitorSelection = input()

    if int(monitorSelection) == 1 or int(monitorSelection) == 2:
        loopControl=1
    else:
        print("")
        print("[ERROR] Sorry option not supported, enter available options ...")
        print("")

print("")
print("[INFO] You have selected option number: " + str(monitorSelection))
print("")

# Only a block
if int(monitorSelection) == 2:

    print("")
    print("[INFO] Only a block was selected.")
    print("")


    print("")
    print("**************************************************************************")
    print("Selective monitoring:")
    print("**************************************************************************")
    print("")
    # Selected block type
    print("")
    print("Do you want to analyze by id or other elements like class name or headers?")
    print("")

    # Selected user Control
    loopControlBlockType = 0

    while int(loopControlBlockType) == 0:

        # Selected option
        print("")
        print("Enter number selection: ")
        print("1. By id")
        print("2. Other elements")
        print("")

        blockTypeSelection = input()

        if int(blockTypeSelection) == 1 or int(blockTypeSelection) == 2:
            loopControlBlockType = 1
        else:
            print("")
            print("[ERROR] Sorry option not supported, enter available options ...")
            print("")

    # Enter find object name
    print("")
    print("[INFO] You have selected option number " + str(blockTypeSelection))
    print("")

    # ID type
    if int(blockTypeSelection) == 1:

        print("")
        print("Please, introduce div id name to monitor:")
        print("")

        monitorIDBlock = input()

        print("")
        print("[INFO] Selected block is: " + str(monitorIDBlock))
        print("")

    # Other blocks
    if int(blockTypeSelection) == 2:

        print("")
        print("[INFO] You have selected other configuration.")
        print("")

        # Enter object type
        print("")
        print("First you have to enter object type, like: section, div, h1, h2 ...")
        print("")

        monitorOtherBlockObject = input()

        print("")
        print("[INFO] You have selected: " + str(monitorOtherBlockObject))
        print("")

        # Enter class name
        print("")
        print("Now enter class name:")
        print("")

        monitorOtherBlockClass = input()

        print("")
        print("[INFO] You have selected: " + str(monitorOtherBlockClass))
        print("")

# Full website
else:
    print("")
    print("[INFO] Full website was selected.")
    print("")

print("")
print("Initializing monitoring system ...")
print("")

# Control first loop
originalBackup = 0

# Backup first run
backupFullWebsiteParsed = "null"
backupAnalyzedIDResults = "null"
backupAnalyzedOtherResults = "null"

# Control tracking
endTracking = 0


print("")
print("**************************************************************************")
print("Check cicle time:")
print("**************************************************************************")
print("")
print("Please, enter check cicle time in minutes ...")
print("")

checkTimeMin = input()
checkTime = int(checkTimeMin)*60

# Enable Pushbullet notification service
print("")
print("**************************************************************************")
print("Pushbullet notification service:")
print("**************************************************************************")
print("")
print("Do you want to add Pushbullet push notifications? By default system notification is enabled.")
print("")

# Control loop
loopPushBulletControl = 0

while int(loopPushBulletControl) == 0:

    # Selected option
    print("")
    print("Enter your selection y/n: ")
    print("")

    pushbulletSelection = input()

    if str(pushbulletSelection) == "y":

        #import pushbullet
        from pushbullet import Pushbullet

        print("")
        print("[INFO] You have decided to use Pushbullet notification service.")
        print("")
        print("Getting user and token from ../config/authentication.ini ...")
        print("")

        loopControlFileExists = 0

        while int(loopControlFileExists) == 0:
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

        print("")
        print("[INFO] Data obtained correctly.")
        print("")
        print("Selected user: " + str(userID))
        print("")

        print("")
        print("Configure pushbullet service with user token ...")
        print("")

        pushbulletNotification = Pushbullet(str(accessToken))

        # Exit loop
        loopPushBulletControl = 1

    elif str(pushbulletSelection) == "n":

        print("")
        print("[INFO] You have decided not use Pushbullet notification service.")
        print("")

        # Exit loop
        loopPushBulletControl = 1

    else:
        print("")
        print("[ERROR] Sorry option not supported, enter available options ...")
        print("")

while int(endTracking) == 0:

    print("")
    print("**************************************************************************")
    print("Downloading website:")
    print("**************************************************************************")
    print("")

    try:
        # Get HTML website
        print("")
        print("Getting "+ webURL +" HTML website at " + str(datetime.datetime.now()) + " ...")
        print("")

        websiteHTML = requests.get(webURL)

        print("")
        print("[INFO] Website downloaded correctly.")
        print("")

    except:
        # Website not available
        print("")
        print("[ERROR] Error, website not available.")
        print("")

        websiteHTML = "null"
        endTracking = 1

        print("")
        print("[INFO] Press any key to close program.")
        print("")

        exitProgram = input()
        sys.exit()

    print("")
    print("**************************************************************************")
    print("Analysis website:")
    print("**************************************************************************")
    print("")
    print("[INFO] Analyzing website at " + str(datetime.datetime.now()) + " ...")
    print("")

    # **************
    # Full analysis
    # **************
    if int(monitorSelection)==1:

        # Parse HTML web
        print("")
        print("Analyzing full website ...")
        print("")

        fullWebsiteParsed = BeautifulSoup(websiteHTML.content, 'html.parser')

        # Create backup first run
        if int(originalBackup) == 0:
            backupFullWebsiteParsed = fullWebsiteParsed
            originalBackup = 1

        # Analyze changes
        else:
            if str(backupFullWebsiteParsed) == str(fullWebsiteParsed):

                print("")
                print("[INFO] Analyzed website has not changes at " + str(datetime.datetime.now()) + ".")
                print("")

            else:
                print("")
                print("**************************************************************************")
                print("ALERT:")
                print("**************************************************************************")
                print("")
                print("[INFO] ¡¡¡Changes detected!!!")
                print("")
                print("Sending notifications ...")
                print("")

                # Push notification system
                if str(systemPlatform) == "Linux":

                    import notify2
                    messageLinux = "webMonitoringBot has detected changes on "+str(webURL)+" website."
                    notify2.init("")
                    notificationLinux = notify2.Notification("[webMonitoringBot] Alert: Changes detected", messageLinux)
                    notificationLinux.show()

                if str(systemPlatform) == "Windows":

                    from win10toast import ToastNotifier
                    messageWindows = "webMonitoringBot has detected changes on "+str(webURL)+" website."
                    notificationWindows = ToastNotifier()
                    notificationWindows.show_toast("[webMonitoringBot] Alert: Changes detected", messageWindows)

                if str(pushbulletSelection) == "y":

                    print("")
                    print("**************************************************************************")
                    print("Send Pushbullet push:")
                    print("**************************************************************************")
                    print("")
                    print("Sending Pushbullet notification ...")
                    print("")

                    pushbulletTitle="[webMonitoringBot] Alert: Changes detected"
                    pushbulletMessage = "webMonitoringBot has detected changes on " + str(webURL) + " website."
                    pushbulletRequest = pushbulletNotification.push_note(str(pushbulletTitle), str(pushbulletMessage))

                    print("")
                    print("[INFO] Push sent")
                    print("")
                    time.sleep(2)

                endTracking = 1

    # ***************
    # Block analysis
    # ***************
    else:

        # Parse HTML website
        print("")
        print("Analyzing block ...")
        print("")

        blockWebsiteParsed = BeautifulSoup(websiteHTML.content, 'html.parser')

        #************
        # Find by ID
        # ***********
        if int(blockTypeSelection) == 1:

            try:
                # Find id class name
                analyzedIDResults = blockWebsiteParsed.find(id=str(monitorIDBlock))

                print("")
                print("**************************************************************************")
                print("Analysis results:")
                print("**************************************************************************")
                print("")

                # Print analyzedResult
                print("")
                print("[RESULTS] Request results: ")
                print("")
                print(analyzedIDResults.prettify())

            except:
                # Website not available
                print("")
                print("[ERROR] Error, ID not founded.")
                print("")
                endTracking = 1

                print("")
                print("Press any key to close program.")
                print("")

                exitProgram = input()
                sys.exit()

            # Create backup first run
            if int(originalBackup) == 0:
                backupAnalyzedIDResults = analyzedIDResults
                originalBackup = 1

            # Analyze changes
            else:
                if str(backupAnalyzedIDResults) == str(analyzedIDResults):

                    print("")
                    print("Analyzed block has not changes at " + str(datetime.datetime.now()) + ".")
                    print("")

                else:

                    print("")
                    print("**************************************************************************")
                    print("ALERT:")
                    print("**************************************************************************")
                    print("")
                    print("[INFO] ¡¡¡Changes detected!!!")
                    print("")
                    print("Sending notifications ...")
                    print("")

                    # Push notification system
                    if str(systemPlatform) == "Linux":

                        import notify2
                        messageLinux = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorIDBlock)+" ID block."
                        notify2.init("")
                        notificationLinux = notify2.Notification("[webMonitoringBot] Alert: Changes detected", messageLinux)
                        notificationLinux.show()

                    if str(systemPlatform) == "Windows":

                        from win10toast import ToastNotifier
                        messageWindows = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorIDBlock)+" ID block."
                        notificationWindows = ToastNotifier()
                        notificationWindows.show_toast("[webMonitoringBot] Alert: Changes detected", messageWindows)

                    if str(pushbulletSelection) == "y":

                        print("")
                        print("**************************************************************************")
                        print("Send Pushbullet push:")
                        print("**************************************************************************")
                        print("")
                        print("Sending Pushbullet notification ...")
                        print("")

                        pushbulletTitle="[webMonitoringBot] Alert: Changes detected"
                        pushbulletMessage = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorIDBlock)+" ID block."
                        pushbulletRequest = pushbulletNotification.push_note(str(pushbulletTitle), str(pushbulletMessage))

                        print("")
                        print("[INFO] Push sent.")
                        print("")

                        time.sleep(2)

                    endTracking = 1

        # ***************************
        # Find by other configuration
        # ***************************
        else:

            try:
                analyzedOtherResults = blockWebsiteParsed.find(str(monitorOtherBlockObject), class_=str(monitorOtherBlockClass))

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
                print("")

                endTracking = 1

                print("")
                print("Press any key to close program.")
                print("")

                exitProgram = input()
                sys.exit()

            # Create backup first run
            if int(originalBackup) == 0:
                backupAnalyzedOtherResults = analyzedOtherResults
                originalBackup = 1

            # Analyze changes
            else:
                if str(backupAnalyzedOtherResults) == str(analyzedOtherResults):
                    print("")
                    print("[INFO] Analyzed block has not changes.")
                    print("")

                else:

                    print("")
                    print("**************************************************************************")
                    print("ALERT:")
                    print("**************************************************************************")
                    print("")
                    print("[INFO] ¡¡¡Changes detected!!!")
                    print("")
                    print("Sending notifications ...")
                    print("")

                    # Push notification system
                    if str(systemPlatform) == "Linux":

                        import notify2
                        messageLinux = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorOtherBlockObject)+" object "+ monitorOtherBlockClass+" class."
                        notify2.init("")
                        notificationLinux = notify2.Notification("[webMonitoringBot] Alert: Changes detected", messageLinux)
                        notificationLinux.show()

                    if str(systemPlatform) == "Windows":

                        from win10toast import ToastNotifier
                        messageWindows = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorOtherBlockObject)+" object "+ monitorOtherBlockClass+" class."
                        notificationWindows = ToastNotifier()
                        notificationWindows.show_toast("[webMonitoringBot] Alert: Changes detected", messageWindows)

                    if str(pushbulletSelection) == "y":

                        print("")
                        print("**************************************************************************")
                        print("Send Pushbullet push:")
                        print("**************************************************************************")
                        print("")
                        print("Sending Pushbullet notification ...")
                        print("")

                        pushbulletTitle="[webMonitoringBot] Alert: Changes detected"
                        pushbulletMessage = "webMonitoringBot has detected changes on "+str(webURL)+" website in "+ str(monitorOtherBlockObject)+" object "+ monitorOtherBlockClass+" class."
                        pushbulletRequest = pushbulletNotification.push_note(str(pushbulletTitle), str(pushbulletMessage))

                        print("")
                        print("[INFO] Push sent.")
                        print("")
                        time.sleep(2)

                    endTracking = 1
    print("")
    print("[INFO] Waiting "+ str(checkTime) + " seconds to next check ...")
    print("")

    time.sleep(checkTime)

    print("")
    print("")
    print("**************************************************************************")
    print("Monitoring finished:")
    print("**************************************************************************")
    print("")
    print("[INFO] Website analyzed and monitorig done correctly.")
    print("")
