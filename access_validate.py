import validate
print("Let's check for validity :\n")

number = '03001234567'

#access the function insdie the imported module
if validate.validate_num(number):
    print('num is valid')
else:
    print('num is invalid')

password = 'key123'

#access the function insdie the imported module
if validate.validate_pass(password):
    print('password is valid')
else:
    print('password is invalid')