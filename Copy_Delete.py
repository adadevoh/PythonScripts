from sys import argv
from os.path import exists

print "This is a simple file copy/deletion tool"

#copy .... 

def copy_file():
    print "Enter path to file to copy from"
    print "If same directory as script just enter 'file_name.extension' "
    from_file_name  = raw_input("Copy from : ")
    from_file = open (from_file_name)
    data = from_file.read()
    print "size in bytes to be copied: ", len(data)


    if not exists(from_file_name):
        print "sorry that file does not exist"
    else:
        print "\n"

        print "Enter path of file to copy to "
        dest_file = raw_input("Copy to : ")
        to = open(dest_file, "w+")
        to.writelines(data)


    to.close()
    from_file.close()
