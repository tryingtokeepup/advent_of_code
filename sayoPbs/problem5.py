"""
Like in other programming languages, the only way to be able to mutate the iterable while iterating over it is to do so in reverse. When you remove elements the remaining list shifts left, but since you're iterating left it's always a step ahead of the shift and therefore won't skip over elements like when you iterate forward. The same goes for appending items while iterating. you can only append to the end. I'm not sure if there's an edge case where this makes since, but shifting the entire list every time you need to remove something is so incredibly slow that one should not even consider it. Take the following example:

import time

nums = list(range(15**5))

# creating a new list with only the items we want
start = time.perf_counter()
new_list = [i for i in nums if i % 2 == 0]
print('time =', time.perf_counter() - start)
print('len =', len(new_list))

# removing undesirable elements from an existing list
start = time.perf_counter()
for i in range(len(nums)-1, -1, -1):
    if nums[i] % 2 != 0:
        del nums[i]
print('time =', time.perf_counter() - start)
print('len = ', len(nums))
results:

time = 0.06529630000000002
len = 379688
time = 27.1267876
len =  379688
"""
