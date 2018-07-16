import random

rythmDict = {'unidad': 4, 'mitad': 2, 'cuarto': 1, 'octavo': .5}
probability = {'unidad': 1, 'mitad': 2, 'cuarto': 4, 'octavo': 6}
rythmicNames = ['unidad', 'mitad', 'cuarto', 'octavo']
soloRythm = []
sum = 0

while sum < 16:
    newNote = random.choice(rythmicNames)
    filter = random.randint(1,10)
    if filter <= probability[newNote]:
        soloRythm.append(newNote)
        value = rythmDict[newNote]
        sum += value
        if sum > 16:
            sum -= value
            soloRythm = soloRythm[:-1]
        
    
print(soloRythm)
    
