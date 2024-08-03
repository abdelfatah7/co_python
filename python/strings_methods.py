x = "i love python\n"
print(len(x)) 

# Strip() , rstrip()  , lstrip()   --->  delete spaces

a = "      i love nmu\n     "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "******i love nmu*********"
print(a.strip("*"))
print(a.rstrip("*"))
print(a.lstrip("*"))

# title()

b = "\ni love 3d printing\n"
print(b.title())

# capitalize()
b = "i love 3d printing "
print(b.capitalize())

# UPPER 
s = "\nabdelfattah"
print(s.upper())

# LOWER
s = "\nABDELFATTAH"
print(s.lower())