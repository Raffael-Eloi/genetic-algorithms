from validation import *
from transform import *
from generators import *

"""
    firstQuestion: Receive a string with values 0 or 1
    Returns real number converted to float 
"""
def firstQuestion(numBinaries: str) -> float:
    if not isInputValid(numBinaries):
        return "The input is not valid!"
    
    return transformFloatToBinary(numBinaries)

"""
    fithQuestion: Receive a string with values 0 or 1
    Returns a list with the format [binarie, value] 
"""
def fithQuestion(numBinaries: str) -> list:
    listForReturn = [numBinaries]
    listForReturn.append( tranformBinaryToDecimal(numBinaries) )
    return listForReturn


"""
    sixthQuestion: Receive a list of binaries
    Returns a list with the format [binarie, value]
"""
def sixthQuestion(listBinaries: list) -> list:
    listForReturn = []
    for eachBinary in listBinaries:
        elemntWithValue = []
        elemntWithValue.append(eachBinary)
        elemntWithValue.append( tranformBinaryToDecimal(eachBinary) )
        
        listForReturn.append(elemntWithValue)
    return listForReturn

"""
    seventhQuestion: Receive a real value 
    Returns the => 2 - realValueReceived²
"""
def seventhQuestion(realValue: float) -> float:
    return 2 - (realValue * realValue)

"""
    eightQuestion: Receive a list with the syntax [binarie, value]
    Returns a list ordened from smallest value to largest
"""
def eightQuestion(listBinaries: list) -> list:
    for eachBinary in listBinaries:
        print(eachBinary)


# eightQuestion ( sixthQuestion( createOneHundredBinaries() ) )

"""
    ninethQuestion: Receive a binaries
    Returns a binaries with the values inveted
    Example: if 0 = 1 || if 1 = 0
"""
def ninethQuestion(binaries: str) -> str:
    newBinary = ''
    for binary in binaries:
        newBinary += invertBinaryValue(binary)
    return newBinary

print(ninethQuestion('10101001'))


