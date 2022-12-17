def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

noOfTimes = 15

if noOfTimes <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence shown below:")
   for i in range(noOfTimes):
       print(recur_fibo(i))