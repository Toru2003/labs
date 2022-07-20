#1 Задача
def PrintRectangle(a, b, file):

    f=open((file),"w")
    f.write(a*"* "+"\n")
    for i in range (b-2):
        f.write( "*" + (a-2)*'  '+" *"+"\n" )
    f.write(a * "* " )
    f.close()
def PrintSquare(a, file) :
    f=open((file),"w")
    f.write(a*"* "+"\n")
    for i in range (a-2):
        f.write( "*" + (a-2)*'  '+" *"+"\n" )
    f.write(a * "* " )
    f.close()
PrintRectangle(8,4,r"output.txt")
PrintSquare(5,r"out.txt")




