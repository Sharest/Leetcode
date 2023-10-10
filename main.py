def isHappy(n: int) -> bool:
    check = set()

    while True:
        if n == 1:
            return True
        elif n in check:
            return False
        check.add(n)

        ls = []
        while n // 10 != 0:
            z = n % 10
            n = n // 10
            ls.append(z)
        ls.append(n)
        ls.reverse()
        
        sq_ls = [pow(i, 2) for i in ls]
        n = sum(sq_ls)   
