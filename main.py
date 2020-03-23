# TODO create a random quize for a times table/divide
# TODO create 40 qustions as a mixture of combination
# TODO write the quiz to a text file - named the quiz and the date
# TODO write an answersheet to another file to compare answers
# TODO add a countdown timer for 4 min - press enter to start

# example question 5 X 5 = 
# store the questions and answers in a dict
# call open, write and close for the quiz and answer key text fields
# use random.shuffle() to randomise the order of the questions 

import random, itertools
# List containing the common numbers
oneTooTwelve = [1,2,3,4,5,6,7,8,9,10,11,12]
# List containing the questions
oneTimesQuestions = []
twoTimesQuestions = []
threeTimesQuestions = []
fourTimesQuestions = []
fiveTimesQuestions = []
sixTimesQuestions = []
sevenTimesQuestions = []
eightTimesQuestions = []
nineTimesQuestions = []
tenTimesQuestions = []
elevenTimesQuestions = []
twelveTimesQuestions = []

class TimesTableQuestion():

    def __init__(self, common_value, multiplyer, output_list):
        self.common_value = common_value
        self.multiplyer = multiplyer
        self.output_list = output_list

    def generateQuestion(self):
        for number in self.common_value:
            ans1 = (str(number) + ' X ' + str(self.multiplyer) + ' = ' + str(number * self.multiplyer))
            ans2 = (str(self.multiplyer) + ' X ' + str(number) + ' = ' + str(number * self.multiplyer))
            ans3 = (str(number * self.multiplyer) + ' / ' + (str(self.multiplyer) + ' = ' + (str(int((number * self.multiplyer) / self.multiplyer)))))
            # TODO add a line to include the divide questions - answer/common_value
            self.output_list.append(ans1)
            self.output_list.append(ans2)
            self.output_list.append(ans3)
            # TODO add the divide questions to the list
        return self.output_list

def initialiseLists():
    # Generate lists holding all the questions (and answers)
    # The TimesTableQuestion takes the numbers 1-12 as a list, the multiplyer, and the empty list name to put the result in as attributes
    oneTimesTable = TimesTableQuestion(oneTooTwelve,1,oneTimesQuestions)
    oneTimesTable.generateQuestion()

    twoTimesTable = TimesTableQuestion(oneTooTwelve,2,twoTimesQuestions)
    twoTimesTable.generateQuestion()

    threeTimesTable = TimesTableQuestion(oneTooTwelve,3,threeTimesQuestions)
    threeTimesTable.generateQuestion()

    fourTimesTable = TimesTableQuestion(oneTooTwelve,4,fourTimesQuestions)
    fourTimesTable.generateQuestion()

    fiveTimesTable = TimesTableQuestion(oneTooTwelve,5,fiveTimesQuestions)
    fiveTimesTable.generateQuestion()

    sixTimesTable = TimesTableQuestion(oneTooTwelve,6,sixTimesQuestions)
    sixTimesTable.generateQuestion()

    sevenTimesTable = TimesTableQuestion(oneTooTwelve,7,sevenTimesQuestions)
    sevenTimesTable.generateQuestion()

    eightTimesTable = TimesTableQuestion(oneTooTwelve,8,eightTimesQuestions)
    eightTimesTable.generateQuestion()

    nineTimesTable = TimesTableQuestion(oneTooTwelve,9,nineTimesQuestions)
    fiveTimesTable.generateQuestion()

    tenTimesTable = TimesTableQuestion(oneTooTwelve,10,tenTimesQuestions)
    tenTimesTable.generateQuestion()

    elevenTimesTable = TimesTableQuestion(oneTooTwelve,11,elevenTimesQuestions)
    elevenTimesTable.generateQuestion()

    twelveTimesTable = TimesTableQuestion(oneTooTwelve,12,twelveTimesQuestions)
    twelveTimesTable.generateQuestion()

def printAnswerSheet(question_list):
    random.shuffle(question_list) # shuffle the question list
    infinate_loop = itertools.cycle(question_list) # continuously cycle the list
    question_set = itertools.islice(infinate_loop, 0, 40) # take the first 40 questions
    for question in question_set:# print the output
        print(question + '\n')
        # TODO write the output to a text file

def printQuestionSheet(question_list):
    # TODO get the answer file, make a copy, remove the answers
    # TODO should have 2 seperate sheets, qustion and answer
    # TODO create a new folder each time a test is done with the date as the name
    pass



initialiseLists()
printAnswerSheet(twoTimesQuestions)

