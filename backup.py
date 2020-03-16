def hasSubdirectories(path): 
    subdirectories = [x[0] for x in os.walk(path)]
    print(len(subdirectories))
    for subdirectory in subdirectories:
        print subdirectory
    print(len(subdirectories) != 0) 