import os
import time
import shutil

def renameFilesOnUpperLevel(path, newName):
    files = os.listdir(path)
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, newName+'-'+file))
    return

def renameFilesSubfolders(path):
    renameFilesOnUpperLevel(path, "foo")

    print("hier gehts noch")

    subdirectories = [x[0] for x in os.walk(path)]
    subdirectories.pop(0)     

    destinationPath = path + "/" + "+Export"
    os.mkdir(destinationPath)

    for subdirectory in subdirectories: 
        timestamp = time.time()
        print(timestamp)
        print(subdirectory)
        renameFilesOnUpperLevel(subdirectory, str(timestamp))
        move(subdirectory, destinationPath)

def move(sourcePath, destinationPath): 
    sourceFiles = os.listdir(sourcePath)
    for sourceFile in sourceFiles:
        fileToMove = sourcePath + "/" + sourceFile
        print(fileToMove)
        shutil.move(fileToMove, destinationPath)


def functionSelector():
    print("Welche Funktion willst du ausfuehren?")
    print("Funktion a = Benenne Dateien und Ordner der obersten Ebene mit einem String um.")
    print("Funktion b = Bennene Dateien der obersten Ebene und Dateien in Unterordnern um, es wird ein Timestamp angefuegt.")
    input = raw_input("a oder b?")
    if (input == "a"): 
        path = raw_input("Bitte gib den Pfad an, in dem die Dateien liegen.")
        newName = raw_input("Was soll vor die Dateien geschrieben werden?")
        renameFilesOnUpperLevel(path, newName)
    elif (input == "b"):
        path = raw_input("Bitte gib den Pfad an, in dem die Dateien liegen.")
        renameFilesSubfolders(path)
    elif (input == "c"):
        path = raw_input("Bitte gib den Pfad an, in dem die Dateien liegen.")
    else:
        print("Bitte eine Funktion auswaehlen")
    return

functionSelector()