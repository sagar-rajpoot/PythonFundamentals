
# r - reading , r+ reading and writing , w writing , w+ writing and reading, a appending, x filecreation

# f = open("./data/datafile.txt","r")
# print(f.read())
# f.close()

# f = open("./data/datafile.txt","w")
# f.write("Let me add things..opps! it will deleted previous content")
# f.close()


f = open("./data/datafile.txt","a")
f.write(" ok Now let me keep writing")
f.close()

# -x did not worked
# f = open("./data/datafile2.txt","x")
# f.close()








