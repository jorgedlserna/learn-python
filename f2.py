# If loop
print("Please type your name")
pwd=input()
if pwd=="Toro":
    print("Access granted.")
else:
    print("Access denied.")

# While loop
# If the user doesn't submit a name, we ask again
name=""
while name != "your name":
    print("Please type your name")
    name=input()
    # If the name is equal to Jorge then we exit of the while loop and print message
    if name=="Jorge":
        break
print("Thank you "+name)

# For loop
# Sum total + current index (num)
total=0
for num in range(101):
    total=total+num
print(total)

# For loop
# Print Toro 5 times with the current index (i)
for i in range(0,5):
    print("Toro "+str(i))
    