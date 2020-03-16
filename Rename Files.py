import os
def renameFilesOnUpperLevel(path, newName):
    files = os.listdir(path)
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, newName+'-'+file))
    return

def renameFilesSubfolders():
    dir = "C:\Users\olere\Desktop\Testordner" 
    subdirectories = [x[0] for x in os.walk(dir)]
    subdirectories.pop(0)

    for subdirectory in subdirectories: 
        renameFilesOnUpperLevel(subdirectory, "2004-")

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
        renameFilesSubfolders()
    else:
        print("Bitte eine Funktion auswaehlen")
    return

functionSelector()