def isAnagram(s: str, t: str) -> bool:
    s_ls = []
    t_ls = []

    s_ls.extend(s)
    t_ls.extend(t)
    s_ls.sort()
    t_ls.sort()
    if s_ls == t_ls:
        return True
    else:
        return False

print(isAnagram(s = "rat", t = "car"))