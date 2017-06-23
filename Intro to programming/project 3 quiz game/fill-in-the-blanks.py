#quiz question line
statement_1 = ["Full form of HTML is Hyper Text _1_ language. Front end consists of _2_, _3_ languages.html is saved with extension ._4_.","Full form of CSS is Cascading Style _1_.Css is saved with extension ._2_.Both css and _3_ are used in _4_ end."," CSS can be included in _1_ ways i.e._2_,_3_,_4_"]
#answer-list to mach answer with question list 
answer_list = [["markup","html","css","html"],["sheet","css","html","front"],["three","internal","external","inline"]]

def ask_level():
    #takes level number
    user_input1 =int(raw_input ("\nPlease enter level number of the quiz\n"+"\nPress 1 : for level 1(easy)\n"+"\nPress 2 : for level 2(medium)\n"+"\nPress 3: for level 3(hard)\n" ))
    return user_input1-1

def check(final_input,answer):
    #checks for answer true or not
    #use of if else
    if (final_input == answer):
        return True
    else:
        return False

def replacement(answer,quiz,index):
    #replace value with correct answer
    #use of replace
    value = "_"+str(index+1)+"_"
    question = quiz.replace(value,answer)
    return question

def wrong():
    #displays a prompt for wrong answer
    print"Sorry your answer is wrong :(.Please try again!!!"

def final(quiz):
#Takes input from user and goes to next blank
    index = 0
    max_no_blanks = 4
    #as 4 blanks taken in statement1 part
    #checking with blank number using while loop
    while index < max_no_blanks:
        print(quiz+"\n")
        answer = (answer_list[level][index])
        #print correct answer line
        user_input = raw_input("the answer to the "+ str(index+1)+ " is:")
        final_input = user_input.lower()
        #use of if else
        if check(final_input,answer):
            quiz = replacement(answer,quiz,index)
            index = index+1
            print ("Congrant!!You are correct!!")
        else:
            #wrong function called
            wrong()

print ("Hi.Start your quiz")
#ask level function called
level = ask_level()
quiz = statement_1[level]
final(quiz)


    

