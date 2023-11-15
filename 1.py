def find(target, source):
    for i in range(len(target) - len(source) + 1):
        cnt = 0
        idx = i
        for j in range(len(source)):
            if target[idx] == source[j]:
                cnt += 1
            idx += 1

        if cnt == len(source):
            return i

    return -1

def find_better(target, source):
    for i in range(len(target) - len(source) + 1):
        if target[i:i+len(source)] == source:
            return i

    return -1

def find_evenbetter(target, source):
    position = -1
    j = 0 #for source

    for i in range(len(target)):
        if target[i] != source[j]:
            position = -1
            j = 0
        if target[i] == source[j]:
           if j == 0:
            position = i

        if j >= len(source) - 1:
            break
        else:
            j +=1

    return position

def find_sum(numbers, sum):
    for i in range(len(numbers) - 1):
        if sum-i in numbers:
            return i, sum - i

    return None


def generate_multiple(number, count):
    multi = [number]

    i = 2
    while i <= count:
        multi.append(number*i)
        i += 1

    return multi

def big_sum(a, b):
    s = 0
    p = 1
    t = 0
    for ind in range(len(a)-1, -1, -1):
      cif1 = int(a[ind])
      cif2 = int(b[ind])
      nr = (cif1 + cif2 + t) % 10
      t = 0
      if cif1 + cif2 > 9:
          t = 1

      s = nr * p + s
      p *= 10
    return str(s)


def test_big_sum():
    assert big_sum('123', '123') == '246'
    assert big_sum('123', '129') == '252'
    assert big_sum('99', '101') == '1100'


def test_generate_multiple():
    assert generate_multiple(3, 4) == [3, 6, 9, 12]
    assert generate_multiple(2, 2) == [2, 4]


def test_find_sum():
    assert find_sum([1, 2, 9], 3) == (1, 2)
    assert find_sum([1, 2, 9], 12) == None

def test_find_2():
    assert find('string', 'ing') == 3
    assert find('stiring', 'ing') == 4

def test_find_3():
    assert find('string', 'ing') == 3
    assert find('stiring', 'ing') == 4

def main():
    pass

test_find_sum()
test_big_sum()
test_find_2()
test_find_3()
test_generate_multiple()
main()

