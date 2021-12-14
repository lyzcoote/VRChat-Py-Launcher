################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import platform
import os
import worldManager as worldManager
import urlCreator as urlHandler
import apiHandler as APIHandler
import logManager as logManager
################################################################################
#                                                                              #
#                                   Variables                                  #
#                                                                              #
################################################################################

version = "0.2.1.0Alpha"
authorGitHubUrl = "https://github.com/lyzcoote"

################################################################################
#                                                                              #
#                                   Functions                                  #
#                                                                              #
################################################################################


def get_arch_os():
    """
    Return the system architecture and OS
    """
    
    return platform.system()


def os_platform():
    """
    Return the system platform
    """
    true_platform = os.environ['PROCESSOR_ARCHITECTURE']
    try:
            true_platform = os.environ["PROCESSOR_ARCHITEW6432"]
    except KeyError:
            pass
            #true_platform not assigned to if this does not exist
    return true_platform


def getMaxStr(lst):
    """
    Return the maximum string length of a list
    Like duh?
    """
    return max(lst, key=len)


def printBox(list):
    """
    Print a box with the list of strings
    """
    print("+" + "-" * (len(getMaxStr(list)) + 3) + "+")
    for i in list:
        print("| " + i + " " * (len(getMaxStr(list)) - len(i)) + "  |")
    print("+" + "-" * (len(getMaxStr(list)) + 3) + "+")



def launcherMenu():
    """
    Print the launcher menu
    """
    print("[i] Welcome to LyzCoote's World Launcher! \n")
    print("[i] You're running version: {}".format(version) + "\n")
    print("[!] Please note that this script is not 100% accurate and will contain bug/crashes. \n")
    print("[i] Please select an option: ")
    print("[i] 1 - Display author's GitHub Page")
    print("[i] 2 - Display system informations ")
    print("[i] 3 - Display current VRChat API Key ")
    print("[i] 4 - Display a user info ")
    print("[i] 5 - Launch custom VRChat Instance ")
    print("[i] 6 - Launch Home VRChat World ")
    print("[i] 7 - Exit \n")
    print("\n")
    while True:
        try:
            option = int(input("[i] Please select an option: "))
            if option == 1:
                print("\n")
                os.system("cls")
                os.system("start \"\" \"{}\"".format(authorGitHubUrl))
                print("\n")
                os.system("cls")
                launcherMenu()
            elif option == 2:
                print("\n")
                os.system("cls")
                os.system("systeminfo")
                os.system("pause")
                print("\n")
                os.system("cls")
                launcherMenu()
            elif option == 3:
                print("\n")
                os.system("cls")
                logManager.logger("The current VRChat API Key is: {}".format(APIHandler.getCachedAPIKey()), "info")
                os.system("pause")
                os.system("cls")
                launcherMenu()
            elif option == 4:
                print("\n")
                os.system("cls")
                APIHandler.getUserInfo(APIHandler.getCachedAPIKey(), str(input("[i] Please enter a username: ")))
                os.system("pause")
                os.system("cls")
                launcherMenu()
            elif option == 5:
                os.system("cls")
                urlHandler.createCustomSession()
                break
            elif option == 6:
                os.system("cls")
                worldManager.lauchHomeWorld()
                break
            elif option == 7:
                print("\n")
                logManager.logger("Goodbye!", "info")
                print("\n")
                exit()
            else:
                print("\n")
                logManager.logger("Invalid option! Please try again. \n", "error")
                print("\n")
                continue
        except ValueError:
            print("\n")
            logManager.logger("Invalid option! Please try again. \n", "error")
            print("\n")
            continue