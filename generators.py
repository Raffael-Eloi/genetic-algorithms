import random

# createEightRamdomBinaries: Returns eight randoms binaries numbers
def createEightRandomBinaries() -> str:
    binaries = ''
    for eachBinary in range(8):
        binaries += str(random.randrange(0, 2))
    return binaries

# createEightRamdomBinaries: Returns a list with 100 randoms binaries numbers with eight characters each
def createOneHundredBinaries() -> list:
    listOfBinaries = []
    for eachBinaryList in range(100):
        listOfBinaries.append( createEightRandomBinaries() )
    return listOfBinaries