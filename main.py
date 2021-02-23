import sys
import time

print('Generating full prime List up to 10000000')
start_time=time.time()
primeList=[]
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p+= 1
    

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            primeList.append(p)
    return primeList
primeList=SieveOfEratosthenes(10000000)
end_time=time.time()
time_lapsed=end_time - start_time
#print(primeList)
print('Done in '+str(int(time_lapsed))+' seconds.')
#exit=input('a.')
start=input('Do you want to find as many twin primes as possible (faster) or find twin primes in a certain range (far slower). (1 or 2)')
if start==('1'):
  for i in range(1,len(primeList)):
    if primeList[i]+2==primeList[i+1]:
      print(str(primeList[i])+' and '+str(primeList[i+1])+' are twin primes.')
if start==('2'):
  x=int(input('What number to start at?'))
  y=int(input('What number to end at?'))
  for i in range (x,y+1):
    for j in range(1,i+1):
      if i==primeList[j] and i+2==primeList[j+1]:
        print(str(primeList[j])+' and '+str(primeList[j+1])+' are twin primes.')
        break
else:
  