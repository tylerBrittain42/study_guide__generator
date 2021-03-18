import bs4, html5lib, os, platform




#Writes the questions of the file to the target file
def getQuestions(quiz, target):

    outF = open(target,"a")
    soup = bs4.BeautifulSoup(open(quiz), "html.parser")
    questions = []

    #Parsing for questions and storeing them in an array
    #Canvas questions are stored in a div with this particulare class so we parse by said class
    question = soup.find_all("div",{"class": "question_text user_content"})
    for curQ in question:
        formattedQuestion = ((curQ.find('p').text))
        questions.append(formattedQuestion)


    #Writes the question array to key.txt
    outF.write('\n\n----------------------------------------------\n')
    outF.write( quiz + '\n\n')
    for formattedQuestion in range(0,len(questions)):
        outF.write(str(formattedQuestion+1) + ')' + questions[formattedQuestion] + '\n\n')
    outF.close()


#calls getQuestions with proper routing depending on os
def generateGuide(folderToAccess,fileToWrite):

    quizList = os.listdir(folderToAccess)

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


#Clears the file
def clearFile(target):
    open(target, 'w').close()

def main():

    #Set equal to values you want to access
    readFrom = input("Directory name: ")
    toWrite = "key.txt"
    

    #Resets and then writes to the file
    clearFile(toWrite)
    generateGuide(readFrom, toWrite)

    print(toWrite + " created")


if __name__ == "__main__":
    main()
