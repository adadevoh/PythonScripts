from sys import argv


script, filename = argv

handler = open(filename, "w")
handler.write("hello governor")
handler.close()

print("enter file name again")
filename = raw_input("> ")
handler = open(filename)

print handler.read()
print ("now enter stuff to write to the file")
msg = raw_input("> ")

handler = open(filename, "a")
handler.write("\n" + msg)

handler.close()

