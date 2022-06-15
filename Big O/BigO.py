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

# Tip Big O a.k.a:
# Big O is technically worst case however, some people refer to Omega as best case big O, and Theta as average case big O.


# Omega - Theta - Big O:
"""
  There's Best case (Omega "Ω"), Average case (Theta "Θ") , and Worst case (Omicron/ Big O "O"). An example would be a sorted number list:

  "Ω"      "Θ"      "O"
  [1, 2, 3, 4, 5, 6, 7]

  If they ask to find 1 in the list that would be Best case Omega "Ω" since it's the first element in the list and we would find it right away.

  If finding 4 in the list, that would be Average case (Theta "Θ") since it's in the middle(average).

  And Worst Case (Omicron "Big O") would be finding 7 since it is at the end of the list and we'd have to iterate through the entire list.
"""


# O(n) a.k.a "Proportional":

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


# O(n log n):

"""
  Used mostly in some Sorting Algorithms like Merge Sort and Quick Sort since this is the most efficient that you can make a sorting algorithms that are not just numbers. If in case you are sorting through strings and or other types of data types, O(nlog n) is probably your most efficient solution.  
"""

# Tip on O(n log n):
# Not usually used other than in Merge Sort and Quick Sort when dealing with strings, mixed data types.


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
# def print_items(a, b):
#   for i in range(a):
#     print(i)

#   for j in range(b):
#     print(j)

"""
  So again you would think just like the previous example, O(n+n) = O(2n) and can be simplified to O(n) by dropping the constant. 

  However, since the parameters are different in this case a and b, we can't simplify this like before. 
"""
# def print_items(a, b):
#   for i in range(a):  => O(a)
#     print(i)

#   for j in range(b):  => O(b)
#     print(j)             ----
#                         O(a + b)

"""
  Again, in this case we can't simplify O(a + b).   
            
  Another Example where we cant simplify would be the following nested for loop which again has different parameters:
"""
# def print_items(a, b):
#   for i in range(a):  => O(a)
#     for j in range(b):  => O(b)
#       print(i,j)           -------
#                           O(a * b)


#  Big O Lists:


# O(1)
"""
  Following the same principles already learned, we can apply these to Lists which are very common data structures:

  Starting with my_list below lets use .append() and .pop() to add and remove an element to the end of the list. This will happen without reindexing.

    my_list = [11, 3, 23, 7]
  Index in list  0  1   2  3

  my.list.append(17) will add to the end of my list and thus make it:

    my_list = [11, 3, 23, 7, 17]
  Index in list  0  1   2  3   4

  my.list.pop() will remove the last element in the list and thus do it without any reindexing.

    my_list = [11, 3, 23, 7]
  Index in list  0  1   2  3 

  Both examples above are O(1) since they are constant time/ have only one operation to complete.
"""


# O(n)
"""
  Now if we take the same list and use my_list.pop(0) our list will have to reindex since the first element (11) is removed and the elements have to shift down to a new index.

    my_list = [3, 23, 7]
  Index in list 0  1   2 

  The same is true if now we try to add 11 back to the index of 0 in my_list:

  (I is Index, E is Element)

    my_list.insert(0,11)
                    I  E
    
    my_list = [11, 3, 23, 7]
  Index in list  0  1   2  3 

  So if we are removing or adding an element to a list where the front or "0 index" is changed like the examples above this is O(n).
"""
# Tip Big O for list.pop() or list.insert() to first and last index in a list:
# If adding or removing from the end O(1), and if doing the same but in the beginning where element at 0 index is changed and a reindex happen, that is O(n)


# Adding or removing from a list(not at index 0 or at the end):
"""
  If adding or removing an element from the middle (anywhere not at index 0 or the end of the list) this causes a reindexing and can be noted as O(n). 

  As mentioned Big O is always looking at worst case so even though adding to the middle of the list may be O(1/2n), we can drop the constant (1/2) and simplify it to O(n)
"""


# Looking for a specific item in a list:
"""
  If we have a piece of code written to look for a specific item by value in a list that will be O(n) since we have to iterate through the list using a for loop to find the value.

  Now if we are looking for the same item by index, and you want the value at that specific spot, you can go directly to that place in memory based on it's index, and that is O(1).
"""


# Wrapping up Big O

"""

  The larger n becomes the more inefficient O(n) and O(n^2) especially are. To put this into perspective:
  
  Lets say n = 100

  That will make:
  O(1) = 1
  O(log n) = appx 7(2^6.65 = 100.42) (2^6 is 64 and 2^7 is 128)
  O(n) = 100
  O(n^2) = 10,000
  
---

  Now let's say n = 1,000

  That will make:
  O(1) = 1
  O(log n) = appx 10 (Since 2^10 is 1,024 and 1,000 is pretty close to that) -- (Notice this only went from almost 7 to almost 10 even though n went from equaling 100 to equaling 1,000)
  O(n) = 1,000
  O(n^2) = 1,000,000 -- (Again as n grows, O(n^2) becomes very inefficient). Finding ways to get our code from O(n^2) to O(n) is a huge increase in efficiency.
"""

# Important terminology tips:
"""
  O(n^2) is a Loop within a Loop
  
  O(n) is Proportional (It's always a straight line (diagonal on graphs))
  
  O(log n) is Divide and Conquer
  
  O(1) is Constant Time
"""


# Edge Cases:

"""
Typically O(n^2) is noted as being in the horrible category given how as n grows it grows exponentially as well. This should be our worst of the worst case typically.

However there are 2 other Big O cases worse than O(n^2)

The worst is:
O(n!) a.k.a "O - N factorial" which has to be intentionally bad written code to achieve. On a graph this is usually close to the vertical axis leaning close to the edge.

The other is O(2^n) which is not too far off to the right of O(n!) and left of O(n^2)
"""

# Tips for this course and in general:

"""
  O(n^2) in the horrible category should be the worst case we see. 

  O(n log n) in the bad category we'll see in a couple of sorting Algorithms(Merge Sort and Quick Sort when dealing with strings, mixed data types.)
  
# But in general you want to stay in the following range:
  
  O(n) in the fair category
  
  O(log n), O(1) are good to excellent cases in the Big-O complexity chart and yield the most efficient results.
  
"""


# Common Data Structure Operations (check README for Cheatsheet chart):

"""
  Space complexity is typically in the Big-O or Worst category in charts given its usually always O(n) except for Skip List which is O(n log n).
  
  Thus focus should be more on Time complexity which can vary alot base on the data structure. See cheat sheet's (in README) Common Data Structure Operations for more.
"""

# Array Sorting Algorithms (check README for Cheatsheet chart):

"""
  Here Space complexity can vary mostly between O(1) and O(n) with Quicksort being O(log (n))

  Time complexity does show alot of Omega/best case with Omega(n*log(n)) and Theta(n*log(n)) being best and average cases accross Quicksort, Mergesort and Heapsort.

  Bubblesort and Insertionsort's bestcase is Omega(n) for lists where the data is sorted or almost sorted completely. While Space Complexity is O(1)
"""
