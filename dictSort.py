test = {"0": 2, "1": 3, "2": 7, "3": 4}


def sort(obj: dict):
    keys = obj.keys()
    values = obj.values()
    sorted_index = [i for i in range(len(obj))]
    for i in range(len(obj) - 1):
        mini = values[i]
        mini_index = i
        
        for j in range(i + 1, len(obj)):
            if mini > values[j]:
                mini = values[j]
                mini_index = j

                
