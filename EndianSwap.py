import sys

class EndSwap:
    def __init__ (self,filepath,size):
        try:
            self.byteList=list(open(filepath,"rb").read())
        except FileNotFoundError:
            print ("File A doesn't exist! Maybe it is spelled wrong?")
            exit()
        except:
            print ("Something went wrong!")
            exit()
        self.result=self.Swapbytes(self.byteList,size)
    
    def Swapbytes (self,bytelist,wsize):
        result=[]
        lenn = len (bytelist)
        while (len(bytelist)>wsize):
            if ((len(bytelist)/wsize)%1000 < 1):
                print(str(len(bytelist)/wsize) + " / " + str(lenn/wsize))
            rl = []
            for i in range(wsize):
                rl.insert(0,bytelist.pop(0))
            result=result +rl
        result = result + bytelist
        return result



def printHelp():
    print("Usage of EndianSwap.py: EndianSwap.py filepath Wordsize")

def main():
    arguments=sys.argv[1:]
    argc= len(arguments)
    result=()
    if(len(arguments)!=2):
        printHelp()
        exit()
    else:
        result = EndSwap(arguments[0],int(arguments[1])).result
        open(arguments[0]+".rev", "wb").write(bytearray(result))
        exit()






if __name__ == "__main__":
    main()