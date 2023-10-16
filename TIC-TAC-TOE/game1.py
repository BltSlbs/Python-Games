from player import InsanOyuncu, RastgeleBilgisayarOyuncu

class XOXOyunu:
    def __init__(self):
        self.tahta = [' ' for _ in range(9)]
        self.mevcut_kazanan = None

    def tahtayi_yazdir(self):
        for satir in [self.tahta[i*3:(i+1)*3] for i in range (3)]:
            print('| ' + ' | '.join(satir) + ' |')

    @staticmethod
    def tahta_numaralariyla_yazdir():
        numarali_tahta = [[str(i) for i in range (j*3, (j+1)*3)] for j in range (3)]
        for satir in numarali_tahta:
            print('| ' + ' | '.join(satir) + ' |')

    def uygun_hamleler(self):
        return [i for i, yer in enumerate(self.tahta) if yer == ' ']
    
    def bos_kareler(self):
        return ' ' in self.tahta
    
    def bos_kare_sayisi(self):
        return self.tahta.count(' ')
    
    def hamleyi_yap(self, kare, harf):
        if self.tahta[kare] == ' ':
            self.tahta[kare] = harf
            if self.kazanan(kare, harf):
                self.mevcut_kazanan = harf 
            return True
        return False
    
    def kazanan(self, kare, harf):
        satir_index = kare // 3
        satir = self.tahta[satir_index*3 : (satir_index + 1)* 3]
        if all([yer == harf for yer in satir]):
            return True
        
        sutun_index = kare % 3
        sutun = [self.tahta[sutun_index+i*3] for i in range(3)]
        if all ([yer == harf for yer in sutun]):
            return True
        

        if kare %2 == 0:
            capraz1 = [self.tahta[i] for i in [0, 4, 8]]
            if all([yer == harf for yer in capraz1]):
                return True
            capraz2 = [self.tahta[i] for i in [2, 4, 6]]
            if all([yer == harf for yer in capraz2]):
                return True
            
        return False

def oyna(oyun, x_oyuncu, o_oyuncu, oyunu_yazdir=True):
    if oyunu_yazdir:
        oyun.tahta_numaralariyla_yazdir()

    harf = 'X'

    while oyun.bos_kareler():
        if harf == 'O':
            kare = o_oyuncu.hamle_al(oyun)
        else:
            kare = x_oyuncu.hamle_al(oyun)

        if oyun.hamleyi_yap(kare, harf):
            if oyunu_yazdir:
                print(f'{harf} {kare} numaralı kareye hamle yaptı.')
                oyun.tahtayi_yazdir()
                print('')

            if oyun.mevcut_kazanan:
                if oyunu_yazdir:
                    print(harf + ' kazandı!')
                return harf

            harf = 'O' if harf == 'X' else 'X'

    if oyunu_yazdir:
        print('Oyun berabere!')

if __name__ == '__main__':
    x_oyuncu = InsanOyuncu('X')  
    o_oyuncu = RastgeleBilgisayarOyuncu('O')
    t = XOXOyunu()
    oyna(t, x_oyuncu, o_oyuncu, oyunu_yazdir=True)
