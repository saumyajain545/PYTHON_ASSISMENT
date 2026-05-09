message = input("Enter message: ")
shift = 3
#encription
encrypted = ""

for ch in message:
    encrypted += chr(ord(ch) + shift)

print("Encrypted:", encrypted)
#Description
# Decryption

decrypted = ""

for ch in encrypted:
    decrypted += chr(ord(ch) - shift)
#displaying description
print("Decrypted:", decrypted)

'''
Enter message: HELLO
Encrypted: KHOOR
Decrypted: HELLO
'''
