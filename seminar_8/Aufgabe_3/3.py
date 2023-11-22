def do_stuff(s1):
    arr = [0] * len(s1)
    for i in range(len(s1)):
        w = 2
        while w < s1[i] and s1[i] % w != 0:
            w *= 2
        print(w)
        #arr[i] = w
    #return arr
    # for i in range(len(arr)):
    #     arr[i] = arr[i] <= s1[i]


    #return arr

print(do_stuff([12, 6, 9]))

