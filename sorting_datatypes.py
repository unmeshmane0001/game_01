string = str(input("enter the mixed statement that have char,digits and alphabates i will sort it :-"))

digit = 0
char=0
spchar=0
for i in string:
    if i.isdigit():
        digit = digit +1
    elif i.isalpha():
        char = char + 1
    else:
        spchar = spchar +1
print(f"digit in string is {digit}")
print(f" special characters in string {spchar}")
print(f"charactersin string {char}")

