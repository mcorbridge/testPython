print("foo")

a=1+2+3+\
4+5+6+\
7+8+9+10

print(a)

colors=["red","blue","green","yellow","orange","black","white"]

print(colors)
print(colors[0])

a=1;b=2;c=3

lenColors = len(colors)

for i in range(lenColors):
	color = colors[i]
	print(color)
	
print("*****************************")
	
	
for i in range(100):
	print("---------------" + str(i) + "--------------------")
	for n in colors:
		print(n)
		
print("")
	
# Variable assignment	
print("Variable assignment")		
a = 5
b = 3.2
c = "Hello"
print("a=" + str(a) + " b=" + str(b) + " c=" + c)
print("")

# Multiple assignments
print("Multiple assignments")	
a, b, c = 5, 3.2, "Hello"
print("a=" + str(a) + " b=" + str(b) + " c=" + c)
print("")

# Python Numbers
print("Python Numbers")
a = 5
print(a, "is of type", type(a))
print("")
a = 2.0
print(a, "is of type", type(a))
print("")
a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
print("")


# Python List (aka Array)
print("Python List")	
a = [5,10,15,20,25,30,35,40]
# a[2] = 15
print("a[2] = ", a[2])
# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])
# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])
print("")


# Python Tuple
print("Python Tuple")	

import RPi.GPIO as GPIO

t = (5,"program", 1+3j)
# t[1] = "program"
print("t[1] = ", t[1])
# t[0:3] = (5, "program", (1+3j))
print("t[0:3] = ", t[0:3])
# Generates error
# Tuples are immutable
# t[0] = 10
print("")

# Python Strings
print("Python Strings")	
s = "Hello world!"
# s[4] = "o"
print("s[4] = ", s[4])
# s[6:11] = "world"
print("s[6:11] = ", s[6:11])
# Generates error
# Strings are immutable in Python
# s[5] ="d"
print("")

# Python Set
print("Python Set")	
a = {5,2,3,1,4}
# printing set variable
print("a = ", a)
# data type of variable a
print(type(a))
a = {1,2,2,3,3,3}
print("a = ", a)
print("")

# Python Dictionary
print("Python Dictionary")	
d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);
print("")