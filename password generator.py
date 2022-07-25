import random
uppercaseletter = chr(random.randint(65,90))
lowercaseletter = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
lowercaseletter3 = chr(random.randint(97,122))
number = chr(random.randint(48,57))
specialChar1 = chr(random.randint(32,64))
specialChar2 = chr(random.randint(91,96))
specialChar3 = chr(random.randint(123,126))
specialChar4 = chr(random.randint(145,148))

password = specialChar1+specialChar2+specialChar3+specialChar1+number+lowercaseletter+lowercaseletter2+lowercaseletter3+uppercaseletter

def shuffle(string):
    Templist = list(string)
    random.shuffle(Templist)
    return ''.join(Templist)
print(shuffle(password))
