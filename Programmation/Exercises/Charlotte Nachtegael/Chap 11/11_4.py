def belongs_to_dictionary(s):
    file = open('words.txt','r')
    dictionary = file.readlines()
    res = False
    for line in dictionary:
        line = line.strip()
        if line == s:
            res = True
    return res

print(belongs_to_dictionary('prince'))