
has_sollved_map = {}

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n in has_sollved_map.keys():
        return has_sollved_map[n]
    ret = f(n-1)+f(n-2)
    has_sollved_map[n] = ret
    return ret