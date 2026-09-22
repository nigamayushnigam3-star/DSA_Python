arr = [10 , 11 , 9 , 8 , 7]
max = arr[0]
sl = arr[0]
for i in range(1,6):
    if arr[i] > max :
        sl = max 
        max = arr[i]
    else:
         if arr[i] > sl and  arr[i]!=max:
            sl = arr[i] 


