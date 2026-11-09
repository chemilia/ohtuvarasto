
"""Varaston tilavuutta ja saldoa hallinnoiva moduuli."""


class Varasto:
    """Luokka, joka kuvaa varastoa."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Alustaa varaston tilavuuden ja alkusaldon."""
        self.tilavuus = max(0.0, tilavuus)
        self.saldo = min(max(0.0, alku_saldo), self.tilavuus)

    def paljonko_mahtuu(self):
        """Palauttaa varastossa olevan vapaan tilan."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon annettu määrä, enintään täyteen asti."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa varastosta pyydetyn määrän ja palauttaa otetun määrän."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        """Palauttaa varaston saldon ja vapaan tilan merkkijonona."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
