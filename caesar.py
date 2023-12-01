'''
The code you provided is a Python program that implements the Caesar cipher algorithm for encryption and decryption.
'''

def getDoubleAlphabet(alphabet, key=2):
    doubleAlphabet = alphabet * int(key)
    return doubleAlphabet
    
def donut_caesar(msg, key):
    # ประกาศตัวแปร Cipher เพื่อเก็บข้อความเข้ารหัสแล้ว
    cipher = ''
    for t in msg:
        plain_text = ord(t.upper())
        
        new_text = plain_text
        # ถ้าข้อความที่ต้องการเป็นอักษร a-z ให้ทำการแปลงค่าตาม key เกิน 65 ให้เริ่มต้นใหม่
        if(plain_text >= 65 and plain_text <= 90):
            new_text = ((ord(t.upper()) + key - 65) % 26) + 65
            
        cipher = cipher + chr(new_text)
    return cipher
    
def decryptMessage(message, cipherKey):
    decryptKey = -1 * int(cipherKey)
    return donut_caesar(message, decryptKey)

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return int(shiftAmount) % 26
    
    
# The `def main():` function is the main entry point of the program. It is where the program execution starts. 
# It calls other functions to get the message to encrypt, the cipher key, and then performs the encryption and decryption 
# using the Caesar cipher algorithm. Finally, it prints the encrypted message and the decrypted message.
def main():
    plain_text = getMessage()
    key = getCipherKey()
    
    cipher = donut_caesar(plain_text, key)
    print(cipher)
    
    print(decryptMessage(cipher, key))
    
main()
# aws re/start caesar cipher lab, 5
# FBX WJ/XYFWY HFJXFW HNUMJW QFG