allVal = {
    'x' : True,
    'y' : False,
    'z' : True
}

def main():

    phrase = input('enter: ')

    print(parse(phrase))

    #precedence order is
    #not and or implies contra




def parse(phrase):

    opCount = 0

    phrase = phrase.replace(' ', '')

    #precedence order is
    #not and or implies contra
    
    #checks to see if there is only one operator 
    opCount = phrase.count('or') + phrase.count('and') +  phrase.count('<->') + phrase.count('->')
    if opCount == 1:
        return(eval(phrase,curOp(phrase)))

#returns a boolean corresponding with the current value
def curVar(val):
    return(allVal[val])

#returns the current operator(As a string)
def curOp(phrase):
    if (phrase.find('or') != -1):
        return('or')
    if (phrase.find('and') != -1):
        return('and')
    if (phrase.find('->') != -1):
        return('->')
    if (phrase.find('<->') != -1):
        return('<->')



#evaluates a boolean phrase consisting of two values and an operator
#All tested and work
def eval(phrase,operator):

    a = curVar(phrase.split(operator)[0])
    b = curVar(phrase.split(operator)[1])

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
