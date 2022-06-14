# len(12345)
# 
# Traceback (most recent call last):
#   File "d:/Test Project/100 Days Python/Day2/Type_Error_Checking_Conversion.py", line 1, in <module>
#     len(12345)
# TypeError: object of type 'int' has no len()


num_char = len(input("What is your name? "))
print("Your name has", num_char, "character.")
print("Your name has " + str(num_char) + " character.")

print("Data Type is a ", type(num_char))
print("Change a type of int to str", type(num_char), ">>>", type(str(num_char)))

# print("Your name has " + num_char + " character.")
# 
# Traceback (most recent call last):
#   File "d:/Test Project/100 Days Python/Day2/Type_Error_Checking_Conversion.py", line 9, in <module>
#     print("Your name has " + num_char + " character.")
# TypeError: can only concatenate str (not "int") to str