#explicit typecasting (user said to conver the data type)
string="45"
number=9
string_number =int(string) 
sum=number + string_number
print("the sum of number is ",sum)

#implicit typecasting to convert datatype
a=1
print(type(a))
b=4.7
c=a+b
print(type(b))
print("the sum of c","=" ,"a","+","b","is:",a+b)
print(type(c))
