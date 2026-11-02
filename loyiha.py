class Oquvchi:
    soni = 0

    def __init__(self, ism):
        self.ism = ism
        self.baholar = {}
        Oquvchi.soni += 1

    @staticmethod
    def baho_togrimi(baho):
        return isinstance(baho, int) and 1 <= baho <= 5

    @classmethod
    def qatordan(cls, qator):
        ism, baholar = qator.strip().split(";")
        oquvchi = cls(ism)
        for juft in baholar.split(","):
            if juft:
                fan, baho = juft.split(":")
                oquvchi.baholar[fan] = int(baho)
        return oquvchi

    @classmethod
    def umumiy_soni(cls):
        return cls.soni

    def baho_qoshish(self, fan, baho):
        if not self.baho_togrimi(baho):
            return f"{self.ism} - {baho} noto'g'ri baho"
        self.baholar[fan] = baho
        return f"{self.ism} - {fan} fanidan {baho} baho oldi"

    def ortacha_baho(self):
        if not self.baholar:
            return 0
        return sum(self.baholar.values()) / len(self.baholar)

    def qatorga(self):
        juftlar = ",".join(f"{fan}:{baho}" for fan, baho in self.baholar.items())
        return f"{self.ism};{juftlar}"

    def holat(self):
        if self.ortacha_baho() >= 4.5:
            return f"{self.ism} - a'lochi"
        if self.ortacha_baho() >= 3.5:
            return f"{self.ism} - yaxshi o'qiydi"
        return f"{self.ism} - ko'proq harakat qilishi kerak"


class Sinf:
    def __init__(self, nomi, fayl):
        self.nomi = nomi
        self.fayl = fayl
        self.oquvchilar = []

    @classmethod
    def fayldan_yuklash(cls, nomi, fayl):
        sinf = cls(nomi, fayl)
        try:
            with open(fayl, "r") as f:
                for qator in f:
                    if qator.strip():
                        sinf.oquvchilar.append(Oquvchi.qatordan(qator))
        except FileNotFoundError:
            pass
        return sinf

    def oquvchi_qoshish(self, oquvchi):
        self.oquvchilar.append(oquvchi)
        return f"{self.nomi} - {oquvchi.ism} qo'shildi"

    def faylga_saqlash(self):
        with open(self.fayl, "w") as f:
            for oquvchi in self.oquvchilar:
                f.write(oquvchi.qatorga() + "\n")
        return f"{self.nomi} - {len(self.oquvchilar)} ta o'quvchi faylga saqlandi"

    def eng_yaxshi(self):
        if not self.oquvchilar:
            return f"{self.nomi} - o'quvchilar yo'q"
        eng = max(self.oquvchilar, key=lambda o: o.ortacha_baho())
        return f"{self.nomi} - eng yaxshi o'quvchi {eng.ism} ({eng.ortacha_baho():.2f})"

    def natijalar(self):
        natija = ""
        for son, oquvchi in enumerate(self.oquvchilar, 1):
            natija += f"{son}. {oquvchi.ism} - {oquvchi.ortacha_baho():.2f}\n"
        return natija.rstrip()


oquvchi1 = Oquvchi("Ali")
oquvchi2 = Oquvchi("Vali")
sinf = Sinf("10-A sinf", "oquvchilar.txt")

print(f"======== {oquvchi1.ism} ========\n" \
      f"{oquvchi1.baho_qoshish('Matematika', 5)}\n" \
      f"{oquvchi1.baho_qoshish('Python', 5)}\n" \
      f"{oquvchi1.baho_qoshish('Fizika', 4)}\n" \
      f"{oquvchi1.baho_qoshish('Kimyo', 7)}\n" \
      f"{oquvchi1.holat()}")

print(f"======== {oquvchi2.ism} ========\n" \
      f"{oquvchi2.baho_qoshish('Matematika', 3)}\n" \
      f"{oquvchi2.baho_qoshish('Python', 4)}\n" \
      f"{oquvchi2.baho_qoshish('Fizika', 3)}\n" \
      f"{oquvchi2.holat()}")

print(f"======== {sinf.nomi} ========\n" \
      f"{sinf.oquvchi_qoshish(oquvchi1)}\n" \
      f"{sinf.oquvchi_qoshish(oquvchi2)}\n" \
      f"{sinf.faylga_saqlash()}\n" \
      f"Jami o'quvchilar: {Oquvchi.umumiy_soni()}\n" \
      f"{sinf.eng_yaxshi()}")

print(f"======== Fayldan yuklangan sinf ========\n" \
      f"{Sinf.fayldan_yuklash('10-A sinf', 'oquvchilar.txt').natijalar()}\n" \
      f"{Sinf.fayldan_yuklash('10-A sinf', 'oquvchilar.txt').eng_yaxshi()}")