import random      #to import a module

#to run a random no
num = random.random()                     

def encrypt(sttr, enkey=str(num)):
    return enkey.join(sttr)

""""
def decrypt(sttr, enkey=str(num)):
    with open("encryption.txt",'r'):
        data=f.read()
        result=data.split(enkey)
    return result
   """
def decrypt(sttr,enkey):
    return sttr.split(enkey)    

# to take a word from user
try:
    text = input("Enter any text: ")  

#to make a choice from user
    print('''Enter your choice:
        1.Encrypt
        2.next time
        ''')
    choice = int(input("Eneter your choice: "))

    if(choice == 1):
        with open("Encrypt.txt", 'a') as f:     #to open a file in text file
            f.write(encrypt(text))              #to write anything in that file
        print(encrypt(text))                    #to print the word i.e encrypted from the file

    elif (choice == 2):
        """"
        with open("Encrypt.txt", 'r') as f1:
            data = f1.read()
            print(data)
            #print(decrypt(str(data), f1))
            #print(decrypt(text, str(num)))
        """
        print("try again later")    

    #elif (choice==2):
        #print(decrypt(text))

    
    else:
        print("Invalid Input!!!")             #if the user enter a no other than the option
except ValueError :
    print("Please Run Again.....")
    #print(e)