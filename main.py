import os
from queue import Empty
from re import L
import time
import a0
from datetime import date, datetime
import csv

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
    
def log_text(text, file):
    f = open(file, "a")
    if file == "log.txt":
        with open(file, "r") as filename:
            if os.stat(file).st_size != 0:
                last_line = filename.readlines()[-1]
            else:
                last_line = 0
            sum = text - int(last_line)
    else:
        sum = text
    f.write(f"{sum}\n")
    print(f"logged to: {file}")
    f.close()

def log_csv(text,file):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(text)

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
        return sum * 25

def main():
    while True:
        test = publisher()
        if(datetime.time(datetime.now()).hour == 23 and datetime.time(datetime.now()).minute == 59 and datetime.time(datetime.now()).second in range(0,10)):
            log_text(test, "log.txt")
            field = [datetime.now(), test]
            log_csv(field, "date_logs.csv")

    

if __name__ == "__main__":
    main()
