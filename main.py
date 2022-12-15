import os
import time
import csv
import datetime
import sys

PATH="/mnt/nfs_data/roboset/v0.3"


def get_output():
    ls = next(os.walk(PATH))[1] #get the top dirs (rp00,01,...,0n)
    ls = sorted(ls)
    logstr = ""

    logstr += ("____________________________________________________________________\n\n")
    trajs = 0 #total trajs per task
    total = 0 #total trajs 
    task_traj_count = 0
    for i in ls:  #go through each robopen
        logstr += (f"{i}: \n")
        top = (next(os.walk(os.path.join(PATH,i)))[1]) # go through each task in the robopen
        for task in top:#cycle through the tasks
            dirname = os.path.join(PATH,i,task)
            for path,dir,file in os.walk(dirname): #go through the task folders
                for f in file:#cycle through the files
                    if f.endswith(".pickle"):
                        traj_count = (int((os.path.splitext(f)[0][-3:-1]).strip("_")))
                        trajs+=1
                        total += traj_count
                        task_traj_count += traj_count
            logstr += (f" - {task} - {trajs} or {task_traj_count} trajectories\n")
            trajs = 0
            task_traj_count = 0

    logstr += (f"Total: {total}\n")
    return logstr, total

def csv_logger(text,file):
    if file.endswith(".csv"):
        with open(file,'a') as f:
            writer = csv.writer(f)
            writer.writerow(text)
            count = 0
        while count < 3:
            sys.stdout.write(f"\r - logging to {file}")
            time.sleep(0.7)
            count +=1
            sys.stdout.write(f"\r - logging to {file}.")
            time.sleep(0.7)
            count += 1
            sys.stdout.write(f"\r - logging to {file}..")
            time.sleep(0.7)
            count += 1
            sys.stdout.write(f"\r - logging to {file}...\n")
            time.sleep(0.7)
            count += 1
        print(f" - Logged to {file}")
    else:
        print(f" - Nothing was logged to {file}, enter a file ending in '.csv'")

def text_logger(text,file):
    if file.endswith(".txt"):
        with open(file,'a') as f:
            f.write(text)
            count = 0
        while count < 3:
            sys.stdout.write(f"\r - logging to {file}")
            time.sleep(0.7)
            count +=1
            sys.stdout.write(f"\r - logging to {file}.")
            time.sleep(0.7)
            count += 1
            sys.stdout.write(f"\r - logging to {file}..")
            time.sleep(0.7)
            count += 1
            sys.stdout.write(f"\r - logging to {file}...\n")
            time.sleep(0.7)
            count += 1
        print(f" - Logged to {file}")
    else:
        print(f" - Nothing was logged to {file}, enter a file ending in '.txt'")

def main():
    log,total = get_output()
    print(log)
    text_logger(log, "log.txt")
    csv_logger([datetime.datetime.today().date(),total], "datetime.csv") 

if __name__ == "__main__":
    while True:
        if datetime.datetime.now().hour == 23 and datetime.datetime.now().minute == 59 and datetime.datetime.now().second == 0:
            main()

