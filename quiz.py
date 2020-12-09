import bs4, html5lib, os


#Removes tags
def noTags(foo):

    foo = str(foo).replace("<span>", "")
    foo = str(foo).replace("</span>", "")

    foo = str(foo).replace("<em>", "")
    foo = str(foo).replace("</em>", "")
    return(foo)


#parses an entire file
def parseFile(quiz, type):
    outF = open("key.txt",type)

    soup = bs4.BeautifulSoup(open(quiz), "html.parser")
    qs = []
    ans = []

    #Parsing Questions
    question = soup.find_all("div",{"class": "question_text user_content"})
    for curQ in question:
        foo = ((str(curQ)).split("<p>")[1]).split("</p>")[0]
        foo = noTags(foo)
        qs.append(foo)


    #Parsing answers
    x = soup.find_all("div",{"class": "answer answer_for_ selected_answer correct_answer"})
    for foo in x:
        bar = str(foo).split('title="')[1]
        print(bar.split('This was the correct')[1])
        ans.append(bar.split('This was the correct answer')[0])



    outF.write('\n\n----------------------------------------------\n')
    outF.write( quiz + '\n\n')
    for foo in range(0,len(qs)):
        try:
            outF.write(str(foo+1) + ')' + qs[foo] + '\n')
            outF.write('a:' + ans[foo] + '\n\n')
            #outF.write("\n-----------------------------\n")
        except IndexError:
            outF.write('a: INVALID\n\n')
    outF.close()

def main():

    #quizList = os.listdir("ai_quizzes")

    #for quiz in quizList:
        #parseFile(("ai_quizzes\\" + quiz),'w')

    parseFile(("ai_quizzes\\2020-10-22 V1 Mind Ontologies.html"), 'w')
if __name__ == "__main__":
    main()
