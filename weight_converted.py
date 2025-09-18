weight = input("Weight: ")
select = input("(L)bs or (K)g: ")
if select == "L" or select =="l":
    converted = float(weight) * 0.45
    print(f"You are {converted} kilos.")
elif select.upper() == "K":
    converted = float(weight) / 0.45
    print(f"You are {converted} pounds.")