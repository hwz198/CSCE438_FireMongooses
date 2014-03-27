import socket, select, string, sys, random

#Constants
title = "Correct or approve these few sentences!" 
type = "text"
payamount = .01
numhits = 10 

#print 'Please enter your Amazon Account username'
#username = int(sys.stdin.readline())
#print 'Please enter your Password'
#password = int(sys.stdin.readline())


#main function
if __name__ == "__main__":
	while True: 
		print '============Fire Mongooses Amazon Turk Application============'
		print 'Please enter the number of the action you would like to take:'
		print '(1) Create a HIT'
		print '(2) Recieve Results'
		print '(3) Approve all HITs'
		print '(4) Reject all HITs'
		maininput = int(sys.stdin.readline())
		
		if maininput == 1:
			print 'HIT created.' 
		elif maininput == 2:
			print 'Results recieved.'
		elif maininput == 3:
			print 'all pending HIT sumbissions have been approved.'
		elif maininput == 4:
			print 'all pending HIT sumbissions have been rejected.'
		else: 
			print 'Invalid input' 
