
"""Esimerkkiohjelma varaston käyttämiseen."""

from varasto import Varasto


def main():
    """Luo varastot ja kokeilee niiden käyttöä."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    olutta.lisaa_varastoon(1000.0)

    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
