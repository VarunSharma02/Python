class array:
    def __init__(self,ls):
        self.ls =ls
    def validity(self,m,n):
        return len=(self.ls)==m*n
    
    def create_matrix(self,m,n):
        self.M=[]
        tmp=[]
        count=0
        for i in self.ls:
            tmp.append(i)
            count+=1
            if count==n:
             self.M.append(tmp)
             tmp=[]
             count=0

            
    def display_matrix(self):
        for i in self.M:
            print(*i,sep='\t')
# input for list of munbers
            
lst=list(map(int,input.split()))
#input for matrix dimension
row,column=list(map(int,input.split()))

arr=array(lst)
if arr.validity(row,column):


