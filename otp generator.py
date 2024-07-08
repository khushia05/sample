import random
def generate_otp():
# Generate a random number between 100000 and 999999
  otp=random.randint(1, 9)
  return otp
print(generate_otp())
