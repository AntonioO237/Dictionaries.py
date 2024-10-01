# Challenge 
# Create a list of friends
# Make sure the initial list is none 
friends = ["Caiden", "Logan", "Dexter", "Johny", "Mr.Mirek", "Casper"]
print(friends)
# add a new friend to the list, add at least 5 friends 
friends.append("Mr.Salazar")
friends.append("Martha")
friends.append("Bruce Wayne")
friends.append("Phone")
friends.append("Usain Bolt")
print(friends)
# remove a friend
friends.remove("Martha")
print(friends)
# insert a friend at a specific index maybe 2
friends[2] = "pillow"
print(friends)
# print the list of friends
for friend in friends:
    print(len(friends))
    print(friend)
# loop through the list and print the friends name
    friendRequest = input("Will you be my friend? What's your name?: ")
    friends.append(friendRequest)
    print(friends)
    print(len(friends))
# if the list is greater than 10 break
    print(friends)
    if len(friends) > 10:
        break