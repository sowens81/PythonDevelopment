# Python Learning Reference
"""This document is a guides on all of the Pyhton syntax and language
Please use at your own risk"""

#Get install version of Python
python --version
python3 --version

# Run a Python file from the command line
python {filename}.py
python {filename}.py

#Access the Pyhton command Line
pyhton

#Exit the Pyhton command line
exit()

#Variables
    x = 5 # X is an int
    Y = "John" # y is a string
    _x = 1 # A variable must start with a letter or an underscore
    x_1 = "Steve" # A variable can only container alphanumeric characters and underscores
    X_2 = 2 # Variable names are case sensitive

# Numbers
    """Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length. """
    x = 1
    x = -1

    """Float, or "floating point number" is a number, positive or negative, containing one or more decimals."""
    x = 1.0
    x = 1.12
    x = -35.243

    """Complex numbers are written with a "j" as the imaginary part"""
    x = 3+5j
    x = 5j
    x = -5j


    """ Type function, identifies what type of number it is int, float, complex."""
    type()

    x = 1
    y = 1.01
    z = 5j
    print(type(x)) # int
    print(type(y)) # float
    print(type(z)) # complex

#Casting
    """There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types."""
    """Intergers"""
    x = int(1)   # x will be 1
    y = int(2.8) # y will be 2
    z = int("3") # z will be 3

    """Floats"""
    x = float(1)     # x will be 1.0
    y = float(2.8)   # y will be 2.8
    z = float("3")   # z will be 3.0
    w = float("4.2") # w will be 4.2

    """String"""
    x = str("s1") # x will be 's1'
    y = str(2)    # y will be '2'
    z = str(3.0)  # z will be '3.0'

#Strings Literals
    """String literals in python are surrounded by either single quotation marks, or double quotation marks."""
    a = 'hello, world!'
    b = "hello, world!"

    """Get the character at position 1 (remember that the first character has the position 0)"""
    a = "Hello, World!"
    print(a[1])

    """Substring. Get the characters from position 2 to position 5 (not included)"""
    b = "Hello, World!"
    print(b[2:5])

    """The strip() method removes any whitespace from the beginning or the end"""
    a = " Hello, World! "
    print(a.strip()) # returns "Hello, World!"

    """The len() method returns the length of a string"""
    a = "Hello, World!"
    print(len(a))

    """The lower() method returns the string in lower case"""
    a = "Hello, World!"
    print(a.lower())

    """The upper() method returns the string in upper case"""
    a = "hello world"
    print(a.upper())

    """The replace() method replaces a string with another string"""
    a = "Hello, World!"
    print(a.replace("H", "J"))

    """The split() method splits the string into substrings if it finds instances of the separator"""
    a = "Hello, World!"
    print(a.split(",")) # returns ['Hello', ' World!']

#Operators
    """Arithmetic operators are used with numeric values to perform common mathematical operations"""
    x + y #Addition +
    x - y #Subtraction -
    x * y #Multiplication *
    x / y #Division /
    x % y #Modulus %
    x ** y #Exponentiation **
    x // y #Floor Division //

    """Comparison operators are used to compare two values"""
    x == y # ==	Equal		
    x != y # !=	Not equal		
    x > y # >	Greater than	
    x < y # <	Less than		
    >= y # >=	Greater than or equal to	
    x <= y # <=	Less than or equal to

    """Logical operators are used to combine conditional statements"""
    x < 5 and  x < 10 #and 	Returns True if both statements are true	
    x < 5 or x < 4 #or	Returns True if one of the statements is true	
    not(x < 5 and x < 10) #not	Reverse the result, returns False if the result is true

    """Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object"""
    x is y #is 	Returns true if both variables are the same object
    x is not y #is not	Returns true if both variables are not the same object

    """Membership operators are used to test if a sequence is presented in an object"""
    x in y #in 	Returns True if a sequence with the specified value is present in the object
    x not in y #not in	Returns True if a sequence with the specified value is not present in the object	

    """Bitwise operators are used to compare (binary) numbers"""
    & 	#AND	Sets each bit to 1 if both bits are 1
    |	#OR	Sets each bit to 1 if one of two bits is 1
    ^	#XOR	Sets each bit to 1 if only one of two bits is 1
    ~ 	#NOT	Inverts all the bits
    <<	#Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
    >>	#Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

    """Assignment operators are used to assign values to variables"""
    x = 5 #Same as	x = 5	
    x += 3	#Same as	x = x + 3	
    x -= 3	#Same as	x = x - 3	
    x *= 3	#Same as	x = x * 3	
    x /= 3	#Same as	x = x / 3	
    x %= 3	#Same as	x = x % 3	
    /x //= 3 #Same as	x = x // 3	
    x **= 3	#Same as	x = x ** 3	
    x &= 3	#Same as	x = x & 3	
    x |= 3	#Same as	x = x | 3	
    x ^= 3	#Same as	x = x ^ 3	
    x >>= 3	#Same as	x = x >> 3	
    x <<= 3	#Same as	x = x << 3

