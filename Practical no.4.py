def bubbleSort(arr, n):
    index = list(range(1, n + 1))

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                index[j], index[j+1] = index[j+1], index[j]

    return index


def selectionSort(arr, n):
    index = list(range(1, n + 1))

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        index[i], index[min_idx] = index[min_idx], index[i]

    return index


def putdata(arr, n):
    print('\n\nFollowing are the percentages of all the students...\n')
    print('**********************************')
    print('|    Roll No    |   Percentage   |')
    print('**********************************')

    for i in range(n):
        print(f'|\t{i + 1}\t|\t{arr[i]}%\t |')
    print('----------------------------------\n\n')


def putsorteddata(arr, n):
    print('\n**********************************')
    print('|    Roll No    |   Percentage   |')
    print('**********************************')

    for i in range(n):
        print(f'|\t{arr[i][0]}\t|\t{arr[i][1]}%\t |')
    print('----------------------------------\n\n')


def main():
    n = int(input('\nEnter number of student in 1st year: '))
    arr = []

    for i in range(n):
        arr.append(int(input(f'Enter percentage of roll no {i + 1}: ')))

    putdata(arr, n)
    arr2 = arr[:]
    n = len(arr)

    print('Sorting all the percentages using Bubble Sort:')
    index = bubbleSort(arr, n)
    putsorteddata(list(zip(index, arr)), n)

    print('Sorting all the percentages using Selection Sort:')
    index = selectionSort(arr2, n)
    putsorteddata(list(zip(index, arr2)), n)


if __name__ == "__main__":
    main()
B14. practical code.txt
Displaying B14. practical code.txt.
B14. Practical Code
Shivali Mali
•
Sep 25

B14. practical code.txt
Text
Class comments
