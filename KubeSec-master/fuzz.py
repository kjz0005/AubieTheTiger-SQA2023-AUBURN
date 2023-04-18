import scanner

def fuzzValues():
    # testing scanner methods
    print (scanner.scanKeys("hello", "hello2"))
    print (scanner.scanPasswords("pass123", "hello2"))
    print (scanner.scanUserName(None, "hello2"))
    print (scanner.isValidPasswordName(None))
    print (scanner.isValidUserName(12345))

def simpleFuzzer(): 
    fuzzValues()


if __name__=='__main__':
    simpleFuzzer()