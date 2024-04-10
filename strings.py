name = 'Dhiraj'
print(name)  # Output: Dhiraj

# This line throws an error because it's trying to assign a string in an invalid way.
# name = 'Dhiraj              This throws error cause it doesnot accept such way
# is a good boy'
# print(name)

# However, you can use triple quotes to define multiline strings.
name = '''Harry
    is a good boy'''
print(name)
# Output:
# Harry
#     is a good boy


#------->string functions<-------------#
naam = "   Dhiraj    "
name2="Ram, Hari, Shyam"
print(naam.strip())             #strip function removes the extra spaces
print(len(naam))                #length of string
print(naam.lower())
print(naam.upper())
print(naam.replace("r","t"))
print(naam.replace("ar","t"))
print(name2.replace(",",''))

#------->concating 2 strings<---------#
st1="Dhiraj"
st2="Chaurasiya"
print(st1+' '+st2)

#-------------------------------------------------------#
#to add using template
temp = "This is {} and he is a good boy".format(st1)
print(temp)

#several ways
temp=f"this is {st2} and he is a good boy"
print(temp)

temp="This is {1} and he's surname isnot {0}".format(st1,st2)
print(temp)