#Collections (Arrays)
    """List - A list is a collection which is ordered and changeable. In Python lists are written with square brackets."""
    thislist = ["apple", "banana", "cherry"]
    print(thislist)

    """Access items - You access the list items by referring to the index number"""
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1]) # Prints the second item in the list

    """Change Item Value - To change the value of a specific item, refer to the index number"""
    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "orange"
    print(thislist)

    """Loop through a list - You can loop through the list items by using a for loop"""
    thislist = ["a", "b", "c"]
    for x in thislist:
        print(x)
    
    """Check if item exists - To determine if a specified item is present in a list use the in keyword"""
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")

    """List Length - To determine how many items a list has, use the len() method"""
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))

    """Add Items"""
        """To add an item to the end of the list, use the append() method"""
        thislist = ["apple", "banana", "cherry"]
        thislist.append("orange")
        print(thislist)

        """To add an item at the specified index, use the insert() method"""
        thislist = ["apple", "banana", "cherry"]
        thislist.insert(1, "orange")
        print(thislist)
    
    """Remove Item - There are several methods to remove items from a list"""
        """The remove() method removes the specified item"""
        thislist = ["apple", "banana", "cherry"]
        thislist.remove("banana")
        print(thislist)

        """The pop() method removes the specified index, (or the last item if index is not specified)"""
        thislist = ["apple", "banana", "cherry", "orange", "lemon", "lime"]
        thislist.pop()
        thislist.pop(1)
        print(thislist)

        """The del keyword removes the specified index"""
        thislist = ["apple", "banana", "cherry"]
        del thislist[0]
        print(thislist)

        """The del keyword can also delete the list completely"""
        thislist = ["apple", "banana", "cherry"]
        del thislist

        """The clear() method empties the list"""
        thislist = ["apple", "banana", "cherry"]
        thislist.clear()
        print(thislist)

    #list() constructor - It is also possible to use the list() constructor to make a list
    thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
    print(thislist)

    #List methods
    append() #Adds an element at the end of the list
    clear()	#Removes all the elements from the list
    copy()	#Returns a copy of the list
    count()	#Returns the number of elements with the specified value
    extend() #Add the elements of a list (or any iterable), to the end of the current list
    index()	#Returns the index of the first element with the specified value
    insert() #Adds an element at the specified position
    pop() #Removes the element at the specified position
    remove() #Removes the item with the specified value
    reverse() #Reverses the order of the list
    sort() #Sorts the list

#Tuple
    """Create a tuple"""
    thistuple =("apple", "banana", "pear")

    """Access a tuple item - Return the item in position 1"""
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])

    """Change tuple value - You cannot change values in a tuple"""
    thistuple = ("apple", "banana", "cherry")
    thistuple[1] = "blackcurrant"
    # The values will remain the same:
    print(thistuple)

    """Loop through a tuple - You can loop through the tuple items by using a for loop"""
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)
    
    """Check if Item Exists - To determine if a specified item is present in a tuple use the in keyword"""
    thistuple = ("apple", "banana", "cherry")
        if "apple" in thistuple:
        print("Yes, 'apple' is in the fruits tuple")
    
    """Tuple Length - To determine how many items a tuple has, use the len() method"""
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))

    """Add Items - Once a tuple is created, you cannot add items to it. Tuples are unchangeable."""
    thistuple = ("apple", "banana", "cherry")
    thistuple[3] = "orange" # This will raise an error
    print(thistuple)

    """Remove Items - Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely."""
    thistuple = ("apple", "banana", "cherry")
    del thistuple
    print(thistuple) #this will raise an error because the tuple no longer exists

    """The tuple() Constructor - It is also possible to use the tuple() constructor to make a tuple."""
    thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
    print(thistuple)

    """Tuple Methods - Python has two built-in methods that you can use on tuples."""
    count()	#Returns the number of times a specified value occurs in a tuple
    index()	#Searches the tuple for a specified value and returns the position of where it was found

#Sets
    """Set - A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets."""
    thisset = {"apple", "banana", "cherry"}
    print(thisset)

    """Access Items - You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
    But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword."""
    thisset = {"apple", "banana", "cherry"}
    for x in thisset:
        print(x)
    
    """Access Items - Check if "banana" is present in the set."""
    thisset = {"apple", "banana", "cherry"}
    print("banana" in thisset)

    





















