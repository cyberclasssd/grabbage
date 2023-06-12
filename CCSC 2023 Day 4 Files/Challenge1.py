#The password is below. Is it safe to put the password in the source code?

def checkPassword(password):
  return password == "flag{warming_up_the_legs}"

userInput = input("Please enter the correct password: ")

if (checkPassword(userInput)):
  print("Correct! The door to the next level unlocks.")
else:
  print("Incorrect! This earns you a suspicious glance from the guards.")