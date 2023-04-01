import json
from difflib import get_close_matches
d=json.load(open("076 data.json"))

def find():
    key=input("Enter Your word: ")
    key.lower()
    if key in d:
        for i in d[key]:
            print(i)
    elif len(get_close_matches(key,d.keys()))>0:
        print("Did you mean ",get_close_matches(key,d.keys())[0]," instead?(Y/N)")
        confirm=input()
        if confirm=="Y":
            if len(get_close_matches(key,d.keys()))>1 :
                for i in get_close_matches(key,d.keys()):
                    print(d[i])
            else:
                print(d[get_close_matches(key,d.keys())])
        else:
            print("Sorry the Word is Incorrect!")
    else:
        print("The Word doesn't Exists.Please Double Check it!")
print("\n\nYou have opened DICTIONARY\n   Welcome to Dictionary\n\t  by KED")
find()
