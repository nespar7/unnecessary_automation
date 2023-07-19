def writeIsEven(file, N):
    if N <= 1:
        file.write("go flip a switch")
        return
    
    file.write("\tif(N == 1) return false")
    
    parityMap = {
        True: "true",
        False: "false"
    }
    
    isEven = True
   
    for i in range(2,N+1):
        file.write(f"\telse if(N == {i}) return {parityMap[isEven]}")
        isEven = not isEven
        
    file.write("\telse return true")
    
if __name__ == "__main__":
    N = int(input("Enter N "))
    file = open("write_is_even.cpp", "w")
    file.write("private bool isEven(int N) {")
    writeIsEven(file, N)
    file.write("}")
    file.close()
