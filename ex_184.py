lst_in = input().split()

def get_int(x):
    try:
        return int(x)
    except:
        return None

print(sum(list(map(int, filter(get_int, lst_in)))))