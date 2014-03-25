import socket, select, string, sys, random

title = "Correct or approve these few sentences!" 
type = "text"
payamount = .01
numhits = 10 
	
	
#main function
if __name__ == "__main__":
	while True: 
		print '=====Fire Mongooses Amazon Turk Application===='
		print '(1) Create a HIT'
		print '(2) Recieve Results'
		print '(3) Approve all HITs'
		print '(4) Reject all HITs'
		
		maininput = sys.stdin.readline()
		
		if 1 is in maininput:
			print 'HIT created.' 
		elif maininput == 2:
			print 'Results recieved.'
		elif maininput == 3:
			print 'all pending HIT sumbissions have been approved.'
		elif maininput == 4:
			print 'all pending HIT sumbissions have been rejected.'
		else: 
			print 'Invalid input' 
