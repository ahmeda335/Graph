# This is a code for HeapQueue including (MiniHeapify, MaxHeapify, and pop).
# I didn't use it in my codes.
# It is possible to find an implementation simpler than this implementation.

# Importing HeapQueue library
import heapq


# This is a function for mini heapifying that I made myself.
# It is O(n).
def miniHeapify(lst):
    for i in range(len(lst)):
        child1 = (len(lst) - i) * 2
        child2 = ((len(lst) - i) * 2) + 1
        if child1 <= len(lst):
            if lst[len(lst) - i - 1] > lst[child1 - 1]:
                lst[len(lst) - i - 1], lst[child1 - 1] = lst[child1 - 1], lst[len(lst) - i - 1]
        if child2 <= len(lst):
            if lst[len(lst) - i - 1] > lst[child2 - 1]:
                lst[len(lst) - i - 1], lst[child2 - 1] = lst[child2 - 1], lst[len(lst) - i - 1]
    for i in range(len(lst)):
        child1 = (i + 1) * 2
        child2 = ((i + 1) * 2) + 1
        if child1 <= len(lst):
            if lst[i] > lst[child1 - 1]:
                lst[i], lst[child1 - 1] = lst[child1 - 1], lst[i]
        if child2 <= len(lst):
            if lst[i] > lst[child2 - 1]:
                lst[i], lst[child2 - 1] = lst[child2 - 1], lst[i]
    return lst


# This is a function for max heapifying that I made myself.
# It is O(n).
def maxHeapify(lst):
    for i in range(len(lst)):
        child1 = (len(lst) - i) * 2
        child2 = ((len(lst) - i) * 2) + 1
        if child1 <= len(lst):
            if lst[len(lst) - i - 1] < lst[child1 - 1]:
                lst[len(lst) - i - 1], lst[child1 - 1] = lst[child1 - 1], lst[len(lst) - i - 1]
        if child2 <= len(lst):
            if lst[len(lst) - i - 1] < lst[child2 - 1]:
                lst[len(lst) - i - 1], lst[child2 - 1] = lst[child2 - 1], lst[len(lst) - i - 1]
    for i in range(len(lst)):
        child1 = (i + 1) * 2
        child2 = ((i + 1) * 2) + 1
        if child1 <= len(lst):
            if lst[i] < lst[child1 - 1]:
                lst[i], lst[child1 - 1] = lst[child1 - 1], lst[i]
        if child2 <= len(lst):
            if lst[i] < lst[child2 - 1]:
                lst[i], lst[child2 - 1] = lst[child2 - 1], lst[i]
    return lst


# My own pop function
# It is O(logn)
def pop(lst):
    popvalue = lst[0]
    lst[0] = lst[-1]  # Copying the value of the last element to the root.
    lst = lst[:len(lst) - 1]  # Deleting the last element
    # Rearranging the heap
    i = 0
    child1 = 2 * (i + 1)
    child2 = (2 * (i + 1)) + 1
    while (child1 or child2) <= len(lst):
        if child1 <= len(lst):
            if lst[i] > lst[child1 - 1]:
                lst[i], lst[child1 - 1] = lst[child1 - 1], lst[i]
        if child2 <= len(lst):
            if lst[i] > lst[child2 - 1]:
                lst[i], lst[child2 - 1] = lst[child2 - 1], lst[i]
        i += 1
        child1 = 2 * (i + 1)
        child2 = (2 * (i + 1)) + 1

    return lst


list1 = [3, 13, 14, 5, 10, 11, 7, 9, 20, 22]
list2 = [5, 10, 22, 27, 30, 9, 11, 12, 25, 5]

print("The output before heapifying:")
print(list1)
print(list2)
print('=' * 50)

##################################################
heapq.heapify(list1)
heapq.heapify(list2)

print("The output after the first heapify:")
print(list1)
print(list2)
print('=' * 50)

#################################################
# Mini Heapifying using my own function.
print("Mini Heapifying using my function:")
print(miniHeapify(list1))
print(miniHeapify(list2))
print('=' * 50)

################################################
heapq.heappush(list1, 4)
heapq.heappush(list2, 4)

print("The output after pushing '4' in both lists")
print(list1)
print(list2)
print('=' * 50)

#################################################
heapq.heappop(list1)
heapq.heappop(list2)

print("The output after poping the smallest element from both lists:")
print(list1)
print(list2)
print('=' * 50)

################################################
# Poping using my own function.
print("poping using my own function:")
print(pop(list1))
print(pop(list2))
print('=' * 50)


################################################
# This will push then pop the smallest element, so the output in "heappushpop" in this case is '1'.
heapq.heappushpop(list1, 1)
heapq.heappushpop(list2, 1)

print("The output after heappushpop(list, 1) in both lists:")
print(list1)
print(list2)
print('=' * 50)


################################################
# This will pop the smallest element first then push, so the output in "heapreplace" in this case
# is '3' in list1 and '4' in list2.
heapq.heapreplace(list1, 1)
heapq.heapreplace(list2, 1)

print("The output after heapreplace(list, 1) in both lists:")
print(list1)
print(list2)
print('=' * 50)


################################################
# printing the 'k' smallest and biggest values in heapqueue.
print("The samallest 4 numbers are:")
print(heapq.nsmallest(4, list1))
print(heapq.nsmallest(4, list2))
print("The biggest 4 numbers are:")
print(heapq.nlargest(4, list1))
print(heapq.nlargest(4, list2))
print('=' * 50)

################################################
# Merging the two lists into one list.
list3 = heapq.merge(list1, list2)
print("After merging two lists:")
print(*list3)
print('=' * 50)

################################################
# Ordering the list in ascending order.
list4 = []
list5 = []
for i in range(len(list1)):
    list4.append(heapq.heappop(list1))
    list5.append(heapq.heappop(list2))

print("The two lists after ordering them:")
print(list4)
print(list5)
print('=' * 50)

#################################################
# Max Heapifying using my own function.
print("Max Heapifying using my function:")
print(maxHeapify(list1))
print(maxHeapify(list2))
print('=' * 50)

