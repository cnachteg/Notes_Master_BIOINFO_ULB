"""
Projet 4 : résolution de systèmes linéaires
Résolution de systèmes d'équations linéaires carrées par combinaison linéaire
"""

__author__ = "Charlotte Nachtegael"
__date__ = "10 décembre 2015"


def solve_system():
    """
    :return: solution of a system of linear equation or None if the system is impossible or undetermined
    """
    system = encode_system()
    sysTriangulaire = triangulation(system)
    solution = substitution(sysTriangulaire)
    print("Solution:")
    print(solution)


def encode_system():
    """
    :return: system of n equations with n variables
    """
    # input of variables
    not_numbers = False
    all_different = False
    while not not_numbers or not all_different:
        print("Please choose your variables (letters between a and z separated by a space)")
        var = input()
        list_var = var.split()
        try:
            for i in range(len(list_var)):
                if not (96 < ord(list_var[i]) < 123):
                    raise TypeError
            not_numbers = True
            for i in range(len(list_var) - 1):
                for j in range(i + 1, len(list_var)):
                    if list_var[i] == list_var[j]:
                        raise Exception
            all_different = True
        except (TypeError, Exception):
            print("Nice try, but all your variables must be letters between 'a' and 'z' and different ! Try again :)")
    list_var.append('ti')

    # input of the coefficients for the equations
    nb_equations = len(list_var)
    list_coefficients_all = []
    for i in range(1, nb_equations):
        print("Equation", i, ":")
        nb_coeff = False
        all_numbers = False
        while not nb_coeff or not all_numbers:
            print("Coefficients of", var, "and the independent term :")
            coeff = input()
            list_coeff = coeff.split()
            try:
                # test of enough number of coefficients
                if len(list_coeff) != len(list_var):
                    raise ValueError
                else:
                    nb_coeff = True

                # all the input are numbers
                for j in range(len(list_coeff)):
                    list_coeff[j] = int(list_coeff[j])
                all_numbers = True
            except:
                print(
                    "Error : All coefficients must be integers or you did not give the good amount of coefficients !")
        list_coefficients_all.append(list_coeff)

    # encode the equations in dictionaries
    system = []
    for i in range(len(list_coefficients_all)):
        equation = {}
        for j in range(len(list_coefficients_all[0])):
            equation[list_var[j]] = list_coefficients_all[i][j]
        system.append(equation)

    print("Linear system encoded :")
    print_system(system, list_var)

    return system


def print_system(system, list_var):
    """
    :param system: system (list) of several equations in the form of dictionaries
    :param list_var: list of the variables of the equations
    :return: a print of the equations in the system
    """
    for i in range(len(system)):
        if system[i][list_var[0]] > 0:
            if system[i][list_var[0]] == 1:
                print(list_var[0], end=' ')
            else:
                print(str(system[i][list_var[0]]) + list_var[0], end=' ')
        elif system[i][list_var[0]] < 0:
            if system[i][list_var[0]] == -1:
                print('-' + list_var[0], end=' ')
            else:
                print(str(system[i][list_var[0]]) + list_var[0], end=' ')
        for j in range(1, len(list_var)):
            if list_var[j] == 'ti':
                if system[i][list_var[j]] > 0:
                    print('+', system[i][list_var[j]], end=' ')
                elif system[i][list_var[j]] < 0:
                    print('-', abs(system[i][list_var[j]]), end=' ')
            elif system[i][list_var[j]] > 0:
                if system[i][list_var[0]] != 0:
                    print('+', end=' ')
                if system[i][list_var[j]] == 1:
                    print(list_var[j], end=' ')
                else:
                    print(str(system[i][list_var[j]]) + list_var[j], end=' ')
            elif system[i][list_var[j]] < 0:
                print('-', end=' ')
                if system[i][list_var[j]] == -1:
                    print(list_var[j], end=' ')
                else:
                    print(str(abs(system[i][list_var[j]])) + list_var[j], end=' ')
        print('=', 0)


