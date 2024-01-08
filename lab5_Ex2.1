import math
import random

def encrypt(decimal, n, e):
    encryptedMessage = pow(decimal, e, n)
    return encryptedMessage

def decrypt(encryptedMessage, n, d):
    decryptedMessage = pow(encryptedMessage, d, n)
    return decryptedMessage

# Function to convert ASCII to hexadecimal
def asciiToHex():
    inputHexString = ''
    inputString = input("Name Surname: ")
    for char in inputString:
        asciiCode = ord(char)
        hexCode = hex(asciiCode)[2:]
        inputHexString += hexCode
    return inputHexString

# Function to convert hexadecimal to decimal
def hexToDecimal(hex):
    try:
        decimalValue = int(hex, 16)
    except ValueError:
        print(f"Invalid hexadecimal input: {hex}")
        return None
    return decimalValue

# Function to convert decimal to ASCII
def decimalToAscii(decimal):
    try:
        asciiString = bytes.fromhex(hex(decimal)[2:]).decode("ASCII")
    except ValueError:
        print(f"Invalid decimal input: {decimal}")
        return None
    return asciiString

if __name__ == "__main__":
    hexString = asciiToHex()
    decimalResult = hexToDecimal(hexString)

    p1 = 54842563352743889723271906945023799461683912940473330029869582002758596244734047414942944302575401866079095165920866170992209481931096674209393130965016371435481884569442089655485749411699719574982471053192268121939770159938429226702886877620651221471881385973515832825501519676270464254882861356577526795533
    p2 = 238039718749478761511019596847354973295026075984876928633653257742855107710737471114249091228926171182269108653240517408263838748050742921792047806440477129321715740869371925409624933238787851825052787854111484624080866546330545373342919542105555763920510724168660349992256096389664239565705057893180586933583
    n = p1 * p2
    print("n length in decimal: ", len(str(n)))
    PhiN = (p1 - 1) * (p2 - 1)
    
    while True:
        e = random.randint(1, PhiN - 1)
        gcdEPhiN = math.gcd(e, PhiN)
        # Check if e is coprime with PhiN
        if gcdEPhiN == 1:
            break
    d = pow(e, -1, PhiN)

    print("\nDecimal message: ", decimalResult)
    encryptedMessage = encrypt(decimalResult, n, e)
    print("Encrypted message: ", encryptedMessage)
    decryptedMessage = decrypt(encryptedMessage, n, d)
    print("Decrypted decimal message: ", decryptedMessage)
    print("Decrypted ASCII message: ", decimalToAscii(decryptedMessage))
