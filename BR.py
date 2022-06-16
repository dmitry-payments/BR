from tkinter.messagebox import NO

def split(str, idx):
    return (str[:idx], str[idx:])

#xxx(xxx)[
#(()((](())]{
#xx(xxx)(xxxx)

def find(str):
    idx = [str.find(x) for x in ["(", "{", "["]] #составили массив индексов скобок
    idx = [x for x in idx if x > 0] #убрали из массива значения меньше 0 (потому что find возвращает -1 если не нашел строку)
    if len(idx) == 0:
        return str
    mini = min(idx)
    h, t = split(str, mini)
    res = recurison_find(t)
    #здесь нужно анализировать если еще есть хвост (while) - это не реализовано
    if check_invalid_res(res):
        return h
    if not t.startswith(res):
        return max(h, res)
    return h+res

br_map = {"(": ")", "{": "}", "[": "]"}

def incorrect_close_brackets(open_br):
    res = {v for k, v in br_map.items() if k != open_br}
    return res

def check_invalid_res(str):
    return str is None or len(str) == 0

def recurison_find(str):
    if len(str) == 0:
        return None
    obr = str[0] 
    icb = incorrect_close_brackets(obr)
    for i in range(1, len(str)):
        if str[i] in icb: #нашпи неправильно закрывающуюся скобку
            return str[1:i]
        if str[i] == br_map[obr]:
            return str[:i+1]
        if str[i] in br_map:
            h,t = split(str, i)
            res = recurison_find(t)
            if check_invalid_res(res):
                return str[1:i]
            if not str.startswith(res):
                return res          
    return str[1:]

test = [
    "xxx(xxx)["
]

for x in test:
    print(find(x))
