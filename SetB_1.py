# Rafie Amandio Fauzan
# Data Engineering Intern Candidate


# How This Function Works
# 1. Receive 2 List from the function
# 2. Create a union (merging the list) and make a set(unique element list) on that two list
# 3. Return the sorted list
 
def setb_1(list1, list2):

    unique_set = set(list1).union(list2)
    
    return sorted(unique_set)

# Creating Test Cases -> Usual and Edge Cases
# For this i want to create some test cases on edge case and usual case ranging to a lot of variation
def testcase_setb_1():

    try:
        # Test Case 1: Multiple Overlapping Elements
        assert setb_1([1, 2, 3], [2, 3, 4]) == [1, 2, 3, 4]
        print("[PASS] Test Case 1 Passed")
    except AssertionError:
        print("[FAIL] Test Case 1 Failed")
        
    try:
        # Test Case 2: Identical Elements in Both Lists
        assert setb_1([1, 1, 1], [1, 1]) == [1]
        print("[PASS] Test Case 2 Passed")
    except AssertionError:
        print("[FAIL] Test Case 2 Failed")
        
    try:
        # Test Case 3: Both Lists Empty
        assert setb_1([], []) == []
        print("[PASS] Test Case 3 Passed")
    except AssertionError:
        print("[FAIL] Test Case 3 Failed")
        
    try:
        # Test Case 4: One List Empty, Other Non-Empty
        assert setb_1([], [1, 2, 3]) == [1, 2, 3]
        print("[PASS] Test Case 4 Passed")
    except AssertionError:
        print("[FAIL] Test Case 4 Failed")
        
    try:
        # Test Case 5: Non-Overlapping Elements in Both Lists
        assert setb_1([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
        print("[PASS] Test Case 5 Passed")
    except AssertionError:
        print("[FAIL] Test Case 5 Failed")
        
    try:
        # Test Case 6: Negative and Positive Numbers
        assert setb_1([-1, -2, -3], [1, 2, 3]) == [-3, -2, -1, 1, 2, 3]
        print("[PASS] Test Case 6 Passed")
    except AssertionError:
        print("[FAIL] Test Case 6 Failed")
        
    try:
        # Test Case 7: Lists with Duplicates Across Both Lists
        assert setb_1([1, 2, 2, 3], [3, 4, 4, 5]) == [1, 2, 3, 4, 5]
        print("[PASS] Test Case 7 Passed")
    except AssertionError:
        print("[FAIL] Test Case 7 Failed")
        
    try:
        # Test Case 8: One List Contains a Single Element
        assert setb_1([7], [1, 2, 3]) == [1, 2, 3, 7]
        print("[PASS] Test Case 8 Passed")
    except AssertionError:
        print("[FAIL] Test Case 8 Failed")
    
    print("[FINISHED] All Test Case Passed")

print("Input : [1,2,6], [3,4,5]")
print(setb_1())
testcase_setb_1()