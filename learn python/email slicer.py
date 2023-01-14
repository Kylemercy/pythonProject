# email slicer
email = input("Enter your email: \n").strip()
username = email[: email.index("@")] #this stops immediately it reaches the @
domain = email[email.index("@")+1:] # this starts immmediately after @ 
print(f"your username is {username}.\ndomain name is {domain}.")