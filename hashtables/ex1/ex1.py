def get_indices_of_item_weights(weights, length, limit):
    memory = {}

    for i in range(length):
        #Check if already exists in memory
        value = memory.get(limit-weights[i])
        #if we find the value in memory:
        if value is not None:
            #can return a tuple with the index
            return (i, value)
         #If there is not a value in memory           
        else:
        #Set key to current value, value at index
            memory[weights[i]] = i
    print(memory)
 
    return None    

