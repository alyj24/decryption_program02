print("Problem 02 ~ Assignment 2".center(42,"="))

# pseudocode
# ask the user for an input and save its input
input_str = input("\033[91mGood Day! Please enter your input string: ")
# recognize each character of the input
output_str = "\033[95m"
for i in range(len(input_str)):
# if *, change it to a
  if input_str[i] == "*":
    output_str += "a"
# if &, change it to e
  elif input_str[i] == "&":
    output_str += "e"
# if #, change it to i
  elif input_str[i] == "#":
    output_str += "i"
# if +, change it to o
  elif input_str[i] == "+":
    output_str += "o"
# if !, change it to u
  elif input_str[i] == "!":
    output_str += "u"
  else:
    output_str += input_str[i]
# print the output
print(output_str)