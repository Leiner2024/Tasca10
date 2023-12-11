def gran_lista(l):
    #Te da None si la lista está vacía
    if not l:
        return None
    max = l[0]
    for n in l:
        if n > max:
            max = n
    return max

l = [3, 4, 2, 3, 10]
r = gran_lista(l)
print(r)