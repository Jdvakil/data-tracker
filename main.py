import os
from queue import Empty
from re import L
import time
import a0
from datetime import date, datetime

PATH = "/mnt/nfs_data/roboset/v0.2/"

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
    
def log(text):
    f = open("log.txt", "a")
    with open("log.txt", "r") as file:
        if os.stat("log.txt").st_size != 0:
            last_line = file.readlines()[-1]
        else:
            last_line = 0
    sum = text - int(last_line)
    f.write(f"{text-int(last_line)}\n")
    f.close()

def publisher():
        p = a0.Publisher("topic")
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
            print(f"{i} - {total}")
            total = 0
        print(f"Sum - {sum * 25}")
        time.sleep(10)
        print("_____________________________________________________\n")
        return sum

def main():
    while True:
        
        if(datetime.time(datetime.now()).hour == 18 and datetime.time(datetime.now()).minute == 47 and datetime.time(datetime.now()).second == 0):
            test = publisher()
            log(test)
            print(test*25)

    

if __name__ == "__main__":
    main()
