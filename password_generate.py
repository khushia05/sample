import random
import string

pass_len=6
charvalues=string.ascii_letters+string.digits+string.punctuation
password="".join([random.choice(charvalues)for i in range(pass_len)])

password=""
for i in range(pass_len):
    password+=random.choice(charvalues)

print("your random password is:",password)