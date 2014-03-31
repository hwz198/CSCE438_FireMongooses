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

def show_results(mtc):
	num_hits = 50
	hits = mtc.get_reviewable_hits(page_size = num_hits)
	print "Total results to fetch %s " % hits.TotalNumResults
	print "Request hits page %i" % 1
	total_pages = float(hits.TotalNumResults)/num_hits
	total_num = int(total_pages)
	if(total_pages - total_num > 0):
		total_pages = total_num+1
	else:
		total_pages = total_num
	page_num = 1
	while page_num < total_pages:
		page_num = page_num + 1
		print "Request hits page %i " % page_num
		temp_hits = mtc.get_reviewable_hits(page_size = num_hits, page_number = page_num)
		hits.extend(temp_hits)
	return hits

#main function
if __name__ == "__main__":
	ACCESS_ID = 'Your info here'
	SECRET_KEY = 'Your info here'
	HOST = 'mechanicalturk.sandbox.amazonaws.com'
	mtc = MTurkConnection(aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY, host=HOST)
	while True: 
		print '============Fire Mongooses Amazon Turk Application============'
		print 'Please enter the number of the action you would like to take:'
		print '(1) Create a HIT'
		print '(2) Show Results'
		print '(3) Approve HITs'
		print '(4) Reject HITs'
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
					question = QuestionContent()
					question.append_field('Title', ExampleOne)
					answerfield = FreeTextAnswer()
					fullquestion = Question(identifier="answer", content=question, answer_spec=AnswerSpecification(answerfield))
					questionform=QuestionForm()
					questionform.append(overview)
					questionform.append(fullquestion)
					mtc.create_hit(questions=questionform,max_assignments=1,title=Hit_title,description='Correct or approve this excerpt',keywords='Grammar, Correct',duration = 300, reward=0.01)
					
				elif SentenceMenuInput == 2:
					print 'Example Two chosen'
					overview=Overview()
					overview.append_field('Title', 'Correct or Approve the grammar')
					question = QuestionContent()
					question.append_field('Title', ExampleTwo)
					answerfield = FreeTextAnswer()
					fullquestion = Question(identifier="answer", content=question, answer_spec=AnswerSpecification(answerfield))
					questionform=QuestionForm()
					questionform.append(overview)
					questionform.append(fullquestion)
					mtc.create_hit(questions=questionform,max_assignments=1,title=Hit_title,description='Correct or approve this excerpt',keywords='Grammar, Correct',duration = 300, reward=0.01)
				elif SentenceMenuInput == 3:
					print 'Example Three chosen'
					overview=Overview()
					overview.append_field('Title', 'Correct or Approve the grammar')
					question = QuestionContent()
					question.append_field('Title', ExampleThree)
					answerfield = FreeTextAnswer()
					fullquestion = Question(identifier="answer", content=question, answer_spec=AnswerSpecification(answerfield))
					questionform=QuestionForm()
					questionform.append(overview)
					questionform.append(fullquestion)
					mtc.create_hit(questions=questionform,max_assignments=1,title=Hit_title,description='Correct or approve this excerpt',keywords='Grammar, Correct',duration = 300, reward=0.01)
				elif SentenceMenuInput == 4: 
					print 'Example Four chosen'
					overview=Overview()
					overview.append_field('Title', 'Correct or Approve the grammar')
					question = QuestionContent()
					question.append_field('Title', ExampleFour)
					answerfield = FreeTextAnswer()
					fullquestion = Question(identifier="answer", content=question, answer_spec=AnswerSpecification(answerfield))
					questionform=QuestionForm()
					questionform.append(overview)
					questionform.append(fullquestion)
					mtc.create_hit(questions=questionform,max_assignments=1,title=Hit_title,description='Correct or approve this excerpt',keywords='Grammar, Correct',duration = 300, reward=0.01)
				elif SentenceMenuInput == 5:
					print 'Example Five chosen'
					overview=Overview()
					overview.append_field('Title', 'Correct or Approve the grammar')
					question = QuestionContent()
					question.append_field('Title', ExampleFive)
					answerfield = FreeTextAnswer()
					fullquestion = Question(identifier="answer", content=question, answer_spec=AnswerSpecification(answerfield))
					questionform=QuestionForm()
					questionform.append(overview)
					questionform.append(fullquestion)
					mtc.create_hit(questions=questionform,max_assignments=1,title=Hit_title,description='Correct or approve this excerpt',keywords='Grammar, Correct',duration = 300, reward=0.01)
				else:
					print 'Invalid Input, returning to main menu.'


			elif CreateInput == 2:
				print '============Create a HIT============'
				print 'Please enter the sentence(s) you would like to use for the HIT:'
				InputSentence = sys.stdin.readline()
				print 'Your input was:'+InputSentence+'\n'
				overview=Overview()
				overview.append_field('Title', 'Correct or Approve the grammar')
				question = QuestionContent()
				question.append_field('Title', InputSentence)
				answerfield = FreeTextAnswer()
				fullquestion = Question(identifier="answer", content=question, answer_spec=AnswerSpecification(answerfield))
				questionform=QuestionForm()
				questionform.append(overview)
				questionform.append(fullquestion)
				mtc.create_hit(questions=questionform,max_assignments=1,title=Hit_title,description='Correct or approve this excerpt',keywords='Grammar, Correct',duration = 300, reward=0.01)
			else:
				print 'Invalid Input, returning to main menu.'
		elif MainInput == 2:
			print '============Show Results============'
			print 'Results recieved.'
			hits = show_results(mtc)
			for hit in hits:
				assignment = mtc.get_assignments(hit.HITId)
				for assign in assignment:
					print "Answers of the worker number %s " % assign.WorkerId
					#print "HITId is %s " % assign.HITId #Removed due to better efficiency of using Assignment ID for the same purposes
					print "Assign ID is %s " % assign.AssignmentId
					for question_form_answer in assign.answers[0]:
						print question_form_answer.fields
						print "-------------------"
			
			
		elif MainInput == 3:
			print '============Approve Workers============'
			print 'What would you like do?'
			print '(1) Approve worker by HITId'
			print '(2) Approve all submissions'
			choice = int(sys.stdin.readline())

			if choice == 1:
				print 'Input Assignment ID of the HIT you want to approve' 
				inputassign = sys.stdin.readline()
				mtc.approve_assignment(inputassign)
				for hit in hits:
					assignment = mtc.get_assignments(hit.HITId)
					for assign in assignment:
						if inputassign == assign.AssignmentId:
							mtc.disable_hit(hit.HITId)
			elif choice == 2:
				hits = show_results(mtc)
				#for temp in hits:
				#	mtc.disable_hit(temp.HITId)
				for hit in hits:
					assignment = mtc.get_assignments(hit.HITId)
					for assign in assignment:
						mtc.approve_assignment(assign.AssignmentId)
					mtc.disable_hit(hit.HITId)
			#print 'Top HIT sumbission has been approved.'
			#mtc.disable_hit(temp.HITId)
			else:
				print 'Invalid input, returning to menu'
		elif MainInput == 4:
			print '============Reject Workers============'
			print 'What would you like do?'
			print '(1) Reject worker by HITId'
			print '(2) Reject all submissions'
			choice = int(sys.stdin.readline())

			if choice == 1:
				hits = show_results(mtc)
				print 'Input Assignment ID of the HIT you want to reject' 
				inputassign = sys.stdin.readline()
				mtc.reject_assignment(inputassign)
				for hit in hits:
					assignment = mtc.get_assignments(hit.HITId)
					for assign in assignment:
						if inputassign == assign.AssignmentId:
							print 'Found it'
							mtc.disable_hit(hit.HITId)
			elif choice == 2:
				hits = show_results(mtc)
				#for temp in hits:
				#	mtc.disable_hit(temp.HITId)
				for hit in hits:
					assignment = mtc.get_assignments(hit.HITId)
					for assign in assignment:
						mtc.reject_assignment(assign.AssignmentId)
					mtc.disable_hit(hit.HITId)
			#print 'Top HIT sumbission has been approved.'
			#mtc.disable_hit(temp.HITId)
			print 'all pending HIT sumbissions have been rejected.'
		elif MainInput == 5:
			print 'Exiting....'
			hits = show_results(mtc)
			#for temp in hits:
			#	mtc.disable_hit(temp.HITId)
			for hit in hits:
				mtc.disable_hit(hit.HITId)
			break
		else: 
			print 'Invalid input' 
