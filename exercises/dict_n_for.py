type_str = "my_string"
type_lst = [1, 2, 3, 4, 5, "six"]
type_dct = dict(k=1, k2=2, k3=3, k4=4)
type_tpl = ("a", "b", "c", 100)
type_lst_tpl = [("k", 1), ("k2", 2), ("k3", 3), ("k4", 4)]

print('str iter ------------------------')
for ch in type_str:
    print(ch)
print('lst iter ------------------------')
for item in type_lst:
    print(item)
print('tpl iter ------------------------')
for item in type_tpl:
    print(item)
print('dct iter ------------------------')
for key in type_dct:
    print(key)
print('dct iter val ------------------------')
for val in type_dct.values():
    print(val)
print('dct iter kv  ------------------------')
for k, v in type_dct.items():
    print(k, v)
print('lst_tpl iter ------------------------')
for v1, v2 in type_lst_tpl:
    print(v1, v2)

dct = {
    "products": {
        "furniture": {
            "chair": {
                "size": "100x20"
            }
        },
        "clothes": {
            "jacket": {
                "size": "xxl"
            }
        },
        "food": {
            "tacos": {
                "spicy": True and True and True
            }
        }
    }
}

chair_size = dct["products"]["furniture"]["chair"]["size"]
is_taco_spicy = dct["products"]["food"]["tacos"]["spicy"]

del dct["products"]["food"]

print(chair_size)
print(is_taco_spicy)
