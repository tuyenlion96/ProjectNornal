def return_distance_handle(nums, target, start):
    __min_distance = 0
    # If the start value = index of target
    if nums[start - 1] == target:
        print("So lucky")
    else:  # another case
        if (start == 0) or (start == len(nums) - 1):
            # If start is zero
            __min_distance = nums.index(target, 0, len(nums))
        else:
            # Cut nums list to 2 list: [0, start] + [start, len(nums) - 1]
            try:
                __min_distance = nums.index(target, 0, start - 1)

                # Checking at the remain list just the length [start, the index of target]
                # If have value. Compare with the previous value
                # If not have value, using the previous value to calculation the minimum distance
                try:
                    __another_min = 0
                    # [0, start] <= [start, len(nums) - 1]. Checking on list remain
                    if (start + __min_distance) >= (len(nums) - 1):
                        __another_min = nums.index(target, start + 1, start + __min_distance)
                    else:
                        __another_min = nums.index(target, start, len(nums) - 1)

                    if abs(__another_min - start) < abs(__min_distance - start):
                        __min_distance = __another_min

                except:
                    print("List remain is not contain " + str(target))

            except:
                __min_distance = nums.index(target, start, len(nums) - 1)
    return abs(__min_distance - start)


# For running
arr = [10, 20, 30, 80, 50, 70, 80, 80, 70]
target = 80
start = 5
value = return_distance_handle(arr, target, start)
print("Value: " + str(value))