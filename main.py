import os
from re import L

PATH = "/mnt/robopen_dataset/robopen_dataset/v0.2"

def get_dir():
    return next(os.walk(PATH))[1]
def get_names():
    names = get_dir()
    names_stripped = []
    for i in names:
        names_stripped.append(i.split("_"))
    count = 0
    while count < len(names_stripped):
        if names_stripped[count][-2:-1] == "data":
            names_stripped[count].pop()
        count+=1
        
    names_final = []  
    temp = ""  
    for i in names_stripped:
        for j in i:
            temp+=j + " "
        names_final.append(temp.rstrip())
        temp = ""
    return(names_final)

def main():
    sum = 0
    total = 0
    ls = get_dir()
    names = get_names()
    for i in ls:
        DIR_PATH = os.path.join(PATH,i)
        for root, dirs, files in os.walk(DIR_PATH):
            for j in files:
                if j.endswith(".pickle"):
                    #print(j)
                    total+=1
                    sum+=1

        print(f"{i} - {total*25}")
        total = 0

    print(sum * 25)

if __name__ == "__main__":
    main()