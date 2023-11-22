# input : [[1, 2, 3, 4],[4, 5, 2, 1],[7 ,2, 8, 5, 1, 4]]
# oupu :[1,4]


def gemeinsame_elemente(l):
    out_list = []
    d = {}
    for lista in l:
        for elem in lista:
          if elem in d:
              d[elem] += 1
          else:
              d[elem] = 1
    for key in d:
        if d[key] == len(l):
            out_list.append(key)

    print(out_list)

gemeinsame_elemente([[11, 2, 3, 4],[4, 5, 2, 11],[7, 8, 2, 5, 11, 4]])
