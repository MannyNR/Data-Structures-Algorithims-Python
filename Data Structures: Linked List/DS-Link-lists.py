# Data Structures - Link Lists

# Overview
"""
  A link list is like a normal list in Python however it DOES NOT have any built in indexes.
  
  Another important difference is that in a traditional list, each element is stored in a contiguos place in memory (The elements are all stored next to each other in memory). This is not the case in a link list, in a linked list the nodes are going to be stored all over the place. 
  
  example:
  
  Traditional list = [11, 3, 23, 7]
             index   [0],[1],[2],[3]  
                
In memory they are all stored next to each other so if we were to run an id check on each element in the index, it will print an id location that increments by 1 as you continue in the list.

             HEAD       TAIL
               ⬇         ⬇
  LinkList =  11➡️ 3➡️ 23➡️ 7➡️ (Null)
  
  (➡️ = Next/Pointer)
  
  Here we can see a link list has a head which points to the next element in memory that follows it. Each element pointing to the next leaving the tail last which points to Null(None/Nothing).
  
  In memory it wont be a straight line similar to a regular list. The ids will be all over the place but what keeps the list in order is the head pointing to the next nodes in the linked list. 
"""



# Nodes in Linked List:
"""
  A good way to think of a node in a linked list is to think of it like a dictionary. A node is the value and also the pointer '➡️'. So '11➡️' is a node.
  
  Given such when we see this below:
              HEAD         TAIL       
               ⬇            ⬇           
  LinkList =  11➡️ 3➡️ 23➡️ 7➡️ 4➡️ (Null)
  

  We can think of it this way:
            HEAD                
              ⬇  
head =   {
           "value": 11,
           "next": {
                     "value": 3,
                     "next": {
                               "value": 23,
                               "next":  {
                                          "value": 7,
                                          "next": {
                                                    "value": 4,
                                                    "next": None
                                                  }      ⬆️
                                         }             TAIL
                               } 
                     }
           }
  
So even though the syntax for a linked list is not written like the nested dictionaries above, we can think of it that way. A set of nested dictionaries.

Proper syntax for a linked list would be something like this in code:
print(my_linked_list.head.next.next.value) # Would print 23
"""




# Linked List: Big O (Methods and their Big O for Linked List (See attached pdf LL-vs-List-BigO for table))



    ## Append (add to the end): O(1)
"""
Using our example, if we were to append a new node (4) to the end of the link list:

  (➡️ = Next)

             HEAD       TAIL     NEW_NODE(NEW TAIL)
              ⬇           ⬇          ⬇
  LinkList =  11➡️ 3➡️ 23➡️ 7➡️ (Null)  4➡️ (Null)
  
  In order to do this first, the last node (7) has to point to the new node (4), now Tail is going to point to it and finally we add it into the list.
  
             HEAD           TAIL       
               ⬇             ⬇           
  LinkList =  11➡️ 3➡️ 23➡️ 7➡️ 4➡️ (Null)
  
As per usual, it doesn't matter how many of 'n'(nodes in this case) we have to add. The number of operations to add it to the end is exactly the same, thus this is O(1).
"""


    ## Removing(Pop) from the end: O(n)
"""
When removing from the end it's a little more complicated than just adding to the end.
  
    (➡️ = Next)
  
              HEAD         TAIL       
               ⬇            ⬇           
  LinkList =  11➡️ 3➡️ 23➡️ 7➡️ 4➡️ (Null)
  
  Using the new example with 4 as our tail node, we can't just simply remove 4 and move tail to 7 just like that. First our tail has to point to something that is pointing to our 7 node (the Next➡️ pointer after 23). And in order to get to that node, we have to start at the head and iterate through the list until we get to that pointer. Then we can set TAIL equal to the Next pointer that is pointing to the 7 node. But because we had to iterate through the entire list, this is O(n)
  
  (➡️ = Next)
  
  Example:
  
             HEAD          TAIL       GARBAGE DISPOSAL
              ⬇             ⬇            ⬇
  LinkList =  11➡️ 3➡️   23➡️  7➡️ (Null)    4➡️ (Null)
Iterat. start ⤴ ➡️ ⤴ ➡️ ⤴ ➡️ ⤴ ↖️ Next pointer pointing to 7
"""


# Adding and Removing from the beginning of a link list:


    ## Adding to the front of a linked list (Prepend): O(1)
