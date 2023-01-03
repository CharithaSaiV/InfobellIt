def power_set(lst):
    pw_set = [[]]

    for i in range(0,len(lst)):
        for j in range(0,len(pw_set)):
            ele = pw_set[j].copy()
            ele = ele + [lst[i]]
            pw_set = pw_set + [ele]

    return pw_set
print(power_set(1,2,3))
