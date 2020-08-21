queue = []
cmd = []
n = int(input())
for i in range(n):
    cmd.append(list(map(int, input().split())))
for i in range(n):
    if(cmd[i][0]==1):
        queue.insert(0,cmd[i][1])
    elif(cmd[i][0]==2):
        queue.pop(-1)
    else:
        print(queue[-1])
