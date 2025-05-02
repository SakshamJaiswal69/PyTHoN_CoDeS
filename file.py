
f1=open('my text.txt',"w+")
f1.write('hello world \nthis is my content')
f1.seek(0)
print(f1.read())
