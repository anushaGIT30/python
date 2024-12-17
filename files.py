f=open('file','r')
print(f.read()) #it displays the entire data in the fille

#print(f.readline()) reads only one line

f1=open('file1','w')
print(f1.write("something"))

f2=open('file1','a')
print(f1.write("good"))


for data in f:
    f1.write("this is ")

    print(f1.write())
