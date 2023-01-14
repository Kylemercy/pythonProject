hotel = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
room = [ ]
taken = 5

print("*********************************")
print("welcome to hotel costal Rings!")
print("*********************************")
print("please do choose room number you would love to stay in ")
print("###############################")
print("the are 20 rooms available")
print("###############################")

while taken >= 1 :
   choice = int(input("Enter the room number of your choice: "))


   if choice not in hotel:
     print("room number is don't exists")

   elif choice in room:
     print("sorry room is taken already")
     print("please choose another room")

   else:
     room.append(choice)
     print("welcome Room of choice is available")
     print("Here is your room key")
   taken -= 1


print("\n")
print("checking  for available rooms")

for i in hotel:
    mit = [ ]
    if i not in room:
      mit.append(i)
      print((mit),end = " ")

else:
  print("\n")
  print("This are the available rooms remaining")