


file = open("file1.txt", "w+")

for i in range(10):
    file.write("This is line %d\n" % (i+1))

file.close()

print("to jest linia w pythonie")
