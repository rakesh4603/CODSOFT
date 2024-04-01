import random
import string
chars=string.ascii_letters+string.digits+string.punctuation
length=int(input("ENTER THE PASSWORD LENGTH: "))
password=''.join(random.sample(chars,length))
print("This is your password: ",password)

