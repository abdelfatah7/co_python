#append()

my_friends=["ali","ahmed","nour"]
print(my_friends)
my_friends.append("sama")
print(my_friends)   

myold_friends=["lilo","jiji"]
my_friends.append(myold_friends)
print(my_friends)   
print(my_friends[4][1]) #هنا بقوله اوصل ل الاندكس 4 ومنه اوصل للندكس 1


###############

#extend() #add list to other as one list 

a=[1,2,3,4]
b=["a","c","g","r"]
a.extend(b)
print(a)

###################

# sort()  بيرتب ارقام بس او حروف بس لكن مينفعش الاتنين مع بعض

a=[-5,10,50,100,0,3,2,7,5,40]
a.sort() #
a.sort(reverse=True) #رتب من الاكبر الي الاصغر 
print(a)

###################

# reverse() دا كل ل بيعمله انه بيعكس اي داتا  ممكن تكون ارقام ممكن حروف او الاتنين مع بعض

s=['A','a',9,2,'ahmed',3,6,5,8,'h']
s.reverse()
print(s)

 