# def get_list_nums(ml):
#     numbers = []
#     ml_2 = ml[:]  
    
#     while ml_2:
#         item = ml_2.pop()  
        
#         if isinstance(item, list):   
#             ml_2.extend(item)
#         elif isinstance(item, int):
#             numbers.append(item)
    
#     return numbers



# ml = [1,2,[3,4,[4,5],16,[17,2,[1]],25]]

# print(sum(get_list_nums(ml)))


# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}


# for k, v in d2.items():  
#     if k not in d1:
#         d1.setdefault(k,v)
#     else:
#         for k,v  in d1.items():
#             d1[k] += v
# print(d1)

# def get_list_items(ml):
#     a = int("".join([str(i) for i in ml]))
#     return str(a)    

        
# ml = [24, 15, 16]

# print(get_list_items(ml))

# ml = [10,20,30,0,50,60]

# for el in ml:
#     try:
#         print(120/el)
#     except ZeroDivisionError:
#         print('cant') 
# print('finish')                 
# 

# filename = input('Enter the file name: ')


# with open(filename, 'r') as file:
#     f = file.readlines()

# for el in f:
#     try:
#         print(int(el)**2)
#     except ValueError:
#         print("Element is not digit")


# def get_content(filename):
#     try:
#         with open (filename) as f:
#             return f.readlines()
#     except FileNotFoundError:
#         print("pleas provide a file")
#         exit()

# def print_square(data):
#     for el in data:
#         tmp = el.replace("\n","")
#         try:
#             print(int(tmp)**2)
#         except ValueError:
#             pass
# def main():
#     fname = input()
#     cnt = get_content(fname)
#     print_square(cnt)


# main()

# import argparse

# # Ստեղծում ենք պարսիչ (parser)
# parser = argparse.ArgumentParser(description="argparse գրադարանի օրինակ")

# # Ավելացնում ենք արգումենտներ
# parser.add_argument('--name', type=str, help='Ձեր անունը', required=True)
# parser.add_argument('--age', type=int, help='Ձեր տարիքը', default=18)

# # Վերլուծում ենք արգումենտները
# args = parser.parse_args()

# # Օգտագործում ենք արգումենտները
# print(f"Բարև, {args.name}! Ձեր տարիքը՝ {args.age}.")

# def rupper(mstr):
#     if len(mstr) == 0: 
#         return mstr
    
#     return mstr[0].upper() + rupper(mstr[1:])  

# mstr = "asaassadas"
# print(rupper(mstr))

# def rreverse(mstr):
#     if not mstr:
#         return ""
#     return mstr[-1] + rreverse(mstr[:-1])    

# mstr="aaaaabbbb"    

# print(rreverse(mstr))

# def rec(mstr):
#     mstr = str(mstr)
#     if not mstr:
#         return 0
#     return int(mstr[0]) + rec(mstr[1:])

# mstr = 121    

# print(rec(mstr)) 

def let_count(mstr):
    a = {}
    for i in mstr:
        if i.isalpha():
            if i in a:
                a[i] += 1 
            else:
                a[i] = 1  
   
    ml = list(a.items())
    ml.sort(key=lambda x : x[1])

    return ml[0], ml[-1]
mstr = "sasdasff"

print(let_count(mstr))

