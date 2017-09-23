"""
Algorithms in computational Biology (INfailureoutput-failure438)
Assignment 3 : using a finite state pattern matching automata, identify pattern in a text in O(m) time.
Configuration needed : Python 3 and superior version.
"""

__author__ = 'Charlotte Nachtegael'
__date__ = '05/05/2016'

def letter_keyword(keywords):
    """
    In the aim to study only the symbols of interest, we compute the symbols of the keywords
    :param keywords: set of keywords computed under the form of strings
    :return: set of symbols found in the keywords. The set allows a search faster than with a list.
    """
    letters = []
    for keyword in keywords:
        for letter in keyword:
            if letter not in letters:
                letters.append(letter)
    return set(letters)


def goto_construction(keywords, letters):
    """
    The function built a graph starting from the state 0. The vertices of the graph are new states connected by edges
    corresponding to the letters of the keywords. If the prefixes of keywords overlap, the edges will be added only
    when the second keyword differs from the first keywords in the graph. The function also build a partial output
    function
    :param keywords: set of keywords in the form of strings
    :param letters: set of letters found in the keywords
    :return: goto graph in the form of a dictionary, where the key is a tuple composed of the state we start from
    (vertex) and the current symbol composing the keyword (edge) and the value is the next state (vertex).
    Output function in the form of a dictionary where the key is the state when the keyword is finished (vertex)
    and the value is a set with the keyword in the form of a string. The output is partially completed as some
    keywords can overlap each other, but in this case we only have one state for one keyword.
    Dictionaries were chosen for the speed of the search higher than with list.
    """
    newstate = 0
    goto = {}
    output = {}

    # build the graph with the keywords
    for keyword in keywords:
        state = 0
        j = 0

        # look if the keyword does not overlap with another
        # allows to create edges only if necessary
        while (state,keyword[j]) in goto:
            state = goto[(state, keyword[j])]
            j += 1

        # add new edges to the graph
        while j < len(keyword):
            newstate += 1
            goto[(state, keyword[j])] = newstate
            state = newstate
            j += 1

        # when keyword completely added to the graph, the last state is the state where we can confirm
        # we have the keyword as input
        output[state] = {keyword}

    # for the letters found in the keywords, but not the first letters of the keywords
    # we stay at the root vertex of state 0
    for symbol in letters:
        if (0, symbol) not in goto:
            goto[(0, symbol)] = 0

    return goto, output


def failure_construction(goto, output, letters):
    """
    The failure function allows to find alternate paths when the path we are engaged in cannot be
    completed as the next symbol does not correspond. It computes the failure of the states of a depth d
    (depth being the length needed to reach the state starting from the root state) by looking at
    all the states of the depth d-1 and look if a new path can be found. This also allows to merge the ouputs
    of keywords overlapping each other as finding an alternative path can be explained by overlapping keywords.
    :param goto: dictionary containing the goto graph with the key being a tuple of the start state and a symbol
    and the value being the next state
    :param output: dictionary containing the keywords as value obtained for each states as key
    :param letters: set of the letters found in the keywords
    :return: failure function in the form of a dictionary where the key is the state we want to know
    the state where it can transition to if the symbol does not correspond to the defined path and the value
    is the state it can transition to.
    The output dictionary is also updated with the keywords overlapping each other.
    Dictionaries were chosen to speed up the search.
    """
    queue = []
    failure = {}

    # state of depth 1 have a failure state of 0
    for letter in letters:
        if (0, letter) in goto and goto[(0, letter)] != 0:
            queue.append(goto[(0, letter)])
            failure[goto[(0, letter)]] = 0

    # compute the others failures states
    while len(queue) != 0:

        # queue is a first-in, first-out list
        r = queue[0]
        queue = queue[1:]

        # look only in letters of interest
        for letter in letters:

            # add the failure of d from d-1
            if (r, letter) in goto:
                s = goto[(r, letter)]
                queue.append(s)
                state = failure[r]

                # until a path is found for the letter coming form the state s
                while (state, letter) not in goto:
                    state = failure[state]
                failure[s] = goto[(state, letter)]

                # merge outputs if the alternative path found is also an output
                if failure[s] in output:
                    output[s].update(output[failure[s]])

    return failure, output


def next_function(goto,failure,letters):
    """
    The next function is built from the goto graph and the failure function to avoid useless transition in case
    of failure. A deterministic automaton is built so that for all the states of the goto and all the letters of
    the keywords we can determine a next state S.
    :param goto: dictionary containing the goto graph with the key being a tuple of the start state and a symbol
    and the value being the next state
    :param failure: dictionary containing as a value the state where we should transition to when we fail to fill
    the condition of the current state (key)
    :param letters: set of the letters found in the keywords
    :return: next function in the form of a dictionary with the key being the state and the next symbol and the
    value the state where we should transition to.
    """
    queue = []
    next = {}

    # the state 0 transitions in the same way as in the goto graph
    for letter in letters:
        next[(0, letter)] = goto[(0, letter)]

        if goto[(0, letter)] != 0:
            queue.append(goto[(0, letter)])

    # look for all states for all letters
    while len(queue) != 0 :
        r = queue[0]
        queue = queue[1:]
        for letter in letters:

            # the path is valid
            if (r, letter) in goto:
                s = goto[(r, letter)]
                queue.append(s)
                next[(r, letter)] = s

            # alternative path must be found
            else:
                next[(r, letter)] = next[(failure[r], letter)]

    return next


def pattern_matching(text, output, next, letters):
    """
    The function processes the text symbol by symbol until one symbol can be found in the keywords.
    The next function allows to check to which state we transition to from the current state and the current symbol.
    If the state we transition to correspond to the end of a keyword, the localization and the keyword are computed
    into a dictionary.
    :param text: string with text in which you want to find the localization of the keywords
    :param output: output: dictionary containing the keywords as value obtained for each states as key
    :param next: a dictionary where the key is the current state and the current symbol and the value is the state
    where we should transition to.
    :param letters: set of the letters found in the keywords
    :return: A dictionary with the localizations (position of the last letter of the keyword) as keys and the keywords
    found at these localizations as values
    """
    state = 0
    localization = {}

    for i in range(len(text)):
        if text[i] in letters:
            state = next[(state,text[i])]
            if state in output:
                localization[i] = output[state]
        else:
            state = 0
    return localization

if __name__ == '__main__':
    K = {'pattern', 'tree', 'state', 'prove', 'the', 'it'}
    letters = letter_keyword(K)
    goto, output = goto_construction(K, letters)
    failure, output = failure_construction(goto, output, letters)
    next = next_function(goto, failure, letters)
    text = """As discussed in the session on Combinatorial Pattern Matching, keywords trees provide an efficient solution to search for multiple k patterns in a text of length n. The algorithm requires first the construction of a keyword tree and then, using naïve threading, the patterns can be identified in O(nm), where n is the average length of the k patterns and m is the length of the text. Alfred Aho and Margaret Corasick proposed in 1975 a more efficient solution that allows one to identify the patterns in O(m) time. To achieve this improvement, the keyword tree is replaced by a finite state pattern matching automata. Once this machine is constructed the text can be processed and the starting positions for the different patterns can be returned as output. The full specification of the Aho-Corasick algorithm is provided in the original article included with this assignment."""
    text = text.lower()
    localization = pattern_matching(text, output, next, letters)

print(localization)