myDict = {'a': 'apple', 'b': 'Bobby' , 'o': 'Orange', 'm': 'Mango' , 'z': 'zebra'}
print("Dictionary : ", myDict)

key = input("Please enter the Key you want to search for: ")


if key in myDict.keys():
    print("\nKey Exists in this Dictionary")
    print("Key = ", key, " and Value = ", myDict[key])
else:
    print("\nKey Does not Exists in this Dictionary")
