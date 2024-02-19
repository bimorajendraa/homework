# ask user for his/her full name
# print to console "Hello Jack Bauer, how are you?"
# print to console "Your name has 10 characters"
# print to console "Your name start with J"

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print("Hello {0} {1}, how are you?".format(first_name.title(), last_name.title() ) )

name = first_name + last_name
characters = len(name)  
print("Your name has {0} characters".format(characters) )

print ("Your name start with {0}".format(first_name[0]) )