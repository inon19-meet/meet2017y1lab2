Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=0
>>> b=10
>>> a=b
>>> b=a
>>> a=b,b
>>> a=b
>>> b=10
>>> a=b
>>> a
10
>>> b=a
>>> b
10
>>> a=b,b
>>> a
(10, 10)
>>> b
10
>>> a=b
>>> a
10
>>> b
10
>>> a=5
>>> b=a
>>> b
5
>>> a
5
>>> a=10
>>> a
10
>>> b
5
>>> b=c
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b=c
NameError: name 'c' is not defined
>>> a=b
>>> b
5
>>> c
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> a
5
>>> a=10
\
>>> a
10
>>> a=b
>>> a
5
>>> b
5
>>> c=5
>>> a
5
>>> b
5
>>> c
5
>>> a=10
>>> a
10
>>> a=b
>>> a
5
>>> a=10
>>> b=a
>>> a
10
>>> b
10
>>> c
5
>>> b=c
>>> c
5
>>> b
5
>>> a
10
>>> four="4"
>>> print(four*3)
444
>>> my_name = "student"
>>> print("Hi,"+MyName")
      
SyntaxError: EOL while scanning string literal
>>> print("Hi,"+MyName)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print("Hi,"+MyName)
NameError: name 'MyName' is not defined
>>> MyName="inon"
>>> 
>>> 
KeyboardInterrupt
>>> print("Hi"+MyName)
Hiinon
>>> my name is'+'my_name
SyntaxError: invalid syntax
>>> MyName'+'my_name
SyntaxError: invalid syntax
>>> print("MyName"+my_name)
MyNamestudent
>>> my_age = 15
>>> print("i am"+my_age+"years_old")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print("i am"+my_age+"years_old")
TypeError: Can't convert 'int' object to str implicitly
>>> print("i am"+"my age"+"years_old")
i ammy ageyears_old
>>> "my age"=15
SyntaxError: can't assign to literal
>>> "my_age"+15
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    "my_age"+15
TypeError: Can't convert 'int' object to str implicitly
>>> "my_age"=15
SyntaxError: can't assign to literal
>>> "my_age"="15"
SyntaxError: can't assign to literal
>>> print('iam'+'my_age'+'years_old')
iammy_ageyears_old
>>> print('iam'+'15'+'years_old')
iam15years_old
>>> my_age
15
>>> print('Iam'+my_age+'years_old')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print('Iam'+my_age+'years_old')
TypeError: Can't convert 'int' object to str implicitly
>>> "my_age"
'my_age'
>>> my_age
15
>>> '15'
'15'
>>> score=1
>>> total=score + (count * 2)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    total=score + (count * 2)
NameError: name 'count' is not defined
>>> print(total)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
>>> count=score
>>> score=total
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    score=total
NameError: name 'total' is not defined
>>> total=22
>>> score=total
>>> total=score+(count*2)
>>> print(total)
24
>>> score
22
>>> score=1
>>> count=2
>>> total=score+(cout+2)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    total=score+(cout+2)
NameError: name 'cout' is not defined
>>> total=score+(count*2)
>>> print(total)
5
>>> 
