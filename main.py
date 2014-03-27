import socket, select, string, sys, random

#Constants
title = "Correct or approve these few sentences!" 
HitType = "text"
PayAmount = .01
NumHits = 10 

#String Constants

# First example string || 'and not' should be 'than' (SAT Prep Easy)
ExampleOne = 'The students have discovered that they can address issues more effectively through letter-writing campaigns and not through public demonstrations'

# Second example string  || last part should read, 'which she thought was more sophisticated than the interpretations of the other performers.' (SAT Prep Medium)
ExampleTwo = 'At the music recital, Alexandra enjoyed listening to her friend Mohammed\'s insightful interpretation, which she thought was more sophisticated than the other performers'

# Third example string  || Should read, 'All states impose severe penalties on drivers who do not stop when they are involved in accidents.' (SAT Prep Hard)
ExampleThree = 'All states impose severe penalties on drivers who do not stop when he or she is involved in accidents.'

#print 'Please enter your Amazon Account username'
#username = int(sys.stdin.readline())
#print 'Please enter your Password'
#password = int(sys.stdin.readline())


#main function
if __name__ == "__main__":
	ACCESS_ID = 'your inforino here, no copy pasterino'
	SECRET_KEY = 'your infomacíon aqui'
	HOST = 'mechanicalturk.sandbox.amazonaws.com'
	mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)
	while True: 
		print '============Fire Mongooses Amazon Turk Application============'
		print 'Please enter the number of the action you would like to take:'
		print '(1) Create a HIT'
		print '(2) Recieve Results'
		print '(3) Approve all HITs'
		print '(4) Reject all HITs'
		CreateInput =  int(sys.stdin.readline())
			if CreateInput == 1:
				print '============Create a HIT============'
				print 'Please choose one of the following strings:'
				print '(1)'+ExampleOne+'\n'
				print '(2)'+ExampleTwo+'\n'
				print '(3)'+ExampleThree+'\n'
				print '(4)'+ExampleFour+'\n'
				print '(5)'+ExampleFive+'\n'
				SentenceMenuInput = int(sys.stdin.readline())
				if SentenceMenuInput == 1:
					print 'Example One chosen'
				elif SentenceMenuInput == 2:
					print 'Example Two chosen'
				elif SentenceMenuInput == 3:
					print 'Example Three chosen'
				elif SentenceMenuInput == 4: 
					print 'Example Four chosen'
				elif SentenceMenuInput == 5:
					print 'Example Five chosen'
				else: 
					print '============Create a HIT============'
					print 'Please enter the sentence(s) you would like to use for the HIT:'
					InputSentence = sys.stdin.readline()
					print 'Your input was:'+InputSentence+'\n'
			elif CreateInput == 2:
				print 'recieve input'
			else:
				print 'Invalid Input, returning to main menu.'
		elif MainInput == 2:
			print 'Results recieved.'
		elif MainInput == 3:
			print 'all pending HIT sumbissions have been approved.'
		elif MainInput == 4:
			print 'all pending HIT sumbissions have been rejected.'
		elif MainInput == 5:
			print 'Exiting....'
			break
		else: 
			print 'Invalid input' 
