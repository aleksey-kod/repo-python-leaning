prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print("id изначального списка",id(prices))
for char in prices:
    temp=str(char/1).split(".")
    print("{} руб {:0^2} коп".format(temp[0],temp[1]),end=', ')
prices.sort()
print()
print("id списка отсортированного по возрастанию ",id(prices))
for idx in range(len(prices)):
    temp=str(prices[idx]/1).split(".")
    print("{} руб {:0^2} коп".format(temp[0],temp[1]),end=', ')
new_prices=sorted(prices,reverse=True);
print()
print("id списка отсортированного по убыванию ",id(new_prices))
for idx in range(len(new_prices)):
    temp=str(new_prices[idx]/1).split(".")
    print("{} руб {:0^2} коп".format(temp[0],temp[1]),end=', ')
print()
for char in new_prices[:5]:
    temp = str(char / 1).split(".")
    print("{} руб {:0^2} коп".format(temp[0], temp[1]), end=', ')

