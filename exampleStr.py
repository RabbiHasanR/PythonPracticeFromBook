import string
str=input("please enter sentence: ")

str_up= ''.join(c for c in str if c.isupper())
print(str_up)
str_lo= ''.join(c for c in str if c.islower())
print(str_lo)
str_digit= ''.join(c for c in str if c.isdigit())
print(str_digit)

all_normal_characters = string.ascii_letters + string.digits

def is_special(character):
  return character not in all_normal_characters

special_characters =''.join(character for character in str if is_special(character))
print(special_characters)