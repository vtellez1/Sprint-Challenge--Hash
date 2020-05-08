def has_negatives(a):
    nums = {}
    result = [] #Need to return a list of nums with negs

    #Loop through each number in the list
    for num in a:
        #need to check if the absolute value of our number is in our dict..
        if nums.get(abs(num)):
            #If if is, we can add it to our result list
            result.append(abs(num))
        else:
            #If not we can add the absoulte value to our dict
            nums[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
