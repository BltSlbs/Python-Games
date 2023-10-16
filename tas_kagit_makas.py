import random

def kazanan(oyuncu, rakip):
    if(oyuncu == 't' and rakip =='m') or (oyuncu == 'm' and rakip == 'k') \
        or (oyuncu == 'k' and rakip == 't'):
        return True
    else:  
        return False
def play():
    oyuncu = input("Seçimini Yap: Taş için 't', Kağıt için 'k', Makas için 'm'\n")
    bilgisayar = random.choice(['t', 'k', 'm'])

    if  oyuncu == bilgisayar:
        return 'Berabere'
    if kazanan(oyuncu, bilgisayar):
        return 'Kazandın!'
    return 'Kaybettin!'
print(play())