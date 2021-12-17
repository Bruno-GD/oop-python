import pytest
from src.DNI import DNI

dniValid = DNI("77537159L")
dniInvalidChar = DNI("12345678A")
dniInvalidNumbers = DNI("A12345678")
dniInvalidLength = DNI("1234567A")

@pytest.mark.dni
def test_gets():
    assert dniValid.getNumbers() == "77537159"
    assert dniValid.getChar() == "L"
    assert dniValid.getDNI() == "77537159L"

    assert dniInvalidChar.getNumbers() == "12345678"
    assert dniInvalidChar.getChar() == "A"
    assert dniInvalidChar.getDNI() == "12345678A"

    assert dniInvalidNumbers.getNumbers() == "A1234567"
    assert dniInvalidNumbers.getChar() == "8"
    assert dniInvalidNumbers.getDNI() == "A12345678"

@pytest.mark.dni
def test_validators():
    assert dniValid.checkValidLength() == True
    assert dniValid.checkNumbers() == True
    assert dniValid.checkValidChar() == True

    assert dniInvalidChar.checkValidLength() == True
    assert dniInvalidChar.checkNumbers() == True
    assert dniInvalidChar.checkValidChar() == False

    assert dniInvalidNumbers.checkValidLength() == True
    assert dniInvalidNumbers.checkNumbers() == False
    assert dniInvalidNumbers.checkValidChar() == False

    assert dniInvalidLength.checkValidLength() == False
    assert dniInvalidLength.checkNumbers() == False
    assert dniInvalidLength.checkValidChar() == False

    assert dniValid.validate() == True
    assert dniInvalidChar.validate() == False
    assert dniInvalidNumbers.validate() == False
    assert dniInvalidLength.validate() == False