import passwordGenerator as pg
import passwordSaver as ps
import pyperclip

password = ""
exit = False

while exit != True:
    Command = input("what do you want to do? commands: genPass, getPass, showKeys, quit  -")

    try:
        data = ps.loadPasswds("data.json")
    except:
        data = {};

    if Command == "genPass":
        pg.getPasswordChars()
        pg.getPasswordChars()
        test = pg.passwordChars
        
        password = pg.makePassword()
        print(password)
        
        command = input("do you wish to save this password? (y/n)")
        if command == "y":
            key = input("as what?")
            data[key] = password
            ps.savePasswd("data.json", data)
            print("Password saves as " + key)
        elif command == "n":
            print("Password not saved")
    elif Command == "getPass":
        key = input("password from where?")
        if key in data:
            print(data[key])
            pyperclip.copy(data[key])
            print("Password copied to clipboard")
        else:
            print("no password found")
    elif Command == "showKeys":
        for k in data:
            print(k)
    elif Command == "quit" or Command == "q":
        exit = True