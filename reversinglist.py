class reverse:
    def __init__(self,val:list):
        self.value=val
    def reverse(self):
          self.value.sort(reverse=True)
          print("The sorted values are",self.value)
     
        
obj=reverse([1,4,5,4,5,3,5,3])
obj.reverse()
