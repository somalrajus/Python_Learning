"""
# print
print("Hello world !!");
x=5;
print(x)
name = 'Srihari' 
role = 'HOD'

print(name + role)

#Lists
my_list = [1,2,3,4]
print(my_list)
my_list_strings = [[1,2,3,4],[],'list1', 'test 1', 'test 3']
print(my_list_strings)
print(len(my_list_strings))


#sets every element in the set needs to be unique
my_set   = {1,2,3,4}
print(my_set)


n=1991
if((n%4 == 0) or ((n%400 ==0) and (n%100 !=0))):
    print('Leap year')



n=5
for i in range(1,n+1):
    print(i, end='')
    """

# class examples

class Stb:
    def __init__(self, name, platform):
        self.stbname = name
        self.platform = platform

    def stbdetails(self):
        print(self.stbname + ' is on ' + self.platform)

xwing = Stb('xwing', 'st412')
mr = Stb('mrbox', 'sti412')
amidala = Stb('Amidala', 'sti418')

xwing.stbdetails()
mr.stbdetails()
amidala.stbdetails()
