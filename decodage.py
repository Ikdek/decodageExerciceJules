import string

oldRempWord = {'rhubarb', 'quince', 'watermelon', 'ximenia', 'nut', 'zucchini','blackberry', 'vine', 'cranberry','durian', 'papaya', 'huckleberry', 'jujube', 'xerophyte', 'elderberry','tangerine', 'satsuma','kiwi', 'victoria', 'lime', 'saffron', 'ugni', 'rasp', 'kale', 'avocado','xigua', 'ugly','waxberry', 'eggplant', 'honeydew', 'lychee', 'dragonfruit', 'zinfandel','raspberry', 'guava','indian', 'fig', 'orange', 'yuzu', 'date', 'tamarind', 'yam', 'strawberry','hawthorn', 'apple','nectarine', 'cherry', 'fennel', 'elderflower', 'quandary', 'blueberry','quandong', 'zest','wildberry', 'yellow', 'apricot', 'onion', 'cantaloupe', 'nutmeg','persimmon', 'mandarin', 'olive','lemon', 'tamarillo', 'ugli', 'mango', 'grape', 'banana', 'jackfruit','gooseberry', 'vanilla','mulberry', 'kumquat', 'peach', 'feijoa'}

def findKeys(encodedString): # finds keys in encoded string by comparing with oldRempWord
    return  " ".join(word for word in encodedString.split() if word.lower() not in oldRempWord)

def defKeys(keyString : str): # define keys by alphabetical order
    alphaCle = sorted(keyString.lower().split())
    alphaB = string.ascii_lowercase

    cleDict = {}
    for indexCle in range(len(alphaCle)):
        if (indexCle < 26):
            cleDict[alphaCle[indexCle]] = alphaB[indexCle]
        else: 
            cleDict[alphaCle[indexCle]] = str(indexCle - 26)
    return cleDict

def decode(encodedString : str, cleDict): # decode the string by replacing keys with values
    decodedString = ""

    for newWord in encodedString.split():
        if newWord.lower() in cleDict:
            decodedString += str(cleDict[newWord.lower()]) 
    return decodedString.strip()

def decodeAll(): # real case scenario 
    with open("oldText.txt", "r") as oldText: 
        oldTextString = oldText.read()

    with open("text.txt", "r") as Text:
        TextString = Text.read()

    keyString = findKeys(oldTextString)
    cleDict = defKeys(keyString)
    decodedText = decode(TextString, cleDict)
    print("\n----------------------------------\n")
    print("Keys:", keyString)
    print("\n----------------------------------\n")
    print("Dictionary:", cleDict)
    print("\n----------------------------------\n")
    print("Decoded Text:", decodedText)
    print("\n----------------------------------\n")

decodeAll()
