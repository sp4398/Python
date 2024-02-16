myDict={
    "fast": "In a quick manner",
    "saurav":"A coder",
    "marks": [1,2,3],
    "anotherdict" : {'Saurav':'Player'},
    1:3
}
# print(myDict.keys()) #print the keys of the dictionary
# print(myDict.values()) #print the value of the dictionary
# print(myDict.items()) #print the  all content of keys and value of the dictionary
print(myDict)
updateDict={
    "hari":"friend",
    "sweta": "friend"
}
myDict.update(updateDict)  #update dictionary 
print(myDict)

print(myDict.get("saurav"))   

print(myDict.get("saurav2"))   #returns none as saurav2 is not present in dictionary
# print(myDict["saurav2"])   #it shows error as saurav2 is not available in dictionary
