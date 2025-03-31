keysDict = {'abbey': 'a', 'amber': 'b', 'bliss': 'c', 'breeze': 'd', 'cactus': 'e', 'cloud': 'f', 'daisy': 'g', 'dawn': 'h', 'eagle': 'i', 'echo': 'j', 'falcon': 'k', 'feast': 'l', 'garden': 'm', 'glow': 'n', 'harmony': 'o', 'haven': 'p', 'ice': 'q', 'ivory': 'r', 'jade': 's', 'jazz': 't', 'koala': 'u', 'lagoon': 'v', 'luna': 'w', 'marvel': 'x', 'meadow': 'y', 'nebula': 'z', 'neck' : ' ', 'nest': '0', 'oasis': '1', 'ocean': '2', 'palm': '3', 'pearl': '4', 'quartz': '5', 'quest': '6', 'rain': '7', 'river': '8', 'serene': '9'}

def get_key(val):
    for key, value in keysDict.items():
        if value == val:
            return key

def encode(text):
    encoded_text = ''
    for char in text.lower():
        if char in keysDict.values():
            key = get_key(char)
            encoded_text += key + " "
        else:
            encoded_text += f"Character '{char}' not found in the dictionary" + " "
    
    return encoded_text

def decode(encodedText):
    decoded_text = ''
    for word in encodedText.split():
        if word in keysDict.keys():
            decoded_text += keysDict[word]
    return decoded_text


print(encode("bonjour jules"))

print(decode(encode("bonjour jules")))
