
def to_pig_latin(sentence):
    i = 0
    while i < (len(sentence)-1):
        if sentence[i] in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
            while sentence[i] != ' ' and i < (len(sentence)-1):
                i +=1
            if i == len(sentence) -1:
                sentence = sentence[:i+1] + 'way' + sentence[i+2:]
            else:
                sentence = sentence[:i] + 'way ' + sentence[i+1:]
        elif sentence[i] not in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
            x =''
            while (sentence[i] != ' ' and sentence[i] not in {'a','e','i','o','u'}) and i < (len(sentence)-1):
                x += sentence[i]
                sentence = sentence = sentence[:i] + '' + sentence[i+1:]
            while sentence[i] != ' '  and i < (len(sentence)-1):
                i += 1
            if i == len(sentence) -1:
                sentence = sentence[:i+1] + 'a' + x + 'ay' + sentence[i+2:]
            else:
                sentence = sentence[:i] + 'a' + x + 'ay '+ sentence[i+1:]
        i +=1
    return sentence
def to_english(sentence):
    sentence = sentence.split(" ")
    english = ""
    for word in sentence:
        if word[:len(word) - 4:-1] == 'yaw':
            english += word[:len(word) - 3] + " "
        else:
            noay = word[:len(word) - 2]
            firstconsonants = noay.split("a")[-1]
            consonantsremoved = noay[:len(noay) - (len(firstconsonants) + 1)]
            english += firstconsonants + consonantsremoved + " "
    return english
