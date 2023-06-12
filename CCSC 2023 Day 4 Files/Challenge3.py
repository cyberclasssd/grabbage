def checkPassword(password):
  if len(password) != 18:
    return False
  buffer = ""
  for i in range(9):
    buffer += password[i]
  for i in range(9):
    buffer += password[17-i]
  return buffer == "flag{m0vi}ffuts_gn"
 

userInput = input("Please enter the correct password: ")

if (checkPassword(userInput)):
  print("Congrats! The door moves to the side.")
else:
  print("Nope. The guards don't feed you dinner tonight.")