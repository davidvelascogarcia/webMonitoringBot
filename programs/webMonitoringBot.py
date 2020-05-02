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
print("Starting system...")

print("")
print("Loading Web Monitoring Bot engine...")

print("")
print("Initializing webMonitoringBot engine...")

# Get system configuration
print("")
print("Detecting system and release version...")
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
print("Website to be monitorized: "+ webURL)

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
        print("Sorry option not supported, enter available options ...")

print("")
print("You have selected option number "+ monitorSelection)

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
            print("Sorry option not supported, enter available options ...")

    # Enter find object name
    print("")
    print("You have selected option number "+blockTypeSelection)

    # ID type
    if int(blockTypeSelection)==1:

        print("Please, introduce div id name to monitor")
        print("")
        monitorIDBlock = input()

        print("")
        print("Selected block is: "+monitorIDBlock)

    # Other blocks
    if int(blockTypeSelection)==2:

        print("")
        print("You have selected other configuration")
        print("")

        # Enter object type
        print("First you have to enter object type, like: section, div, h1, h2 ...")
        monitorOtherBlockObject = input()
        print("You have selected: "+ monitorOtherBlockObject)

        # Enter class name
        print("")
        print("Now enter class name...")
        monitorOtherBlockClass = input()
        print("You have selected: "+ monitorOtherBlockClass)

# Full website
else:
    print("")
    print("Full website was selected")

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
        print("You have decided to use Pushbullet notification service.")
        print("")
        print("Getting user and token from ../config/authentication.ini ...")

        # Get autentication data
        print("")
        print("Getting authentication data ...")
        authenticationObject = configparser.ConfigParser()
        authenticationObject.read('../config/authentication.ini')
        authenticationObject.sections()

        userID = authenticationObject['Authentication']['user-id']
        accessToken = authenticationObject['Authentication']['access-token']

        print("Data obtained correctly.")
        print("")
        print("Selected user: "+ str(userID))

        print("Configure pushbullet service with user token ...")
        pushbulletNotification = Pushbullet(str(accessToken))

        # Exit loop
        loopPushBulletControl = 1

    elif str(pushbulletSelection)=="n":
        print("")
        print("You have decided not use Pushbullet notification service.")

        # Exit loop
        loopPushBulletControl = 1
    else:
        print("")
        print("Sorry option not supported, enter available options ...")

while int(endTracking==0):

    print("")
    print("")
    print("**************************************************************************")
    print("Downloading website:")
    print("**************************************************************************")
    # Get HTML website
    print("")
    print("Geting "+ webURL +" HTML website ...")
    websiteHTML = requests.get(webURL)
    print("Website downloaded")

    print("")
    print("")
    print("**************************************************************************")
    print("Analysis website:")
    print("**************************************************************************")
    print("")
    print("Analyzing website ...")

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
                print("Analyzed website has not changes")
            else:
                print("")
                print("")
                print("**************************************************************************")
                print("ALERT:")
                print("**************************************************************************")
                print("")
                print("¡¡¡Changes detected!!!")
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
                    print("Push sent")
                    time.sleep(2)

                endTracking = 1


    else:

        # Parse HTML website
        print("")
        print("Analyzing block ...")
        blockWebsiteParsed = BeautifulSoup(websiteHTML.content, 'html.parser')

        # Find by ID
        if int(blockTypeSelection)==1:

            # Find id class name
            analyzedIDResults = blockWebsiteParsed.find(id=str(monitorIDBlock))

            print("")
            print("")
            print("**************************************************************************")
            print("Analysis results:")
            print("**************************************************************************")

            # Print analyzedResult
            print("")
            print("Results: ")
            print(analyzedIDResults.prettify())

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
                    print("¡¡¡Changes detected!!!")
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
                        print("Push sent")
                        time.sleep(2)

                    endTracking = 1

        # Find by other configuration
        else:
            analyzedOtherResults = blockWebsiteParsed.find(str(monitorOtherBlockObject), class_=str(monitorOtherBlockClass))

            print("")
            print("")
            print("**************************************************************************")
            print("Analysis results:")
            print("**************************************************************************")
            print("")
            print("Results:")
            print(str(analyzedOtherResults.text))

            # Create backup first run
            if int(originalBackup)==0:
                backupAnalyzedOtherResults=analyzedOtherResults
                originalBackup=1

            # Analyze changes
            else:
                if str(backupAnalyzedOtherResults)==str(analyzedOtherResults):
                    print("")
                    print("Analyzed block has not changes")
                else:


                    print("")
                    print("")
                    print("**************************************************************************")
                    print("ALERT:")
                    print("**************************************************************************")
                    print("")
                    print("¡¡¡Changes detected!!!")
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
                        print("Push sent")
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
    print("Website analyzed and monitorig done correctly.")
