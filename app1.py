from difflib import get_close_matches
import json
data = json.load(open("data.json"))
def translate(w):
        w = w.lower()
        if w in data:
            return data[w]
        elif len(get_close_matches(w, data.keys()))>0:
            yn =  input("Incorrect spelling, do you mean %s : press Y or N \n " % get_close_matches(w, data.keys())[0])
            loweryn = yn.lower()
            if loweryn =="y":
                return data[get_close_matches(w, data.keys())[0]]
            else:
                return "Recheck the word or enter another word"
        else:
            print ("no match found, retry another word")
word = input("Input a word to translate:\n ")

output = (translate(word))
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
