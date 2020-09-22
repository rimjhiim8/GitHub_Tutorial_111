#an object that is made from a class with a __len__ function
#that reurns 0 or false
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))        

#to check if an object is an integer or not
x=200
print(isinstance(x,int))