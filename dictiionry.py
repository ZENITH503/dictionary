# printing the normal dictionary without nesting
mydictionary1 = { "shubham":"is a god boy" ,
                "harry" : "is a bad boy",
                "cde" : "i am the best"
}
print(mydictionary1["shubham"])
print(mydictionary1["harry"])
print(mydictionary1["cde"])
# printing the dictionary with nesting
# in nested dictionary u have to put the name of the nested dictionary with the keyword
# dictionary is mutable  that is we can change its value

mydictionary = { "shubham":"is a god boy" ,
                "harry" : "is a bad boy",
                "cde" : "i am the best",
                "marks" : [1,2,3,4,5,6,7,8,9],
                "mydictionarynested" : {  "haryy2" : "i am the worst"}
}
print(mydictionary["shubham"])
print(mydictionary["harry"])
print(mydictionary["cde"])
print(mydictionary["marks"])
print(mydictionary["mydictionarynested"]["haryy2"])
mydictionary["shubham"]=[1,2,3,4]
print(mydictionary["shubham"])
#this fucntion prints the keywords of the dictionary
print(mydictionary.keys()) 
#the dictionary is not list but dict data type which can be later converted to list
print(type(mydictionary))
# mydictionary = list(mydictionary)
# print(type(mydictionary))
#to print the meaning or the values of the keywords we take , this only prints the values of a dictionary not the values or do nnot print list data type
print(mydictionary.values())
 #to print every value in the dictionay including values and keywords
print(mydictionary.items()) 
#in order to add items in the dictionary we take and also updates the dictionary if we want to by changing the value of the same key word
print(mydictionary)
update_dictionary = {
    "idli" : "bekar",
    "sambhar" : "achaa",
    "dosa" : " bekar"
}
mydictionary.update(update_dictionary)
print(mydictionary)
#new method of priting the value of keys
print(mydictionary.get("shubham"))
print(mydictionary["shubham"])
# difference between .get function is that
print(mydictionary.get("shubham1"))#do  not throw error , but throws none if the keyowrd enterd is not present in the dictionary
#print(mydictionary["shubham1"])#throws an error if the keyowrd enterd is not present in the dictionary
#in order to create an empty dictionary we take
a={}
print(type(a))