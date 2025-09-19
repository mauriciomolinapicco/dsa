def smallerNumbersThanCurrent(nums):
    temp=sorted(nums)
    d={}
    print(temp)
    for i, num in enumerate(temp):
        print(f"i: {i} --num: {num} --d:{d}")
        if num not in d:
            d[num]=i
    ret=[]
    for i in nums:
        print(d[i])
        ret.append(d[i])
    return ret

smallerNumbersThanCurrent([8,1,2,2,3])