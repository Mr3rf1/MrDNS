import subprocess, re
from pyuac import runAsAdmin, isUserAdmin
from colorama import Fore
from time import sleep
from os import name

# check the os
if name != 'nt':
    print(f" {Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.RESET} This script just works on windows.")
    exit()

mainTxt = \
r"""
    ██████   ██████              ██████████   ██████   █████  █████████ 
    ░░██████ ██████              ░░███░░░░███ ░░██████ ░░███  ███░░░░░███
    ░███░█████░███  ████████     ░███   ░░███ ░███░███ ░███ ░███    ░░░ 
    ░███░░███ ░███ ░░███░░███    ░███    ░███ ░███░░███░███ ░░█████████ 
    ░███ ░░░  ░███  ░███ ░░░     ░███    ░███ ░███ ░░██████  ░░░░░░░░███
    ░███      ░███  ░███         ░███    ███  ░███  ░░█████  ███    ░███
    █████     █████ █████        ██████████   █████  ░░█████░░█████████ 
    ░░░░░     ░░░░░ ░░░░░        ░░░░░░░░░░   ░░░░░    ░░░░░  ░░░░░░░░░     t.me/Mr3rf1
"""


# Specify the preferred and alternate DNS addresses
oneone = ['1.1.1.1', '1.0.0.1']
google = ['8.8.8.8', '8.8.4.4']
elec = ['78.157.42.101', '78.157.42.100']
radar = ['10.202.10.10', '10.202.10.11']
openDns = ['208.67.222.222', '208.67.222.220']

# function that changes DNS
def setDNS(dns, netAdapter):
    command = f'netsh interface ip set dns name="{netAdapter}" source=static address={dns[0]} validate=no' # windows cmd command to set dns
    subprocess.run(command, shell=True, check=True) # another option: subprocess.Popen(...), os.system(...)
    command = f'netsh interface ip add dns name="{netAdapter}" address={dns[1]} validate=no'
    subprocess.run(command, shell=True, check=True)

def main():
    subprocess.run('cls', shell=True, check=True)
    print(mainTxt)
    # choosing network adapter
    netAdapter = input(f" {Fore.YELLOW}[{Fore.GREEN}<{Fore.YELLOW}]{Fore.RESET} Choose your adapter:\n   {Fore.YELLOW}[{Fore.CYAN}1{Fore.YELLOW}]{Fore.RESET} WiFi\n   {Fore.YELLOW}[{Fore.CYAN}2{Fore.YELLOW}]{Fore.RESET} Ethernet\n\n>>> {Fore.CYAN}")
    print(Fore.RESET)
    while True:
        if netAdapter == '1':
            netAdapter = 'Wi-Fi'
            break
        elif netAdapter == '2':
            netAdapter = 'Ethernet'
            break
        else:
            print(f' {Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.RESET} Wrong Command')
        netAdapter = input(">>> ")

    while True:
        # get current dns
        tmp = subprocess.run(f'netsh interface ip show dns "{netAdapter}"', shell=True, check=True, stdout=subprocess.PIPE)
        tmp = tmp.stdout.decode('utf-8')
        crDns = re.findall(r"\b\d+\.\d+\.\d+\.\d+\b", tmp)
        shDns = ""
        for dns in crDns:
            shDns += f"{dns}, "
        shDns = shDns[:-2]

        subprocess.run('cls', shell=True, check=True)
        print(mainTxt)
        # choosing DNS
        choice = input(f' {Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}]{Fore.RESET} Current DNS: {shDns}\n {Fore.YELLOW}[{Fore.GREEN}<{Fore.YELLOW}]{Fore.RESET} Choose DNS:\n    {Fore.YELLOW}[{Fore.CYAN}1{Fore.YELLOW}]{Fore.RESET} GoogleDNS\n    {Fore.YELLOW}[{Fore.CYAN}2{Fore.YELLOW}]{Fore.RESET} Clouadflare\n    {Fore.YELLOW}[{Fore.CYAN}3{Fore.YELLOW}]{Fore.RESET} ElectroDNS\n    {Fore.YELLOW}[{Fore.CYAN}4{Fore.YELLOW}]{Fore.RESET} RadarDNS\n    {Fore.YELLOW}[{Fore.CYAN}5{Fore.YELLOW}]{Fore.RESET} OpenDNS\n\n    {Fore.YELLOW}[{Fore.CYAN}c{Fore.YELLOW}]{Fore.RESET} clearDNS\n\n>>> {Fore.CYAN}')
        print(Fore.RESET)
        if choice == '1':
            setDNS(google, netAdapter)
        elif choice == '2':
            setDNS(oneone, netAdapter)
        elif choice == '3':
            setDNS(elec, netAdapter)
        elif choice == '4':
            setDNS(radar, netAdapter)
        elif choice == '5':
            setDNS(openDns, netAdapter)
        elif choice in ['c', 'C', 'clear', 'CLEAR']:
            command = f'netsh interface ip delete dns "{netAdapter}" all' # windows cmd command to clear dns
            subprocess.run(command, shell=True, check=True)
        else:
            print(f' {Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.RESET} Wrong command')
            sleep(0.5)

if __name__ == "__main__":
    # set app as administrator
    if not isUserAdmin():
        runAsAdmin()
    # run app
    main()