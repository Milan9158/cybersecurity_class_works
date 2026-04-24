def check_weight(w):
    if w > 15:
        k=w-15
        return f"Exceeds ! ! you need to remove {k} kg "
    else :
        r=15-w
        return f"You can add {r} kg more"
w=float(input("enter the weight: "))
print(check_weight(w))