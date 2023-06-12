def checkPassword(password):
  result = ""
  for char in password:
    result += chr(ord(char) + 1)
  return result == "gmbh|ti2guz`c1j~"

userInput = input("Please enter the correct password: ")

if (checkPassword(userInput)):
  print("You kick the door down!! B)")
else:
  print("Oh no, the queen sends more guards!")