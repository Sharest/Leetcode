from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    result: str = ''
    if len(strs) == 1:
        result = strs[0]
        return result

    min_len_str: str = min(strs, key=len)

    for i in range(len(min_len_str)):
        for j in range(len(strs)):
            temp_str: str = ''
            if min_len_str[:i+1] == strs[j][:i+1]:
                temp_str = min_len_str[:i+1]
            else:
                break
        else:
            result = temp_str
    return result


print(longestCommonPrefix(["ab", "a"]))