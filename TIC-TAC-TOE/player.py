import random

class Oyuncu:
    def __init__(self, harf):
        self.harf = harf

    def hamle_al(self, oyun):
        pass

class RastgeleBilgisayarOyuncu(Oyuncu):
    def __init__(self, harf):
        super().__init__(harf)

    def hamle_al(self, oyun):
        kare = random.choice(oyun.uygun_hamleler())
        return kare

class InsanOyuncu(Oyuncu):
    def __init__(self, harf):
        super().__init__(harf)

    def hamle_al(self, oyun):
        gecerli_kare = False
        deger = None
        while not gecerli_kare:
            kare = input(self.harf + '\'in sırası. Hamlenizi girin (0-9):')
            try:
                deger = int(kare)
                if deger not in oyun.uygun_hamleler():
                    raise ValueError
                gecerli_kare = True 
            except ValueError:
                print('Geçersiz Hamle! Tekrar deneyin.')
        return deger
