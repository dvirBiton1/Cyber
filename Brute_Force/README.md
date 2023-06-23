
Use for cyber ethical purposes only! Not for hacking !
# Brute Force
## Attacking & Mitigation
## Written by Ohad Shirazi & Dvir Biton.
## About This Project:

In this project there are four parts using Python.
In the project we used the following libraries:
paramiko
colorama
pyfiglet
scapy

The first part "IP_MAC_Scanner.py" script purpose is to scan the IP and MAC address in the local network

The second part "port_scanner.py" script purpose is to scan the open ports with the attacked IP

The third part "bf_attack.py" script is the main attack tool - in order to guess the password

The fourth part "bf_mitigation.py" script is the mitigation tool, which detects brute force attacks. Based on reading logs.

### preinstalls:

$ pip3 install paramiko

$ pip3 install colorama

$ pip3 install pyfiglet

$ pip3 install scapy

### How to use:
First use the IP_MAC_Scanner to see witch victims are in the local network
* open terminal in the same directory of the code "IP_MAC_Scanner"
* command: python port_scanning.py

NOTE: You need to add your gateway at the code.


Second use the port_sanning to see if the victim's port 22 is open:
* open terminal in the same directory of the code "port_scanning"
* command: python port_scanning.py <ip> (ip target)

Now we will start the attack with the bture force tool:
* open terminal in the same directory of the code "bf_attack.py"(the word list have to be in the same directory).
* command: python bf_attack.py <ip> (ip target) -u <username> -P <worldList> (txt file with passwords parse by enter)
          
          example: python bf_attack.py 13.20.12.45 -u admin -P worldList.txt

In order to check your mitigation tool' you have to run it before the attack:
* open terminal in the same directory of the code "bf_mitigation.py"
* command: python bf_mitigation.py
          
          
![image](https://user-images.githubusercontent.com/92723105/189150399-0476d006-9d92-4d04-9b17-f5089ce6e409.png)


