
x = input("Please input a text/character: ")

checkNumber = sum(c.isdigit() for c in x)
checkString = sum(c.isalpha() for c in x)
checkWhitespace = sum(c.isspace() for c in x)
specialChars = len(x) - checkNumber - checkString - checkWhitespace
stringCount = len(x)

sd = "Characters = {}, Digits = {},  Symbol = {} Spaces = {}"
s = sd.format(str(checkString), str(checkNumber), str(specialChars), str(checkWhitespace))
print(s)
s2 = "Total characters, digits, and symbols count is: {}"
ss = s2.format(str(stringCount))
print(ss)

