#strings are a sequence of characters enclosed in single, double or triple quotes
str1 = "this is a string"
str2 = 'Prajwal'
str3 = """This is a multi line string"""
print(str1)
print(str2)
print(str3)

#string formatting using escape characters
str1 = "This is a string.\n we are creating it in python."
print(str1)

#string concatenation
str4 = "Prajwal"
str5 = "Shivashimpar"
print(str4 + " " + str5)

#string length
#the len() function is used to find the length of a string
print(len(str4)) #length of str4 is 7
print(len(str5)) #length of str5 is 12
print(len(str4 + " " + str5)) #length of str4 + str5 is 20 (7 + 1 + 12)


#string indexing
#strings are indexed from 0 to n-1, where n is the length of the string
str = "Prajwal Shivashimpar"
#print(str[0])
ch = str[0] #first character of the string
print(ch) #output: P

#print(str[7]) #output: S
ch = str[7] #eighth character of the string
print(ch) #output: S

#print(str[-1]) #output: r
ch = str[-1] #last character of the string
print(ch) #output: r


#string slicing
#string slicing is used to extract a part of the string
#the syntax for string slicing is: string[start:end], where start is the index of the first character to be extracted and end is the index of the first character to be excluded
str = "Prajwal Shivashimpar"
#print(str[0:7]) #output: Prajwal
sliced_str = str[0:7] #slicing the string from index 0 to 6
print(sliced_str) #output: Prajwal

#print(str[8:20]) #output: Shivashimpar
sliced_str = str[8:20] #slicing the string from index 8 to 19
print(sliced_str) #output: Shivashimpar

#print(str[:7]) #output: Prajwal
sliced_str = str[:7] #slicing the string from index 0 to 6
print(sliced_str) #output: Prajwal

#print(str[8:]) #output: Shivashimpar
sliced_str = str[8:] #slicing the string from index 8 to the end of the string
print(sliced_str) #output: Shivashimpar

#print(str[:]) #output: Prajwal Shivashimpar
sliced_str = str[:] #slicing the string from index 0 to the end of the string
print(sliced_str) #output: Prajwal Shivashimpar

#negative indexing and slicing
#print(str[-3:-1]) #output: ar
sliced_str = str[-3:-1] #slicing the string from index -3 to -2
print(sliced_str) #output: ar

#print(str[-5:-2]) #output: par
sliced_str = str[-5:-2] #slicing the string from index -5 to -3
print(sliced_str) #output: par


#string functions
#string functions are built-in functions that can be used to perform various operations on strings

str = "prajwal Shivashimpar"

#the upper() function is used to convert a string to uppercase
print(str.upper()) #output: PRAJWAL SHIVASHIMPAR
print(str.capitalize()) #output: Prajwal shivashimpar

#the lower() function is used to convert a string to lowercase
print(str.lower()) #output: prajwal shivashimpar

#the title() function is used to convert the first character of each word to uppercase and the rest to lowercase
print(str.title()) #output: Prajwal Shivashimpar

#the strip() function is used to remove leading and trailing whitespace from a string
str_with_spaces = "   Prajwal Shivashimpar   "

#the original string with spaces
print(str_with_spaces.strip()) #output: Prajwal Shivashimpar

#the split() function is used to split a string into a list of substrings based on a specified delimiter
print(str.split()) #output: ['prajwal', 'Shivashimpar']

#the endwith() function is used to check if a string ends with a specified suffix
print(str.endswith("par")) #output: True

#the startswith() function is used to check if a string starts with a specified prefix
print(str.startswith("prajwal")) #output: True

#the find() function is used to find the index of the first occurrence of a specified substring in a string
print(str.find("Shiva")) #output: 8

#the count() function is used to count the number of occurrences of a specified substring in a string
print(str.count("r")) #output: 2

#the replace() function is used to replace a specified substring with another substring in a string
print(str.replace("a", "A")) #output: prAjwAl ShivAshimpar

