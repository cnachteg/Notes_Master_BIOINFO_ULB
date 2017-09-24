import codecs

def file_histogram(fileName):
    letter_count={}
    file = codecs.open(fileName,'r', 'utf-8-sig')
    text = file.readlines()
    file.close()
    for line in text:
        line = line.strip()
        for letter in line:
            if letter != '\n' and letter != '\r':
                if letter not in letter_count:
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1
    return letter_count


def vowels_histogram(fileName):
    vowels_count={}
    vowels={'A','E','I','O','U','Y','a','e','i','o','u','y'}
    file = codecs.open(fileName,'r', 'utf-8-sig')
    text = file.readlines()
    file.close()
    for line in text:
        suite = ""
        for letter in line:
            if letter in vowels:
                suite += letter
            elif len(suite) != 0 and letter not in vowels:
                if suite not in vowels_count:
                    vowels_count[suite] = 1
                else:
                    vowels_count[suite] += 1
                suite = ""
            else:
                suite = ""
    return vowels_count


def words_by_length(fileName):
    file = codecs.open(fileName,'r', 'utf-8-sig')
    text = file.readlines()
    file.close()
    words_length = {}
    for line in text:
        mot=""
        for letter in line:
            if letter.isalpha():
                mot += letter.lower()
            elif len(mot) != 0 and not letter.isalpha():
                if len(mot) not in words_length:
                    words_length[len(mot)] = {mot}
                else:
                    words_length[len(mot)].add(mot)
                mot = ""
            else:
                mot = ""
    return words_length
