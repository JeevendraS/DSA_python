#+++++++++++++++++++++++++++ Bubble sort ++++++++++++++++++++++++++++++++++++
# list = [2,3,3,4,5,342,23,43]
# list = [1,2,3,4,5,6,7,9,8]
# list = [8,7,6,5,4,3,2,1]
list = [5,4,2,45,7,68,56,345,23,234,32,3,11,2,323,22,2]

class Sort:
    def __init__(self,list):
        self.list = list
    def Bubble_sort(self):
        for i in range(len(self.list)):
            stop = 0
            for j in range(len(self.list)-i-1):
                print(j)
                if self.list[j]>self.list[j+1]:
                    temp = self.list[j]
                    self.list[j]=self.list[j+1]
                    self.list[j+1]= temp
                    stop = 1
            if stop == 0:
                return 
    def Selection_sort(self):
        for i in range(len(self.list)):
            for j in range(i+1,len(self.list)):
                print(j)
                if self.list[i]>self.list[j]:
                    temp = self.list[i]
                    self.list[i]=self.list[j]
                    self.list[j]=temp 
    def Insertion_sort(self):
        for i in range(1,len(self.list)):
            min = i
            print(i)
            while min>0 and self.list[min-1]>self.list[min]:
                print(" ",i)
                temp = self.list[min-1]
                self.list[min-1]= self.list[min]
                self.list[min]= temp
                min -= 1
    def Quick_sort(self):
        if len(self.list)==0:
            return self.list 
        else:
            pivot = self.list[0]
            greater = [x for x in self.list[1:] if x>pivot]
            lesser = [x for x in self.list[1:] if x<pivot]
            print(2)
            return Sort(lesser).Quick_sort()+[pivot]+Sort(greater).Quick_sort()
    def Merge_sort(self):
        if len(self.list)==1:
            return self.list
        else:
            mid = len(self.list)//2
            left = Sort(self.list[:mid]).Merge_sort()
            right = Sort(self.list[mid:]).Merge_sort()
            i = j = k = 0
            num = len(left)+len(right)
            list = [0]*num
            while i<len(left) and j<len(right):
                if left[i]>right[j]:
                    list[k] = right[j]
                    k+=1
                    j+=1
                else:
                    list[k] = left[i]
                    k+=1
                    i+=1
            while i<len(left):
                list[k] = left[i]
                k+=1
                i+=1
            while j<len(right):
                list[k] = right[j]
                k+=1
                j+=1
            return list                    


            

                
                
                                                           
            
# l = Sort(li)
# # l.Bubble_sort() 
# # l.Selection_sort()
# l.Insertion_sort()             
# print(li)
l = Sort(list) 
# print(l.Quick_sort()) 
print    (l.Merge_sort())

            




