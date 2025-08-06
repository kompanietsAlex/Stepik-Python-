lst_in = input().split()

def get_int(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

lst_out = list(map(get_int, lst_in))
print(lst_out)