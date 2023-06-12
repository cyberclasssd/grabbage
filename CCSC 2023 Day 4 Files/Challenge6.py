def checkPassword(password):
  if len(password) != 14:
    return False
  for i in range(len(password), 2):
    if ord(password[i]) > ord(password[i+1]):
      return False
  return True

userInput = input("Please enter the correct password: ")

if (checkPassword(userInput)):
  print("You kick the door down!! B)")
else:
  print("Oh no, the queen sends more guards!")