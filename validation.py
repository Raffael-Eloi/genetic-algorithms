def isInputValid(input_num_binaries: str) -> bool:
    if not isInputString(input_num_binaries) or not isNumbersBinaries(input_num_binaries) or not isNumbersSizeValid(input_num_binaries, 8):
        return False
    return True

def isInputString(input_num_binaries: str) -> bool:
    if not isinstance(input_num_binaries, str):
        return False
    return True

def isNumbersBinaries(input_num_binaries: str) -> bool:
    for number in input_num_binaries:
        if int(number) != 0 and int(number) != 1:
            return False

    return True

def isNumbersSizeValid(input_num_binaries: str, quantityAllowed: int) -> bool:
    return len(input_num_binaries) == quantityAllowed