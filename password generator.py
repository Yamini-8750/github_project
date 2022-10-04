import random

def gen_pswd(length):
    upper_alpha = [chr(x) for x in range(65, 91)]#this is and array of all upper alphabets
    lower_alpha = [chr(y) for y in range(97,113)]#this is an array of all lowercase alphabets
    num = [str(z) for z in range(0, 10)]
    special = ['@', '_', '/']
    
    pswd = ''#initially the pswd string is empty
    characters = [upper_alpha, lower_alpha, num, special]
    
    for i in range(length):#this function will generate random characters and this will be added in string pswd
        #to generate random character from array random() function from random module is used
        lst = random.choice(characters)
        pswd += random.choice(lst)
        
    return pswd
for j in range(15):#the password generatoe fucntion is called !5 times it could be any number of times
    print("Password{} is:".format(j+1),gen_pswd(random.randint(5,15)))#the length of the password is aldo random it could be of any size between 5 adn1 5 both inclusive

