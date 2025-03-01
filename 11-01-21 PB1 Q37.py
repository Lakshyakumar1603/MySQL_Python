#11-01-2021 pb1 Q37

def Lshift(arr, n):
    print('Original array is :',arr)
    narr=Arr[n:]+Arr[:n]
    print('new arrary is :',narr)

#calling
Arr=eval(input('Enter a list :'))
n=int(input('Enter a number :'))
Lshift(Arr,n)
