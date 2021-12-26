




'''
leetcode = 128
------------------
Runtime: 184 ms, faster than 85.07% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 25.9 MB, less than 30.31% of Python3 online submissions for Longest Consecutive Sequence.
------------------
(1) : 0 <= nums.length <= 10^5
(2) : -10^9 <= nums[i] <= 10^9
'''



def LongestConsecutiveSequence(nums=list):
    # init
    output = 0
    nums = set(nums)
    # main
    for val in list(nums):
        # val is smallest contunuisABLE val
        if val - 1 not in nums:
            cur_val = val
            length = 0
            while cur_val in nums:
                cur_val += 1
                length +=1
            output = max(output, length)
    return output


if __name__ == '__main__':
    # basic unit test
    basic_test_case = [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]
    basic_test_case_sol = [4, 9]

    for i, case in enumerate(basic_test_case):
        sol = basic_test_case_sol[i]
        try:
            output = LongestConsecutiveSequence(nums=case)
        except:
            print('ERROR-{}'.format(str(i)))
        if sol == output:
            print('SuccessBasic-{}'.format(str(i)))
        else:
            print('FailureBasic-{}'.format(str(i)))
            print('output : ', output)
            print('sol : ', sol)
    