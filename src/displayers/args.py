#STUB - Colors to enable prints
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printUsedArgs(dashboard,job,env,branch,build_number):
    print("\t\t{}======== Arguments ========".format(bcolors.OKCYAN))
    print("\tDashboard: " + dashboard)
    print("\tJob: " + job)
    print("\tEnvironment: " + env)
    print("\tBranch: " + branch)
    print("\tBuild Number: " + build_number)
    print("\t\t==========================={}".format(bcolors.ENDC))