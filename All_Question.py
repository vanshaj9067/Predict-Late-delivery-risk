# Question 1
# Python program to find sum
# of first n odd numbers
 
def oddSum(n) :
    sum = 0
    curr = 1
    i = 0
    while i < n:
        sum = sum + curr
        curr = curr + 2
        i = i + 1
    return sum
 
# Driver Code
n = 20
print (" Sum of first" , n, "Odd Numbers is: ",
                                oddSum(n) )
                                
  b)
  # Python implementation to find sum of
# first n even numbers
     
# function to find sum of
# first n even numbers
def evensum(n):
    curr = 2
    sum = 0
    i = 1
     
    # sum of first n even numbers
    while i <= n:
        sum += curr
         
        # next even number
        curr += 2
        i = i + 1
    return sum
 
# Driver Code
n = 20
print("sum of first ", n, "even number is: ",
      evensum(n))


c)def findSum(num):
        sumo = 0
        sume = 0
        x = 1
        cur = 0
        ans = 0
        while (num > 0):
            inc = min(x, num)
            num -= inc
            if (cur == 0):
                ans = ans + sumodd(sumo + inc) - sumodd(sumo)
                sumo += inc
            else:
                ans = ans + sumeven(sume + inc) - sumeven(sume)
                sume += inc
            x *= 2
            cur ^= 1
        return ans




# Question 2 

Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10). Write a program to perform following 
operations:
a. Print half the values of tuple in one line and the other half in the next line.
b. Print another tuple whose values are even numbers in the given tuple.
c. Concatenate a tuple t2=(11,13,15) with t1.
d. Return maximum and minimum value from this tuple.
                                                   code:
                                                   
 a. t1=(1,2,5,7,9,2,4,6,8,10) # we use indexing to split it in half ,indexing starts with 0
print("first half value",t1[0:5])  # it will not take value of element on index 5 . 
print("other half value",t1[5:10]) #it will not take value of element on index 10 ,in this case there is no index 10 though..

b.t1=(1,2,3,4,5,6,7,8,9,10)
n=list(t1)
list1=list()
for i in n:
    if i in n:
        if i%2==0:
            list1.append(i)
    p=tuple(list1)
print('tuple:',p)
print()


c.t1=(1,2,5,7,9,2,4,6,8,10) # Concatenate a tuple t2=(11,13,15) with t1,(Concatenate means adding).
t2=(11,13,15)
print(t1+t2)

d.t3=t1+t2 # Return maximum and minimum value from this tuple
print(t3)
print("Minimum value in ", t3, "is : ", min(t3))
print("Maximum value in ", t3, "is : ", max(t3))





#QUESTION 3

def main():
    ch=int(input('Enter 1-length , 2=max of 3 strings,3=to print , 4=number of words='))
    if ch==1:
        n=input('Enter a string:')
        l=len(n)
        print('The length of the string is=',l)
    elif ch==2:
        n1=input('Enter string 1=')
        n2=input('Enter string 2=')
        n3=input('Enter string 3=')
        print('The maximum of the 3 strings is=',max(n1,n2,n3))
    elif ch==3:
        a=input('Enter a string:')
        s=''
        a=list(a)
        for i in range(len(a)):
            if (i%2!=0):
                if a[i]==' ':
                    a[i]=' '
                else:
                    a[i]='#'
        for e in a:
            s=s+e
        print('the new string=',s)    
    elif ch==4:
         b=input('Enter a string=')
        c=0
        for ch in b:
            if ch==' ':
                c+=1
        a=c+1
        print('The number of words:',a)
    else:
        print('invalid choice') 
if __name__=='__main__':
    main()
