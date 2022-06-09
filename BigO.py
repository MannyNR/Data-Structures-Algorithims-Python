# Intro to Big O:

"""
Big O is a way of comparing 2 sets of code mathematically and seeing how efficient they run.

This is compared via time complexity and space complexity.
"""


# Time Complexity:

"""
Time complexity can be comparing the time it takes for code to execute and complete a.k.a "runtime". However, time complexity is not measuring time itself.
Though it's called time complexity, it is not measured in time. Because if you took the same code and ran it on a computer that runs twice as fast, it would complete twice as fast. It doesn't make the code any better just means the computer is better. So it is measured in the number of operations that it takes to complete something.
"""


# Space Complexity:

"""
There is also space complexity which measures the amount of memory (or "space") code is using. So even though for example code 1 is faster, if the company needs it to work with less capable devices or speed is not the priority, it will be better to consider code that prioritizes space complexity.
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


# O(n) a.k.a Proportional:

"""
In this example we take n and pass it the number 10 and ran this operation n times(10). What ever n is, is the number of operations.

O(n) on a graph will always be a straight line and thus called "Proportional". So if I hear proportional they are talking about O(n)
"""

# def print_items(n):
#   for i in range(n):
#     print(i)

# print_items(10)




# Drop Constants:

"""
So for i this ran n times and this was also the case for j. Which would make this n+n=2n or O(2n) but we can simplify this by dropping the 2 and write it as O(n). 

So no matter what the constant is, it can be O(100n), O(10n) etc, we simplify it to O(n).

"""

# def print_items(n):
#   for i in range(n):
#     print(i)

#   for j in range(n):
#     print(j)

# print_items(10)




# O(n^2) a.k.a "O of n squared" :

"""
O(n^2) or "O of n squared" (n* n = n^2) is typically seen in nested for loops like the example below. However given we simplify if there was another or even multiple other for loops nested in there instead of being O(n^3 or higher) we would simplify it to O(n^2).

def print_items(n):
  for i in range(n):
    for j in range(n):
      for k in range(n):
        print(i,j,k)
      
print_items(10)

^^^^
Still O(n^2)

Given the multiple processes time complexity here is less efficient than in O(n)
"""

# def print_items(n):
#   for i in range(n):
#     for j in range(n):
#       print(i,j)
      
# print_items(10)



# Drop Non-Dominants:

"""
Here we have O(n^2) for the nested i,j loop and O(n) for the k for loop which will be O(n^2 + n). But because O(n^2) is more significant in operations it is the dominant term, thus we drop the non-dominant(n) term and simplify this to O(n^2)
"""

# def print_items(n):
#   for i in range(n):
#     for j in range(n):
#       print(i,j)
  
#   for k in range(n):
#     print (k)
      
# print_items(10)




# O(1) a.k.a "Constant Time":

"""
Known as the most efficient and optimal of the Big O since even as it increases, the number of operations is going to remain constant. 

It's just one operation, and even if its the function below, it gets simplified to O(1). 
 
def add_items(n):
  return n + n + n

If looked at on a Big O graph, O(1) will be a flat straight line across the bottom.
"""

# def add_items(n):
#   return n + n



# O(log n):

"""
An example of how O(log n) works would be to take a list that has sorted items like [1, 2, 3, 4, 5, 6, 7, 8]. To have the most efficient way of finding a number on this list that we dont know where it's at. (imagine if this number is in a larger sorted list) 

To keep it simple, let's say we have to find the number 1 in the list: 

Here we can take the list and cut it in half and see if its in the first half or second half.

list = [1, 2, 3, 4, 5, 6, 7, 8]

first-half-of-list = [1, 2, 3, 4]   second-half-of-list = [5, 6, 7, 8]
  
Here we see its not in the second-half-of-list so we can remove that and stick with the first-half-of-list and repear the halving process until we reach the number 1 in the list.
---

second time halving:

list = [1, 2, 3, 4]

first-half-of-list = [1, 2]   second-half-of-list = [3, 4]

---
third time halving:

list = [1, 2]

first-half-of-list = [1]   second-half-of-list = [2]

On the 3rd attempt we got to the number 1 in the list of 8 numbers, and can count the  3 steps to find it via the examples above. So again, we had 8 elements in the list and it took 3 steps to get the number 1. 

And it just so happens to be that 2 to the third power is 8.
  
 3
2 = 8  (inline it would read 2^3 =8)

If we take the above equation and turn it into a logarithim: 

 3
2 = 8 is the same as saying log 8 = 3
                               2
                               
So what we are looking for is 2 to the what power equals 8? 

We know it's 3 but just for clarity it can be written out as 2**3 = 8 or 2*2*2 =8.

Another way to look at this would be, how many times you have to take the number 8 and divide it by 2 to get down to one item and that is 3 times.

The above examples are to make it more digestable but if we have an equation like this large number over a billion:

log 1,073,741,824
   2

Given the above equation, how many times do you have to cut the number in half to get to one item? The answer is 31 times.

So if you think about a list with a billion items in it, if you're going to iterate through that linearly, from beginning to end, you could have over a billion operations.

But if you do this process of cutting it and have repeatedly, you can find any number in that list in 31 steps.

On a Big O graph, O(log n) is very flat since it's very efficient but O(1) is still the flattest and most efficient Big O. 

"""

# O(nlog n):

"""
Used mostly in some Sorting Algorithms like Merge Sort and Quick Sort since this is the most efficient that you can make a sorting algorithms that are not just numbers. If in case you are sorting through strings and or other types of data types, O(nlog n) is probably your most efficient solution.  

Tip: Not usually used other than in Merge Sort and Quick Sort when dealing with strings, mixed data types.
"""



# Big O: Different Terms for Inputs

"""
Some Interviers will do a gotcha question where they would take a normal for loop and add more than one parameter.

"""
# def print_items(n):
#   for i in range(n):  => is O(n)
#     print(i)
  
#   for j in range(n):  => is O(n)
#     print(j)               ------

# So O(n+n) = O(2n) and can be simplified to O(n) by dropping the constant.
"""
But with different terms for inputs, they will take what looks like this and change it to a function with 2 parameters like the following:
"""
def print_items(a, b):
  for i in range(a):
    print(i)
    
  for j in range(b):
    print(j)
# So again you would think just like the previous example O(n+n) = O(2n) and can be simplified to O(n) by dropping the constant. However, since the parameters are different in this case a and b we can't simplify this 