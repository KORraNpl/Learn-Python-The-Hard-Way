directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(string):
    result = []
    words = string.split()
    for word in words:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stop:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        elif convert_number(word) is not None:
            result.append(('number', convert_number(word)))
        else:
            result.append(('error', word))

    return result