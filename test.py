# import os
PATH = "/mnt/robopen_dataset/robopen_dataset/v0.2"

# ls = os.listdir(PATH)
# print(ls)
# total = 0
# arr = []
# for i in ls:
#     for root, dirs, files in os.walk(os.path.join(PATH,i)):
#         for j in files:
#             if j.endswith(".pickle"):
#                 #print(f"dir - {dirs}")
#                 #print(f"root - {root}")
#                 print(f"file - {j}")
#                 total+=1
#                 print(total)
#                 arr.append(total)
#         total = 0

# print(arr)
import os

# def Count_files_in_subd():
#     for root, dirs, files in os.walk(PATH):
#         for i in files:
#             if i.endswith(".pickle"):
#                 print ("{} in {}".format(i, root))

# Count_files_in_subd()
# file_list = []
# for root, dirs, files in os.walk(PATH):
#     for file in files:
#         file_list.append(os.path.join(root,file));
# total = 0
# for trlFile in file_list:
#     if trlFile.endswith(".pickle"):
#         total+=1

# print(total*25)
# test = os.listdir(PATH)
# for j in test:

#     ls = (j.split("_"))
#     name = []
#     for i in ls:
#         if i != "data":
#             name.append(i)
#         if i == "data":
#             break
#     traj = ls[-2:-1][0]

#     print(traj)
#     print((" ".join(name)))

cmt = next(os.walk(PATH))[1]


print(cmt[1])
name = cmt[1].split("_")
new_name = []
for i in name:
    if i != "data":
        new_name.append(i)


print(name)
check = (" ".join(new_name))
testDict = dict()
temp = []
#temp = os.path.join(PATH,cmt[1])
for root,dirs,files in os.walk(os.path.join(PATH,cmt[1])):

    temp.append(os.path.join(root,files))
    print(os.path.join(root,files))

print(check)
testDict[str(check)] = temp
print(testDict)