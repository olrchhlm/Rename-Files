import os
path = raw_input("Bitte gib den Pfad an, in dem die Dateien liegen.")
files = os.listdir(path)

newName = raw_input("Was soll vor die Dateien geschrieben werden?")


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, newName+'-'+file))
