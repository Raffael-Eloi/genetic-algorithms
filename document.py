from validation import isInputValid
from transform import tranformBinaryToDecimal, transformFloatToBinary, invertBinaryValue
from generators import createEightRandomBinaries, createOneHundredBinaries

"""
    firstQuestion: Receive a string with values 0 or 1
    Returns real number converted to float 
"""
def firstQuestion(numBinaries: str) -> float:   
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
    Example: if 0:  value = 1 || if 1: value = 0
"""
def ninethQuestion(binaries: str) -> str:
    newBinary = ''
    for binary in binaries:
        newBinary += invertBinaryValue(binary)
    return newBinary

"""
    tenthQuestion: Receive two string with eight values 0 or 1
    Returns two string 
        first string -> first 4 numbers of the first string
        first string -> last 4 numbers of the second string

        second string -> first 4 numbers of the first string
        second string -> last 4 numbers of the second string
"""
def tenthQuestion(firstBinaries: str, secondBinaries: str) -> list:
    return [ (firstBinaries[:4] + secondBinaries[4:]), (secondBinaries[:4] + firstBinaries[4:]) ]

"""
    tenthQuestion: Receive two string with eight values 0 or 1
    Returns two string 
        first string -> first 2 numbers of the first string
        first string -> 4 numbers in the middle of the second string
        first string -> last 2 numbers of the first string

        second string -> first 2 numbers of the second string
        second string -> 4 numbers in the middle of the first string
        second string -> last 2 numbers of the second string
"""
def eleventhQuestion(firstBinaries: str, secondBinaries: str) -> list:
    return [ (firstBinaries[:2] + secondBinaries[2:6] + firstBinaries[6:]), (secondBinaries[:2] + firstBinaries[2:6] + secondBinaries[6:]) ]

print(eleventhQuestion('11111111', '00000000'))
