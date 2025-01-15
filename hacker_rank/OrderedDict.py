from collections import OrderedDict

def prnt_ordered_item_net_price():
    no_item = int(input())
    o_dict = OrderedDict()#Instead of OrderedDict, use a regular dictionary (item_prices), which keeps order in Python 3.7+.
    for _ in range(no_item):
        *name, price = input().split()
        name = " ".join(name)
        price = int(price)
        o_dict[name] = o_dict.get(name, 0)+price
    for k,v in o_dict.items():
        print(f"{k} {v}")
if __name__ == "__main__":
    prnt_ordered_item_net_price()