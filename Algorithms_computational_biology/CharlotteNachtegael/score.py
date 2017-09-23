def score(protein, coordinates):
    length_fold = len(coordinates)
    length_prot = len(protein)
    number_bonds_for_H = {}
    score = 0
    i = 0

    for residue in range(length_prot):
        if protein[residue] == 'H':
            number_bonds_for_H[str(residue)] = 0

    while length_fold > 4 and i < length_fold:
        if protein[i] == 'H':
            x_first_H, y_first_H = coordinates[i]
            for j in range(i + 3, length_fold, 2):
                if protein[j] == 'H':
                    x_second_H, y_second_H = coordinates[j]
                    if abs(x_first_H - x_second_H) + abs(y_first_H - y_second_H) == 1:
                        score += 1
                        number_bonds_for_H[str(i)] += 1
                        number_bonds_for_H[str(j)] += 1

        i += 1

    i = 0
    if length_fold < length_prot:
        while i < length_prot:
            if protein[i] == 'H':

                # residues can only have 3 hydrogen bonds maximum
                # H residues at extremities can have 3 hydrogen bonds, other H residues 2 maximum
                if (i == 0 or i == length_prot - 1 and number_bonds_for_H[str(i)] < 3) or \
                        (0 < i < length_prot - 1 and number_bonds_for_H[str(i)] < 2):
                    print("i =", i)

                    # look only to the residues that are not yet placed in the grid
                    for j in range(i + 3, length_prot, 2):
                        print(j)
                        if j > length_fold - 2 and protein[j] == 'H':
                            print("j=",j)
                            if j == length_prot - 1 and number_bonds_for_H[str(j)] < 3:
                                score += 1
                                number_bonds_for_H[str(i)] += 1
                                number_bonds_for_H[str(j)] += 1
                            elif j != length_prot - 1 and number_bonds_for_H[str(j)] < 2:
                                score += 1
                                number_bonds_for_H[str(i)] += 1
                                number_bonds_for_H[str(j)] += 1
            i+=1
    print(number_bonds_for_H)
    return score

x = [(0,2),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(3,2),(3,1),(4,1),(4,0),(3,0)]
#prot = 'HPHHHHPPHPPH'
#prot = 'HHHPHPPHPHPPHHHPH'
#prot = 'HPPHPHP'
y = [(0,2),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(3,2)]
print(score(prot,[(0, 0), (1, 0)]))

#prot2='HPHPPHHPHPPHPHHPPHPH'
#print(score(prot2,[(0,0),(0,1)]))