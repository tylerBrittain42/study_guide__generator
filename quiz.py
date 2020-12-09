import bs4, html5lib, os, platform


#Removes tags
def noTags(foo):

    foo = str(foo).replace("<span>", "")
    foo = str(foo).replace("</span>", "")

    foo = str(foo).replace("<em>", "")
    foo = str(foo).replace("</em>", "")
    return(foo)

#Writes the questions of the file to the target file
def getQuestions(quiz, target):

    outF = open(target,"a")
    soup = bs4.BeautifulSoup(open(quiz), "html.parser")
    questions = []

    #Parses the 
    question = soup.find_all("div",{"class": "question_text user_content"})
    for curQ in question:
        foo = ((str(curQ)).split("<p>")[1]).split("</p>")[0]
        foo = noTags(foo)
        questions.append(foo)


    #Writes the questions
    outF.write('\n\n----------------------------------------------\n')
    #Change sunstring to length of the containing folder
    outF.write( quiz[8:] + '\n\n')
    for foo in range(0,len(questions)):
        outF.write(str(foo+1) + ')' + questions[foo] + '\n\n')
    outF.close()

#Clears the file
def clearFile(target):
    open(target, 'w').close()

#Does the thing with respect to the correct operating
def doTheThing(folderToAccess,fileToWrite):

    quizList = os.listdir(folderToAccess)
    quizList = sorted(quizList)

    if(platform.system() == "Linux"):
        for quizWeek in quizList:
            week = os.listdir(folderToAccess + '/' + quizWeek)
            for quiz in week:
                getQuestions((folderToAccess + "/" + quizWeek + '/' + quiz),fileToWrite)


    elif (platform.system == "Windows"):
        for quizWeek in quizList:
            week = os.listdir(folderToAccess + '\\' + quizWeek)
            for quiz in week:
                getQuestions((folderToAccess + "\\" + quizWeek + '\\' + quiz),fileToWrite)


def main():

    #Set equal to values you want to access
    toWrite = "key.txt"
    readFrom = "quizzes"

    #Resets and then writes to the file
    clearFile(toWrite)
    doTheThing("quizzes", toWrite)


if __name__ == "__main__":
    main()
