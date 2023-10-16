import random
def  bilgisayar_tahmini(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low 
        feedback = input(f'Tahmin {guess} çok yüksek (H), çok düşük (L), veya doğru (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'OHAAAA BİLGİSAYAR DOĞRU BİLDİ, {guess}, DOĞRUYDU!')

bilgisayar_tahmini(10)