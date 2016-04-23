# Ввести список и вывести второй максимум этого списка, т. е. элемент a∈S : ∃ b∈S : b>a и a⩾c ∀c∈S, c≠b.
# Если второго максимума нет, вывести NO.
lst = []
while str != '':
    str = input()
    if str == '':
        break
    lst.append(str)
lst.sort()
print(lst)
if lst[-2].isdigit():
    print(lst[-2])
else:
    print("No")
