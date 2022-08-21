# tranformBinaryToDecimal: Returns a converted value from binary to int
def tranformIntegerToBinary(value: str) -> bin:
    return bin(value)

# tranformIntegerToBinary: Returns a converted value from integer to binary
def tranformBinaryToDecimal(binary: str) -> int:
    return int(binary, 2)

def tranformBinaryToFloat(binary: str) -> float:
    firstTwoValues = tranformBinaryToDecimal(binary[0:2])
    lastSixValues  = tranformBinaryToDecimal(binary[2:])
    valueFormated = str(firstTwoValues) + '.' + str(lastSixValues)
    return float(valueFormated)
    
# transformFloatToBinary: Returns a converted value from float to binary
def transformFloatToBinary(binaries: str):
    print('binaries', binaries)
    firstPart = tranformIntegerToBinary(int(str(binaries).split(".")[0]))[-2:]
    secondPart = tranformIntegerToBinary(int(str(binaries).split(".")[1]))[-6:]

    while len(firstPart) < 2: firstPart = "0" + firstPart
    while len(secondPart) < 6: secondPart = "0" + secondPart
    return firstPart + "." + secondPart

def invertBinaryValue(binary: str) -> str:
    if binary == '0': return '1'
    return '0'

def invertGene(gene: str) -> str:
    if gene == '0': return '1'
    return '0'
