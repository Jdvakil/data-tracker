import os
from re import L
from sre_constants import GROUPREF_EXISTS
import time
import csv
import datetime

PATH="/mnt/nfs_data/roboset/v0.2/"
def get_output():
    ls = next(os.walk(PATH))[1] #get the top dirs (rp00,01,...,0n)
    logstr = ""

    logstr += ("____________________________________________________________________\n\n")
    trajs = 0 #total trajs per task
    total = 0 #total trajs 
    for i in ls:  #go through each robopen
        logstr += (f"{i}: \n")
        top = (next(os.walk(os.path.join(PATH,i)))[1]) # go through each task in the robopen
        for task in top:#cycle through the tasks
            dirname = os.path.join(PATH,i,task)
            for path,dir,file in os.walk(dirname): #go through the task folders
                for f in file:#cycle through the files
                    if f.endswith(".pickle"):
                        trajs+=1
                        total += 25
            logstr += (f" - {task} - {trajs} or {trajs * 25} trajectories\n")
            trajs = 0

    logstr += (f"Total: {total}\n")
    return total,logstr

def text_logger(text,file):
    with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(text)
def main():
    #TODO Add a logger and more time structure
    total,log = get_output()
    text_logger([datetime.datetime.today().date(),total], "datetime.csv")    
main()
