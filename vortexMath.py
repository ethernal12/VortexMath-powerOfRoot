# nikola tesla vortex mathematics---
def powerOfRoot(arrayPowerOfTwo):
    nums = []
    print(arrayPowerOfTwo)
    for i in range(len(arrayPowerOfTwo)):
        currentNum = arrayPowerOfTwo[i]
        print(currentNum)
        if len(str(currentNum)) == 1:
            nums.append(currentNum)
        if len(str(currentNum)) >= 2:
            sum = currentNum # 16       
            while len(str(sum)) >= 2:
                newSum = 0
                for j in range(len(str(sum))):
                    newSum += int(str(sum)[j])
                sum = newSum
            nums.append(sum)
        print(nums)

      
def powerOfTwo(N):
    root = []
    for i in range(N):
        rootNum = 2 ** i
        root.append(rootNum)
    return(root)


powerOfRoot(powerOfTwo(30))
