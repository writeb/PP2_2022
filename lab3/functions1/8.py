l = list(map(int, input().split()))
def spy_game(nums):
    for i in range(0,len(nums)):
        first_0=nums.index(0)
        second_0=nums.index(0, first_0+1)
        sev=nums.index(7)
        if nums[first_0:second_0+1]!=sev and sev>second_0:
            return True
        else:
            return False
print(spy_game(l))