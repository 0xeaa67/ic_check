def idcardcheck(id):
    arr = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    map = "10X98765432"
    ans = 0
    for i in range(17):
        ans += int(id[i]) * int(arr[i])
    if map[ans % 11] == id[-1]:
        return True
    print(map[ans % 11])
    return False


# id = '101234567891234567'
id = '11010119900307395X'
print(idcardcheck(id))

