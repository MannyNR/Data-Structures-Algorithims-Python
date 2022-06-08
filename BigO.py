#Intro to Big O:

"""
Big O is a way of comparing 2 sets of code mathematically and seeing how efficient they run.

This is compared via time complexity and space complexity.
"""


# Time Complexity:

"""
Time complexity can be comparing the time it takes for code to execute and complete. However, time complexity is not measuring time itself.
The thing about time complexity that is interesting is that it is not measured in time. Because if you took the same code and ran it on a computer that runs twice as fast, it would complete twice as fast. It doesn't make the code any better just means the computer is better. So it is measured in the number of operations that it takes to complete something.
"""


#Space Complexity:

"""
There is also space complexity which measures the amount of memory/ram code is using. So even though ie code 1 is faster, if the company needs it to work with less capable devices or speed is not the priority it will be better to consider code that works best in space complexity.
"""


# Omega - Theta - Big O:
"""
There's Best case (Omega "Ω"), Average case (Theta "Θ") , and Worst case (Omicron/ Big O "O"). An example would be a sorted number list:

"Ω"      "Θ"      "O"
[1, 2, 3, 4, 5, 6, 7]

If they ask to find 1 in the list that would be Best case Omega "Ω" since it's the first element in the list and we would find it right away.

If finding 4 in the list, that would be Average case (Theta "Θ") since it's in the middle(average).

And Worst Case (Omicron "Big O") would be finding 7 since it is at the end of the list and we'd have to iterate through the entire list.
"""


# Tip:
"""
Big O is technically worst case however, some people refer to Omega as best case big O, and Theta as average case big O.
"""



# Big O: O(n)


# def print_items(n):
#   for i in range(n):
#     print(i)

# print_items(10)

"""
In this example we take n and pass it the number 10 and ran this operation n times(10). What ever n is, is the number of operations.

O(n) on a graph will always be a straight line and thus called "Proportional". So if I hear proportional they are talking about O(n)
"""


# Drop Constants

# def print_items(n):
#   for i in range(n):
#     print(i)
    
#   for j in range(n):
#     print(j)

# print_items(10)

"""
So for i this ran n times and this was also the case for j. Which would make this n+n=2n or O(2n) but we can simplify this by dropping the 2 and write it as O(n). So no matter what the constant is, it can be O(100n), O(10n) etc, we simplify it to O(n).

"""



# Big O: O(n^2)
