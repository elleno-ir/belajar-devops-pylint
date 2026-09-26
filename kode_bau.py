"""Modul sederhana untuk menghitung penjumlahan dua angka."""


def hitung_penjumlahan(angka1, angka2):
    """Menghitung hasil penjumlahan dua angka.

    Args:
        angka1 (int): Angka pertama.
        angka2 (int): Angka kedua.

    Returns:
        int: Hasil penjumlahan angka1 dan angka2.
    """
    return angka1 + angka2


def main():
    """Fungsi utama program."""
    hasil = hitung_penjumlahan(10, 20)
    print(f"Hasil penjumlahan: {hasil}")


if __name__ == "__main__":
    main()