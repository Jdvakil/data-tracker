import os
PATH="/mnt/nfs_data/roboset/v0.2/"

ls = next(os.walk(PATH))[1]
# for i in ls:
#     print(i)

sum = 0
total = 0
for i in ls:
    print(f"{i}: ")
    top = (next(os.walk(os.path.join(PATH,i)))[1])
    for task in top:
        dirname = os.path.join(PATH,i,task)
        for path,dir,file in os.walk(dirname):
            for f in file:
                if f.endswith(".pickle"):
                    sum+=1
                    total += 25
        print(f" - {task} - {sum} or {sum * 25} trajectories")
        sum = 0

print(f"Total: {total}")


