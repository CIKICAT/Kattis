cases=int(input())
xlist=[""]*(cases)
alphalist=["A","B","C","D","E","F","G","H","I","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
status=""
mx=0
for i in range(cases):
    x=str(input())
    xlist[i]=x[0]
for i in range(cases):
    for al in range(len(alphalist)):
        if(xlist[i]==alphalist[al]):
            if(mx==0):
                mx=al
                break
            else:
                if(status==""):
                    if(al<mx):
                        status="d"
                    elif(al>mx):
                        status="i"
                    mx=al
                    break
                elif(status=="d"):
                    if(al<mx):
                        status="d"
                    elif(al>mx):
                        status="e"
                    mx=al
                    break
                elif(status=="i"):
                    if(al<mx):
                        status="e"
                    elif(al>mx):
                        status="i"
                    mx=al
                    break
    if(status=="e"):
        break
if((status=="e")|(status=="")):
    print("NEITHER")
elif(status=="d"):
    print("DECREASING")
elif(status=="i"):
    print("INCREASING")
