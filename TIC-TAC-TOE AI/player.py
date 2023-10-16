import random
import math

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

class DahiBilgisayarOyuncu(Oyuncu):
    def __init__(self, harf):
        super().__init__(harf)

    def hamle_al(self, oyun):
        if len(oyun.uygun_hamleler()) == 9:
            kare = random.choice(oyun.uygun_hamleler())
        else:
            kare = self.minimax(oyun, self.harf)['konum']
        return kare

    def minimax(self, durum, oyuncu):
        max_oyuncu = self.harf
        diger_oyuncu = 'O' if oyuncu == 'X' else 'X'

        # Terminal durumu kontrolü
        if durum.mevcut_kazanan == diger_oyuncu:
            return {'konum': None, 'puan': 1 * (durum.bos_kare_sayisi() + 1) if diger_oyuncu == max_oyuncu else -1 * (durum.bos_kare_sayisi() + 1)}
        elif not durum.bos_kareler():
            return {'konum': None, 'puan': 0}

        if oyuncu == max_oyuncu:
            en_iyi = {'konum': None, 'puan': -math.inf}
        else:
            en_iyi = {'konum': None, 'puan': math.inf}

        for muhtemel_hamle in durum.uygun_hamleler():
            durum.hamleyi_yap(muhtemel_hamle, oyuncu)
            sim_puan = self.minimax(durum, diger_oyuncu)
            durum.tahta[muhtemel_hamle] = ' '
            durum.mevcut_kazanan = None
            sim_puan['konum'] = muhtemel_hamle

            if oyuncu == max_oyuncu:
                if sim_puan['puan'] > en_iyi['puan']:
                    en_iyi = sim_puan
            else:
                if sim_puan['puan'] < en_iyi['puan']:
                    en_iyi = sim_puan

        return en_iyi
