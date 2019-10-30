def func(t, c, e):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    nText    = ""
    for i in range(0, len(t)):
        a = alphabet.find(t[i])
        nText += alphabet[((a+c) if e == "e" else (a-c))%26]
    return nText

while True:
    uInput = input("Do you want to encrypt or decrypt? Input e for encryption or d for decryption: ")[0]
    if uInput == "e" or uInput == "d":
        text = input("Please input text you wish to be parsed: ").lower()
        caesar = int(input("Please input your caesar: "))
        print("Your output is: ", func(text, caesar, uInput))
        
