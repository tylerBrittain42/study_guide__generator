#ADD Paranthesis and negation


allVal = {
    'x' : True,
    'y' : False,
    'z' : True,
    'a' : True
}

def main():

    phrase = input('enter: ')

    print('answer = ' + str(parse(phrase)))

    print('end')
    #precedence order is
    #not and or implies contra




def parse(phrase):


    opCount = 0

    phrase = phrase.replace(' ', '')

    #precedence order is
    #not and or implies contra
    

    #checks to see if there is only one operator 
    opCount = phrase.count('or') + phrase.count('and') +  phrase.count('<->') + phrase.count('->')
    
    opp = curOp(phrase)
    # try:
    #     a = curVar(phrase.split(opp)[0])
    #     print('a: ' + str(a))
    #     b = curVar(phrase.split(opp)[1])
    #     print('b: ' + str(b))
    # except IndexError:
    #     print('b: n/a')

    # print('opp: ' + str(opp))
    # print('count: ' + str(opCount) + '\n')


    if opCount == 0:
        return(curVar(phrase.split(opp)[0]))
    elif opCount == 1:
        return(eval(curVar(phrase.split(opp)[0]),curVar(phrase.split(opp)[1]),opp))


    #reverse precedence order bc recursive calls
    else:
        return(eval(parse(phrase.split(opp)[0]),parse(phrase.split(opp)[1]), opp))

        




#returns a boolean corresponding with the current value
def curVar(val):
    return(allVal[val])

#returns the current operator(As a string)
def curOp(phrase):
    if (phrase.find('<->') != -1):
        return('<->')
    if (phrase.find('->') != -1):
        return('->')
    if (phrase.find('or') != -1):
        return('or')
    if (phrase.find('and') != -1):
        return('and')





#evaluates a boolean phrase consisting of two values and an operator
#All tested and work
def eval(a,b,operator):
    print('ea: ' + str(a))
    print('eb: ' + str(b))


    #or
    if (operator == 'or'):
        return( a or b)
   
    #and
    elif (operator == 'and'):
        return(a and b)
    
    #implies
    elif(operator == '->'):
        if( (a == True) and (b == False)):
            return(False)
        else:
            return(True)

    #contraposition
    elif(operator == '<->'):
        if(a == b):
            return(True)
        else:
            return(False)


if __name__ == "__main__":
    main()
