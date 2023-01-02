import random


def makeTab():
    tab = set()
    while len(tab) != 100:
        tab.add(random.randrange(1000))
    return tab


def bubbleSort(tab):
    tab = list(tab)
    sorted = 1

    while sorted != len(tab):
        for i in range(len(tab) - 1):
            if tab[i] > tab[i + 1]:
                #temp = tab[i]
                #tab[i] = tab[i + 1]
                #tab[i + 1] = temp

                tab[i], tab[i+1] = tab[i+1], tab[i]
            else:
                i += 1
        sorted += 1
    return tab


if __name__ == '__main__':
    tabToSort = makeTab()
    print(tabToSort)
    sortedTab = bubbleSort(tabToSort)
    print(sortedTab)

    autoSort = list(tabToSort)
    autoSort.sort()
    print(autoSort)

    if autoSort == sortedTab:
        print("Good")
