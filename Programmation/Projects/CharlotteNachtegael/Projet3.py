"""
Projet 3 - Gestion d'agenda
Filter the events of a calendar according to several filters
"""
__author__ = "Charlotte Nachtegael - 000425456 - Groupe TP 1"

import sys
import codecs


def is_ok_filter(s, filters):
    """
    Receive string s and list of parameters list_argu and return true
    if it conforms to at least one filter desired
    """
    res = False
    n = len(filters)  # number of filters
    i = 0
    while not res and i < n:  # test the until the string is conform to a filter or all the filters were tested
        nb_ok = 0  # number of parameters conformed
        for j in range(len(filters[i])):  # test all the parameters in the filter,
            if filters[i][j][-1] in s:
                nb_ok += 1
        if nb_ok == len(filters[i]):  # if all the desired are in the string, res = True
            res = True
        i += 1
    return res


# obtain all the arguments
list_argu = sys.argv

fileIN = list_argu[1]
fileOUT = list_argu[2]

# formate the arguments so they can be used
# to filter the events :
# the sublist is one filter composed of several
# subsets (parameters),themselves divided in two parts,
# the parameter itself and the one desired
final_list = []
for elem in list_argu[3:]:
    elem = elem.split('and')
    final_list.append(elem)
for i in range(len(final_list)):
    for j in range(len(final_list[i])):
        final_list[i][j] = final_list[i][j].strip().split(':')

fd = codecs.open(fileIN, "r", "utf-8")
line = fd.readline()

head = ""

# set the headers of the file in var head
while line != "BEGIN:VEVENT\r\n":
    head += line
    line = fd.readline()

# set the events conforming to at least one filter in a list
filtered_list = []
while line != "END:VCALENDAR\r\n":
    newEvent = line
    line = fd.readline()
    while line != "END:VEVENT\r\n":
        newEvent += line
        line = fd.readline()
    newEvent += line
    if is_ok_filter(newEvent, final_list):
        filtered_list.append(newEvent)
    line = fd.readline()

# last line
tail = line
fd.close()

# write the list of events into the out file
file = codecs.open(fileOUT, 'w', 'utf-8')
file.write(head)
for i in range(len(filtered_list)):
    file.write(filtered_list[i])
file.write(tail)
file.close()
