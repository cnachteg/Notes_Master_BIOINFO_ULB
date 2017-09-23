"""
INFO-F413 : Data Structures and algorithms
Assignment 2 : Randomized Selection
Select the kth smallest element out of a collection of n elements using the quicksort algorithm,
but only sorting the part where you can find the kth smallest element of the list.
The expected number of comparisons in the worst case is : (2*n + 2*n * log(n/(n-k)) + 2*k * log((
n-k)/k))
"""

from math import log
from random import sample, randint


def create_list(n):
    """
    Create a list of n unsorted elements belonging to the interval [0,n*2[
    :param n: integer, number of elements for the list
    :return: list of n unsorted elements
    """
    return sample(range(n * 2), n)


def quick_select(list_to_sort, k, count):
    """
    Select the kth smallest element of a unsorted list by using the principle of the Quick Sort
    algorithm.
    :param list_to_sort: unsorted list of integers
    :param k: rank of the element we desired to find in the unsorted list (1 to the size of the
    list)
    :param count: number of comparisons done until now, integer
    :return: the kth smallest element and the number of comparisons done to find it
    """
    n = len(list_to_sort)

    # select a random element of the list and class all the others according to it
    pivot = list_to_sort[randint(0, n - 1)]
    list_to_sort.remove(pivot)
    list_under = []
    list_upper = []

    for element in list_to_sort:
        count += 1
        if element < pivot:
            list_under.append(element)
        elif element > pivot:
            list_upper.append(element)

    # determine if the kth smallest element is the pivot, in the list of elements smaller than
    # the pivot or bigger than the pivot
    if len(list_under) == k - 1:
        res = count, pivot

    elif len(list_under) > k - 1:
        res = quick_select(list_under, k, count)

    else:
        res = quick_select(list_upper, k - len(list_under) - 1, count)

    return res


def summary(count, n, k):
    """
    Compare between the observed average number of comparisons and the upper bound of expected
    number of comparisons, print the results and confirm if the upper bound is respected
    :param count: total number of comparisons for all the runs
    :param n: size of the list
    :param k: rank of the element we searched for
    """
    average = count / 1000
    expected_count = 2 * n + 2 * n * log(n / (n - k)) + 2 * k * log((n - k) / k)

    if average < expected_count:
        print("The above bound is respected with a average of %s against the expected number of "
              "comparisons of %s." % (average, expected_count))
    else:
        print("Error")
        print("Average : %s" % average)
        print("Expected : %s" % expected_count)


def main(n, k):
    """
    Run the Quick Select Algorithm 1000 times with a specified size for the list and rank to find,
    and confirm if it respects the upper bound of the number of comparisons
    :param n: integer, size of the list
    :param k: integer, rank of the smallest element of the list to look for
    """
    count = 0
    for i in range(1000):
        list_to_sort = create_list(n)
        # print(list_to_sort)
        newcount, element = quick_select(list_to_sort, k, 0)
        # print(element)
        count += newcount
    summary(count, n, k)


if __name__ == "__main__":
    n = int(input("Size of the list : "))
    k = int(input("Which element do you want to find ? "))
    main(n, k)
