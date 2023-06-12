def checkPassword(password):
  return len(password) == 15 and password[3] == 'g' and password[5] == '5' and password[1] == 'l' and password[4] == '{' and password[14] == '}' and password[9] == 'm' and password[12] == '3' and password[0] == 'f' and password[13] == 'd' and password[10] == 'b' and password[2] == 'a' and password[6] == 'c' and password[8] == '4' and password[7] == 'r' and password[11] == 'L'

userInput = input("Please enter the correct password: ")

if (checkPassword(userInput)):
  print("Ding Ding Ding! The door swings wide open.")
else:
  print("Wrong! The guard pokes you with his stick warily.")