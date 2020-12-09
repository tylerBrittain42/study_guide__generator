import bs4, html5lib, os, platform


#Removes tags
def noTags(foo):

    foo = str(foo).replace("<span>", "")
    foo = str(foo).replace("</span>", "")

    foo = str(foo).replace("<em>", "")
    foo = str(foo).replace("</em>", "")
    return(foo)


#Writes the questions of the file to the target file
def getQuestions(quiz, type, target):

    outF = open(target,type)
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
    outF.write( quiz + '\n\n')
    for foo in range(0,len(questions)):
        outF.write(str(foo+1) + ')' + questions[foo] + '\n')
    outF.close()


#Clears the file
def clearFile(target):
    open(target, 'w').close()


def doTheThing(folderToAccess,fileToWrite):


    quizList = os.listdir(folderToAccess)

    if(platform.system() == "Linux"):
        for quiz in quizList:
            getQuestions((folderToAccess + "/" + quiz),'a',fileToWrite)

    elif (platform.system == "Windows"):
        for quiz in quizList:
            getQuestions((folderToAccess + "\\" + quiz),'a',fileToWrite)



def main():

   
   toWrite = "key.txt"
   readFrom = "ai_quizzes"

    clearFile(toWrite)
    doTheThing(readFrom, toWrite)


    


if __name__ == "__main__":
    main()
