from random import randint

def convert(palabra, random = False):
    if(palabra == 'acuario'):
        return(randint(1, 10) if random else 10)
    elif(palabra == 'piscis'):
        return(randint(11, 20) if random else 20)
    elif(palabra == 'cancer'):
        return(randint(21, 30) if random else 30)
    elif(palabra == 'sagitario'):
        return(randint(31, 40) if random else 40)
    elif(palabra == 'escorpio'):
        return(randint(41, 50) if random else 50)
    elif(palabra == 'libra'):
        return(randint(51, 60) if random else 60)
    else:
        return(randint(61, 100) if random else 100)