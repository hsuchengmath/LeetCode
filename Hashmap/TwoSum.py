


'''
leetcode = 1
------------------
Runtime: 56 ms, faster than 89.25% of Python3 online submissions for Two Sum.
Memory Usage: 17.6 MB, less than 8.52% of Python3 online submissions for Two Sum.
------------------
(1) : 2 <= nums.length <= 10^4
(2) : -10^9 <= nums[i] <= 10^9
(3) : -10^9 <= target <= 10^9
(4) : Only one valid answer exists.
'''





def TwoSum(nums=list, target=int):
    # mapping val into index
    val2index_set = dict()
    for i, val in enumerate(nums):
        if val not in val2index_set:
            val2index_set[val] = set()
        val2index_set[val].add(i)
    # find diff index
    for i in range(len(nums)-1):
        val = nums[i]
        diff = target - val
        if diff in val2index_set:
            real_index_set = list(val2index_set[diff] - {i})
            if len(real_index_set) != 0:
                diff_index = real_index_set[0]
                return [i, diff_index]





if __name__ == '__main__':
    # basic unit test
    basic_test_case = [([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6)]
    basic_test_case_sol = [[0,1], [1,2], [0,1]]

    for i, case in enumerate(basic_test_case):
        sol = basic_test_case_sol[i]
        try:
            output = TwoSum(nums=case[0], target=case[1])
        except:
            print('ERROR-{}'.format(str(i)))
        if sorted(sol) == sorted(output):
            print('SuccessBasic-{}'.format(str(i)))
        else:
            print('FailureBasic-{}'.format(str(i)))
            print('output : ', output)
            print('sol : ', sol)
    

