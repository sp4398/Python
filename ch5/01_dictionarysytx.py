myDict={
    "Fast": "In a quick manner",
    "Saurav":"A coder",
    "Marks": [1,2,3],
    "anotherdict" : {'Saurav':'Player'}
}
print(myDict['Saurav'])
print(myDict['Fast'])
myDict['Marks']=[12,34] #mutable means value over ride
print(myDict['Marks'])
print(myDict['anotherdict']['Saurav'])

a={} #empty dictionary
print(type(a))
