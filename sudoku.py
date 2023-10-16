from pprint import pprint

def sonraki_bos_hucre(bulmaca):
    for satir in range(9):
        for sutun in range(9):
            if bulmaca[satir][sutun] == -1:
                return satir, sutun
    return None, None

def gecerli_mi(bulmaca, tahmin, satir, sutun):
    satir_degerleri = bulmaca[satir]
    if tahmin in satir_degerleri:
        return False

    sutun_degerleri = [bulmaca[i][sutun] for i in range(9)]
    if tahmin in sutun_degerleri:
        return False

    satir_baslangic = (satir // 3) * 3
    sutun_baslangic = (sutun // 3) * 3

    for s in range(satir_baslangic, satir_baslangic + 3):
        for k in range(sutun_baslangic, sutun_baslangic + 3):
            if bulmaca[s][k] == tahmin:
                return False

    return True

def sudoku_coz(bulmaca):
    satir, sutun = sonraki_bos_hucre(bulmaca)

    if satir is None:
        return True

    for tahmin in range(1, 10):
        if gecerli_mi(bulmaca, tahmin, satir, sutun):
            bulmaca[satir][sutun] = tahmin

            if sudoku_coz(bulmaca):
                return True

            bulmaca[satir][sutun] = -1

    return False

if __name__ == '__main__':
    ornek_bulmaca = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(sudoku_coz(ornek_bulmaca))
    pprint(ornek_bulmaca)
