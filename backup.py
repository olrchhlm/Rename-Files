import os
dir = "C:\Users\olere\Desktop\Testordner"

subdirectories = [x[0] for x in os.walk(dir)]
subdirectories.pop(0)

for subdirectory in subdirectories: 

    print(subdirectory) 

