'''
arithmetical operators
+ add
- subtraction
* multiplication
/ division
% modulus
** exponent
// floor division
'''
def arithmetic(a,b):
    print("addition: ",a+b)
    print("subtraction: ",b-a)
    print("multiplication: ",a*b)
    print("division: ",a/b)
    print("modulus: ",a%b)
    print("exponent: ",a**b)
    print("floor: ",a//b)
a,b=map(int,input("Enter a and b: ").split())
arithmetic(a,b)
'''
relational or comparision operators
<   less than
>   greater than
<=  less than or equal to
>=  greater than or equal to
==  equal to
!=  not equal to
'''
'''
logical operators
and  conjunction
or   disjunction
not  negation
'''
'''
identity operators
is True if both are equal
is not True if both are not equal
'''
'''
assignment operators
= assign
+= add and assign
-= subtrac and assign
*= multiply and assign
/= divide and assign 
%= mod and assign
**= exponent and assign
//= floor and assign
'''
'''
membership operators
in True if found in sequence
not in True if not found in sequence
'''
'''
bitwise operator
& bitwise and
| bitwise or
^ xor
<< left shift
>> right shift
'''