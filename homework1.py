string = input(str())
reverse = ""

for i in range(len(string)-1, -1, -1):
    reverse += string[i]

print(reverse)

if string == reverse:
    print("True")
else:
    print("False")

