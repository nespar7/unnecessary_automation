def writeIsEven(N):
    if N <= 1:
        print("go flip a switch")
        return
    
    print("\tif(N == 1) return false")
    
    parityMap = {
        True: "true",
        False: "false"
    }
    
    isEven = True
   
    for i in range(2,N+1):
        print(f"\telse if(N == {i}) return {parityMap[isEven]}")
        isEven = not isEven
        
    print("\telse return true")
    
if __name__ == "__main__":
    N = int(input("Enter N "))
    print("private bool isEv
