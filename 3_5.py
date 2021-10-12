
from random import choice,randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью","вечерело"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count,duble=False):
    ans=[]
    if duble == True:
        n = nouns.copy()
        adv = adverbs.copy()
        adj = adjectives.copy()
        while (count > 0  and n !=[] and adv!=[] and adj!=[]):
            rand_n = randrange(len(n))
            rand_adv = randrange(len(adv))
            rand_adj = randrange(len(adj))
            ans.append(n.pop(rand_n)+" "+adv.pop(rand_adv)+" "+adj.pop(rand_adj))
            count -= 1
        return ans
    for i in range(count):
        ans.append(choice(nouns)+" "+choice(adverbs)+" "+choice(adjectives))
    return ans
print(get_jokes(10))
print(get_jokes(10,True))

