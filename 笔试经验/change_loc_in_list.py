a=[3,4,5,6,3,4]
def f(nums):
    if len(nums) == 0:
        return []
    i = 0
    while (i < len(nums)):
        print(i,nums)
        if nums[i] == nums[nums[i] - 1]:
            i = i + 1
        else:
            # tmp = nums[i]
            # nums[i] = nums[tmp - 1]
            # nums[tmp - 1] = tmp

            # tmp=nums[i]
            # nums[i]=nums[nums[i]-1]
            # nums[tmp-1]=tmp
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            # nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i] 这句是错误的，



            # tmp=nums[nums[i]-1]
            # nums[nums[i]-1]=nums[i]
            # nums[i]=tmp
    # print(nums)
    ans = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            ans.append(i + 1)
    return ans
print(f(a))

