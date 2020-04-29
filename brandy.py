#tuple and sets....-tuple is an ordered collection or groupings of items//#
 #they are immutable meaning the values cannot be changed//
alphabet = ("a" ,"b","c" , "d")
print(alphabet[0])

#tuples can be used as keys in dictionaries#
locations = {
    (67.980,56.78):"mariwenyi",
    (23,675,45.7890):"st.joseph",
    (12.345,23.4567):"baobab"
}
print(locations[(23,675,45.7890)])


months = ("january","february","march","april","may","june","july","august","september","october","november","december")
#for month in months:
    #print(month)


#this will print the  months backward//#
i = len(months) -1
while i>=0:
    print(months[i])
    i -=1

#tuple methods....count --returns number of times a value appears in a tuple//#
x = (1,2,3,3)
print(x.count(1))
print(x.count(3))

#index----returns the index of value in tuple
x = (1,2,3,3)
print(x.index(1))


#sets.....they are mathematical sets,they do not have dublicate values and elements in sets arent ordered//
#items in set  cannot be accessed with their index#
s = {"23,6,b,5,90.67,f"}
for num in s:
    print(s)
#print(s)
#adding elements in a set is just same as removing  we use .add and .remove/discard,.copy and .clear
s = {1,2,3,5}
s.add(4)
print(s)

#set math...if you want the total list without dublicate we use union
#set intersection...tell students both in the set
math_students = {"kenny","rodgers","jemo","denviour","betty","meghan","edwine"}
phyc_students = {"kenny","calleb","brandy","ryan","denviour","betty","jones","edwine"}
print(math_students|phyc_students)#print the set union
print(math_students & phyc_students)#prints intersection

#set comprehension
string = "Hello"
print({char for char in string if char in "aeiou"})
print len ({char for char in string if char in "aeiou"})

