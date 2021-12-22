class DNI:
    """
    Class representing a DNI object
    """

    dni = str
    isValid = bool
    isValidChar = bool
    validChars = str
    validLength = int

    def __init__(
        self,
        newDNI: str = "",
        *,
        validChars: str = "TRWAGMYFPDXBNJZSQVHLCKE",
        validLength: int = 9
    ) -> None:
        self.dni = newDNI.upper()
        self.isValid = False
        self.isValidChar = False
        self.validChars = validChars
        self.validLength = validLength

    # PUBLIC

    def setDNI(self, newDNI: str) -> None:
        self.dni = newDNI.upper()

    def getDNI(self) -> str:
        return self.dni

    def setValid(self, valid: bool = False) -> None:
        self.isValid = valid

    def getValid(self) -> bool:
        return self.isValid

    def setValidChar(self, valid: bool = False) -> None:
        self.isValidChar = valid

    def getValidChar(self) -> bool:
        return self.isValidChar

    def validate(self) -> bool:
        self.setValid(
            self.checkValidLength() and self.checkNumbers() and self.checkValidChar()
        )
        return self.getValid()

    # PRIVATE
    def calculateChar(self) -> str:
        mod = self.getNumbers(int) % len(self.validChars)
        return self.validChars[mod]

    def getNumbers(self, converter: object = str) -> str:
        return converter(self.getDNI()[:-1])

    def getChar(self) -> str:
        return self.getDNI()[-1]

    def checkNumbers(self) -> bool:
        return self.checkValidLength() and self.getNumbers().isdigit()

    def checkValidLength(self) -> bool:
        return len(self.getDNI()) == self.validLength

    def checkValidChar(self) -> bool:
        self.setValidChar(
            self.checkValidLength()
            and self.checkNumbers()
            and self.calculateChar() == self.getChar()
        )
        return self.getValidChar()