"""
Here we are going to add a node (4) to the front on the link list. We need to have that 4 point to the 11 node. The HEAD points to the 11, so we'll also have 4's Next pointer equal to HEAD and that points it to that node. Once that happens 4 is now at the HEAD of the link list.

(➡️ = Next)

Add a 4 node to the front of this list, making it the HEAD: 
       
                      CURR._HEAD   TAIL
                          ⬇         ⬇
                    4 ➡️  11➡️ 3➡️ 23➡️ 7➡️ (Null)
Have 4 ➡️ point to 11 ⤴       

        NEW_HEAD         TAIL
            ⬇             ⬇
LinkList =  4➡️ 11➡️ 3➡️ 23➡️ 7➡️ (Null)
  
The number of operations to add it to the front is exactly the same, thus this is O(1).

"""


    ## Removing from the front of a linked list (Pop First): O(1)
"""
Here we are going to remove node (4) from the front on the link list. We need to start by pointing HEAD to the 11 node. We can do that by saying HEAD = HEAD.Next

(➡️ = Next)
       
              CURR._HEAD      TAIL
                  ⬇             ⬇
                  4➡️ 11➡️ 3➡️ 23➡️ 7➡️ (Null)
Have HEAD point to 11 ⤴       
  
GARB.DISP.   NEW_HEAD    TAIL
⬇               ⬇         ⬇
4 ➡️            11➡️ 3➡️ 23➡️ 7➡️ (Null)
  
The number of operations to remove it from the front is exactly the same no matter how many new nodes we add to the front, thus this is O(1).

"""


    ## Inserting a node to the middle of a link list (Insert): O(n)
"""

Add a 4 node to the middle of this list, right after node 23
  
  We have to start at the HEAD and iterate through the list until we get to the 23 node. Now we want the 4 node to point '➡️' at the 7 node, but that pointer'➡️' after node 23 is pointing to the 7 node. 
  
              HEAD        TAIL
  (➡️ = Next)     ⬇           ⬇
              11➡️ 3➡️ 23⤵  7➡️ (Null)
                        4↗️
                      
              HEAD         TAIL       
               ⬇            ⬇           
  LinkList =  11➡️ 3➡️ 23➡️ 4➡️ 7➡️ (Null)

Again, since we had to iterate through the list, this is O(n). If we have to iterate through the list and the number of nodes we need to add increases we are adding more operations to the code. Just like for loops(iterating) usually O(n).
"""


    ## Removing a node from the middle of a linked list (Remove): O(n)
"""
  So starting with our new LinkList, lets say we want to remove the 4 node from the list: 

  (➡️ = Next)
    
      HEAD         TAIL       
        ⬇            ⬇           
      11➡️ 3➡️ 23➡️ 4➡️ 7➡️ (Null)

  We want to iterate through the list starting at the HEAD until we get to the 4 node like this:
  
      HEAD         TAIL
        ⬇            ⬇
        11➡️ 3➡️ 23⤵  7➡️ (Null)
                  4↗️
  
  Now we want node 23 to point at the 7 node, so we are going to set the '➡️' Next pointer from 23 to equal to the pointer going from the 4 to the 7 node:  
  
      HEAD        TAIL       
        ⬇          ⬇  
        11➡️ 3➡️ 23➡️ 7➡️ (Null)
                        (4 ➡️ Will be taken care of by Garbage Disposal)
                              
Once again we had to iterate through the list, so this is O(n)
"""


## Lookup by Index/Value in a Linked List: O(n)
"""
Starting with the same Link List let us look up the node 23:

    HEAD        TAIL       
      ⬇          ⬇  
      11➡️ 3➡️ 23➡️ 7➡️ (Null)

We have to start at the HEAD and say is this 23? And it's not, so we will continue to iterate through until we find it. Also with a linked list, if we are going to look at this by index and node 23 is at the index of two, you have to start at the head and iterate through the indexes until you get to the index of two.

This is something different than lists because with lists you can do this by index as O(1) but with a linked list, both looking it up by the value or the index is O(n). (see PDF for chart)
"""


# Big O Cliff Notes for Linked List and Python Lists:

"""
 Any time we are working on adding (prepend) or removing (pop first) from the front of a linked list (changing the head) it's O(1) everything else is O(n).
 
 With a traditional Python list, Append(add to end), Pop(remove last) (changing the tail), and Lookup by Index are the only O(1), everything else is O(n).
"""