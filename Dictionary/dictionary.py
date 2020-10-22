import json
from difflib import get_close_matches
data=json.load(open("data.json")) ##Retrieving data from json file
word=input("enter the word you want to search-->")
def translate(word):
    word=word.lower()#First converting all in lower
    if word in data:
        return data[word]
    elif word.title() in data:#Only the first letter will be capital
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]#All the word will be upper letters
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean %s instead"%get_close_matches(word,data.keys())[0])#For getting the closer matches if the user give nearly right input
        decide=input("press y for yes or n for no")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            print("Then you have entered wrong word,kindly search again !")
        else:
            print("Please press y or n to find result")


    else:
        print("You have entered wrong word or it is not present in database")
output=translate(word)

if type(output)==list:  #For better experience of user and to make the output more readable
    for item in output:
        print(item)
else:
    print(output)
##Important methods->data.keys()->it will fetch all the key terms from the data
#->get_close_matches(str,list,cutoff=0.8/0.5/0/1)#cutoff for accuracy