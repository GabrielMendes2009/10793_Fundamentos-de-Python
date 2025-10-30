lst = [51, 34, 94, 634, 64, 34, 31, 64, 945, 65]

lst_triplo = [num * 3 for num in lst]
print(lst_triplo)

print("")

lst1 = ["51", "34", "94", "634", "64", "34", "31", "64", "945", "65"]

lst1_int = [int(num) for num in lst1]
print(lst1_int)

print("")

lista = ["10", "abc", "42", "python", "314", "100", "dfhdt", "7", "hhshgh", "0", "2025", "oi", "x", "99", "hello"]

nums = [int(i) for i in lista if i.isdigit()]
print(nums)

