#This will calculate the value of the given index in the fibonacci sequence
def fibonacciCalculator(n, memo={}): 
    if n in memo:
        return memo[n]
    elif n<=2:
        result= 1
    else:
        result= fibonacciCalculator(n-1,memo)+fibonacciCalculator(n-2,memo)
    memo[n]= result
    return result

#This is to feed a dict with all required data (256 cz ASCII has 256 values in it)
def FibonacciSequence(memory={}):
    for i in range(256):
        memory[i]=fibonacciCalculator(i)
    return memory

#This will return the key of the given value in the dictionary
def findvalue(value):
    for i in range(256):
        if memory[i] == int(value):
            return i


#This will find the key's value in the Fibonacci sequence and use it to encrypt 
def encrypt (text):
    translatedText= ""
    for i in text:
        translatedText += str(memory[ord(i)]) + "99919" # ord converts characters to its ASCII value.
                                                        # 99919 is to split values while decrypting
    
    return translatedText[:-5] #Its necessarry. Because we need to get rid of the last 99919.


#This will call the 'findvalue' to reverse encryption
def decrypt (text):
    encryptedText= text.split("99919")
    decryptedText=""
    for i in encryptedText:
        decryptedText += chr(findvalue(i))
    return decryptedText


#Feeding the 'memory' dict with FibonacciSequence
memory=FibonacciSequence()


#This will keep the program in a loop until the user decides to leave
while(True):
    secim = input("Yapılacak işlemi seçiniz:\n=======================================\n1:Encryption\n2:Decryption\n3:Seçim döngüsünü kır\n=======================================\n")

    if secim=='1': #Encryption
        text=encrypt(input("Şifrelenmesini istediğiniz mesajı giriniz\n=======================================\n"))
        print(text)
    elif secim=='2':#Decryption
        text=decrypt(input("Çözülmesini istediğiniz mesajı giriniz\n=======================================\n"))
        print(text)
    elif secim=='3':#To end the loop
        break
    else: #If user inputs a undesired value, it will reject it and keep the user in the loop.
        print("Lütfen yukarıda verilen seçeneklerden birini giriniz.=======================================\n")