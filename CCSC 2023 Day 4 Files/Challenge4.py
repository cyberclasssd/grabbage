def checkPin(pin):
  pin = pin + 9
  pin = pin * 10
  if (pin % 2 == 0):
    pin = pin - 2
  else:
    pin = pin + 2
  return (pin == 398)

userInput = input("Please enter the correct password: ")
userInput = int(userInput)

if (checkPin(userInput)):
  print("You kick the door down!! B)")
else:
  print("Oh no, the queen sends more guards!")