import random

def guess(x):
    rastgele_sayi = random.randint(1, x)
    guess = 0
    while guess != rastgele_sayi:
        guess = int(input(f'1 - {x} arasında bir sayı tahmin et.: '))
        if guess < rastgele_sayi:
            print('HAHAHA EZİK TEKRAR TAHMİN ET. TAHMİN ETTİĞİN SAYI DÜŞÜK')
        elif guess > rastgele_sayi:
            print('HAHAHA EZİK TEKRAR TAHMİN ET. TAHMİN ETTİĞİN SAYI YÜKSEK')

    print(f'OHA BİLDİN ŞAŞIRDIM AÇIKÇASI {rastgele_sayi} DOĞRU TAHMİN')

guess(999)