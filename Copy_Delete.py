from sys import argv
from os.path import exists

print "This is a simple file copy/deletion tool"

#copy .... 

print "Enter path to file to copy from"
print "If same directory as script just enter 'file_name.extension' "
copy_from_file  = raw_input("Copy from : ")
from_file = open (copy_from_file)
data = from_file.read()
print len(data)


if not exists(copy_from_file):
    print "sorry that file does not exist"
else:
    print "\n"

    print "Enter path of file to copy to "
    dest_file = raw_input("Copy to : ")
    to = open(dest_file, "w+")
    to.writelines(data)


to.close()
from_file.close()