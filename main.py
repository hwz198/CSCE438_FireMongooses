import socket, select, string, sys, random
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer

#Constants
Hit_title = "Correct or approve these few sentences!" 
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

#Fourth example string || 
ExampleFour = 'YO MAMMA'

#Fifth example string || 
ExampleFive = 'YOUR MUTTA'

#print 'Please enter your Amazon Account username'
#username = int(sys.stdin.readline())
#print 'Please enter your Password'
#password = int(sys.stdin.readline())


#main function
if __name__ == "__main__":
	ACCESS_ID = 'AKIAIC6NJRXA5KHGVFXA'
	SECRET_KEY = 'hIy1A5Xcq4VDcOhDlBuXhm39O4s9ci3hd4K9/CJr'
	HOST = 'mechanicalturk.sandbox.amazonaws.com'
	mtc = MTurkConnection(aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY, host=HOST)
	while True: 
		print '============Fire Mongooses Amazon Turk Application============'
		print 'Please enter the number of the action you would like to take:'
		print '(1) Create a HIT'
		print '(2) Recieve Results'
		print '(3) Approve all HITs'
		print '(4) Reject all HITs'
		print '(5) Exit'
		MainInput = int(sys.stdin.readline())

		if MainInput == 1:
			print '============Create a HIT============'
			print 'What would you like do?'
			print '(1) Choose an example string to use'
			print '(2) Write my own string'
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
					overview=Overview()
					overview.append_field('Title', 'Correct or Approve the grammar')
					question1 = QuestionContent()
					question1.append_field('Title', ExampleOne)
					answerfield1 = FreeTextAnswer()
					fullquestion1 = Question(identifier="answer", content=question1, answer_spec=AnswerSpecification(answerfield1))
					questionform1=QuestionForm()
					questionform1.append(overview)
					questionform1.append(fullquestion1)
					mtc.create_hit(questions=questionform1,max_assignments=1,title=Hit_title,description='Correct or approve this excerpt',keywords='Grammar, Correct',duration = 300, reward=0.01)
				elif SentenceMenuInput == 2:
					print 'Example Two chosen'
				elif SentenceMenuInput == 3:
					print 'Example Three chosen'
				elif SentenceMenuInput == 4: 
					print 'Example Four chosen'
				elif SentenceMenuInput == 5:
					print 'Example Five chosen'
				else: 
					print 'Invalid Input, returning to main menu.'
			elif CreateInput == 2:
				print '============Create a HIT============'
				print 'Please enter the sentence(s) you would like to use for the HIT:'
				InputSentence = sys.stdin.readline()
				print 'Your input was: '+InputSentence+'\n'
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
