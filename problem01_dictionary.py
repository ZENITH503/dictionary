mydictionary = {
   "pankha" : "fan",
   "balti" : "bukcet",
   "basta"  : "bag"
}
print("options of words are : " , mydictionary.keys())
a=input("enter the word ur looking for : ")
#print("the meaning of ur word is : " , mydictionary[a])
#in order to avoid error in the program we make use of get function
print("the meaning of ur word is : " , mydictionary.get(a))