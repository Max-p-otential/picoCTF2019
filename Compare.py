import sys

class Compare:
    def __init__(self,file1,file2,mode):
        try:
            self.listA=list(open(file1,mode).read())
        except FileNotFoundError:
            print ("File A doesn't exist! Maybe it is spelled wrong?")
            exit()
        except:
            print ("Something went wrong! Maybe try it with option -b if they are Binary files")
            exit()
        try:
            self.listB=list(open(file2,mode).read())
        except FileNotFoundError:
            print ("File B doesn't exist! Maybe it is spelled wrong?")
            exit()
        except:
            print ("Something went wrong! Maybe try it with option -b if they are Binary files")
            exit()
        self.result=[]
        for i in range(len(self.listA)):
            if (i>= len(self.listB) or self.listA[i]!=self.listB[i]):
                self.result.append(self.listA[i])


def printHelp():
    print("Usage of Compare.py: Compare.py [options] filepath1 filepath2")
    print("Options: ")
    print("-h  : prints this help page")
    print("-b  : binary comparison between files (returns decimal if not specified)")
    print("-C  : tries to convert Bytes to Characters via ascii")
    print("-x  : converts output to hexadecimal")
    print("-s  : print the result as string; not as list (with whitespaces in between)")
    print("-ss : print the result as string; not as list (without whitespaces in between)")

def main():
    arguments=sys.argv[1:]
    argc= len(arguments)
    result=()
    if(len(arguments)<2):
        printHelp()
        exit()
    elif(arguments.count("-h")>=1):
        printHelp()
        exit()
    elif(arguments.count("-b")==1):
        result = Compare(arguments[argc-2],arguments[argc-1],"rb").result
    else:
        result = list(map(ord,Compare(arguments[argc-2],arguments[argc-1],"rt").result))
    if(arguments.count("-C")==1):
        result =list(map(chr,result))
    if(arguments.count("-x")==1):
        result =list(map(hex,result))
    if(arguments.count("-s")==1):
        result=' '.join(str(s) for s in result)
    elif(arguments.count("-ss")==1):
        result=''.join(str(s) for s in result)        
    print(result)   


if __name__ == "__main__":
    main()
    