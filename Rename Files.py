import os
path = 'D:/+Upload-(danach-loeschen)/2009'
files = os.listdir(path)
newName = raw_input("Bitte gib die Jahreszahl ein :) ")


for index, file in enumerate(files):
     os.rename(os.path.join(path, file), os.path.join(path, newName+'-'+file))