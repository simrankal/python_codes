a="simran"
print(len(a))
print(a.upper())
print(a.lower())
# Strings are immutables means we can change it into lower and upper case
b="simran!!!!!"
print(b.rstrip("!"))
# it will strip the only backward character not trailing one
print(b.replace("simran","kalsi"))  #replace character will replace the existing character with the new one

c="Simran !!!!! kalsi"
print(c.split(" ")) #split convert the existing string into list



blogheading="Introduction to js"
print(blogheading.capitalize()) #capitalize will convert the first character into upper case and the other character into lower case


stri="Welcome to the junngle"
print(stri.center(50)) #center will add the space in the string

str2='Simran'
print(str2.count("a")) #count will count the number of character in the string



str3="simran!!!!!!"
print(str3.endswith("!!!!!!")) #endswith will check the string is ending with the given character or not

print(stri.endswith("to",4,10)) #endswith also use for slicing as well


str4="where is the pen"
print(str4.find("is")) #find will find the first occurence of the given character and return the index number, if it will not find anything then it will return -1. And also it will count from starting and if it has maximum number then it will return only one occurance.


print(str4.index("is")) #index will find the first occurence of the given character and return the index number, if it will not find anything then

print(str4.isalnum()) #isalnum will check the string is alphanumeric or not
print(str4.isalpha()) #isalpha will check the string is alphabet or not
print(str4.islower()) #islower will check the string is in lower case or not
print(str4.isprintable()) #isprintable will check the string is printable or not
print(str4.isspace()) #isspace will check the string is space or not
print(str4.istitle()) #istitle will check the string is title or not
print(str4.isupper()) #isupper will check the string is in upper case or not
print(str4.startswith("where")) #startswith will check the string is starting with the given character or not
print(str4.swapcase()) #swapcase will convert the upper case into lower case and lower case into upper case

print(str4.title()) #title will convert the first character of each word into upper case
 