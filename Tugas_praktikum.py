class persegi_panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

pp = persegi_panjang (53 , 20)

persegi_panjang = persegi_panjang(pp.panjang, pp.lebar)
print(f"\nLuas: {persegi_panjang.luas()}")
print(f"Keliling: {persegi_panjang.keliling()}")

print(f"\nPanjang dari persegi panjang =",pp.panjang)
print(f"Lebar dari persegi panjang =",pp.lebar)
