import heapq
#entender melhor o heapq e revisar o codigo 
class Solution:
    def minOperations(self,a,n):
        # code here
        cnt=0
        queue=[]
        for i in range(n):
            print(i)
            if len(queue)>0 and queue[0]<a[i]:
                print("entra aqui ?")
                cnt+=a[i]-heapq.heappop(queue)
                heapq.heappush(queue,a[i])
                
                
            heapq.heappush(queue,a[i])
            print(heapq)
        return cnt



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    print(t)
    for _ in range(t):
        # n=(input())
        # print(n)
        a=[int(x) for x in input().strip().split()]
        print(a)
        obj=Solution()
        print(obj.minOperations(a,t))

