# Use a while loop, to simulate a child asking their parent for a piece of candy.
# Have the program keep looping until the user answers "yes", then have the program 
# output "Thank you." For example:


# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? yes
# Thank you.

#Coding starts here...
candy = ""
while candy != "yes":
    candy = input("May I have a piece of candy? ").lower()
    if candy == "yes":
        print("Thank you.")
    else:
        continue