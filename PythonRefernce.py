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

    