#SECTION - Imports are also important to organize and document
import argparse
from src.displayers.args import *
from src.classes.example import example_object

#SECTION - Global entry parameters
#TODO - These are the only global variables you are allowed to use

#REVIEW - Using this function, you should be able to see in the terminal what parameters were used
printUsedArgs("TODO","TODO","TODO","TODO","TODO")

#SECTION - Optional arguments for running the script 
parser = argparse.ArgumentParser(prog='SeleniumImageParser', description='This script will scrape all the error screenshots in Jenkins starting from a build in a specific branch', epilog='Should not be used to add individual entries.')

#NOTE - This is a class in pyhton
print(f"{bcolors.BOLD}An NBI worker tuple:\n{example_object()}{bcolors.ENDC}")