def triangulation(system):
    """
    :param system: system (list) of several equations in the forms of dictionaries
    :return: a triangular system if possible, None if undetermined or impossible to solve
    """

    def check_equations(sysTriangulaire, variables):
        """
        :param sysTriangulaire: system (list) of several equations in the forms of dictionaries
        :param variables: list of variables used in the equations
        :return: the system if it is solvable, None if undetermined or impossible to solve
        """
        nb_eq_total = len(sysTriangulaire)
        nb_eq_check = 0
        zero_variable = False
        # check the coefficient for each variables until one equation with no variable is found
        while not zero_variable and nb_eq_check < nb_eq_total:
            nb_zero = 0
            for x in range(len(variables)):
                if sysTriangulaire[nb_eq_check][variables[x]] == 0:
                    nb_zero += 1
            nb_eq_check += 1
            if nb_zero == len(variables):
                zero_variable = True
        if not zero_variable:
            res = sysTriangulaire
        else:
            res = None
        return res

    sysTriangulaire = []
    variables = []
    nb_eq = len(system)
    # compute the triangular system
    for elem in system[0]:
        if elem is not 'ti':
            variables.append(elem)
        variables.sort()
    nb_variables = len(variables)
    for i in range(nb_variables - 1):
        for j in range(i, nb_eq - 1):
            for k in range(j + 1, nb_eq):
                system[k] = compute_combili(system[j], system[k], variables[i])
        sysTriangulaire.append(system[i])
    sysTriangulaire.append(system[-1])
    res = check_equations(sysTriangulaire, variables)
    return res


def compute_combili(equation1, equation2, var_elimi):
    """
    :param equation1: dictionary with the coefficients and variables of an equation
    :param equation2: dictionary with the coefficients and variables of an equation
    :param var_elimi: string of the variable to eliminate
    :return: one dictionnary with the coefficients and variables of an equation resulting
    of a linear combination of equation1 and equation 2 with the coefficient of the var_elimi
    equal to 0
    """

    def ppcm(x, y):
        """
        :param x: number 1
        :param y: number 2
        :return: smallest multiple in common of number 1 and 2
        """

        def pgcd(x, y):
            """
            :param x: number 1
            :param y: number 2
            :return: the biggest common divisor of number 1 and 2
            """
            if y == 0:
                res = x
            else:
                res = pgcd(y, x % y)
            return res

        divisor = pgcd(x, y)
        if divisor == 0:
            res = 0
        else:
            res = x * y / divisor
        return res

    # calculate the coefficient for the linear combination
    coeff_eq1, coeff_eq2 = equation1[var_elimi], equation2[var_elimi]
    multiple_in_common = ppcm(abs(coeff_eq1), abs(coeff_eq2))
    if multiple_in_common == 0:
        res = equation2
    else:
        c1 = multiple_in_common / coeff_eq1
        c2 = multiple_in_common / coeff_eq2
        # compute the final equation with the coefficient of var_elimi equal to 0
        equation_final = {}
        for elem in equation1:
            if abs(equation1[elem] * c1) + abs(equation2[elem] * c2) == 0:
                equation_final[elem] = 0.0
            elif abs(equation1[elem] * c1 - equation2[elem] * c2) / (
                        abs(equation1[elem] * c1) + abs(equation2[elem] * c2)) < 1e-05:
                equation_final[elem] = 0.0
            else:
                equation_final[elem] = equation1[elem] * c1 - equation2[elem] * c2
        res = equation_final
    return res


def substitution(sysTriangulaire):
    """
    :param sysTriangulaire: triangular system of several equations in the form of dictionaries or None
    :return: the solution set of the system in the for of a dictionary
    """
    if sysTriangulaire == None:
        solution = None
    else:
        nb_eq = len(sysTriangulaire)
        variables = []
        solution = {}
        for elem in sysTriangulaire[0]:
            if elem is not 'ti':
                variables.append(elem)
        variables.sort()
        for i in range(nb_eq - 1, -1, -1):
            if sysTriangulaire[i][variables[i]] == 0:
                solution[variables[i]] = 0.0
            else:
                solution[variables[i]] = sysTriangulaire[i]['ti'] * (-1) / sysTriangulaire[i][variables[i]]
                if solution[variables[i]] == -0.0:
                    solution[variables[i]] = 0.0
                if i > 0:
                    for elem in solution:
                        sysTriangulaire[i - 1]['ti'] = sysTriangulaire[i - 1]['ti'] + (
                            sysTriangulaire[i - 1][elem] * solution[elem])
                        sysTriangulaire[i - 1][elem] = 0
    return solution


if __name__ == "__main__":
    solve_system()
