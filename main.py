def generate(numRows: int) -> list[list[int]]:
    result = [[1]]
    for i in range(numRows-1):
        temp_arr = [1]
        for j in range(i):
            temp_arr.append(result[i][j]+result[i][j+1])
        temp_arr.append(1)
        result.append(temp_arr)
    return result

