def kira_kuboid(a, b, c):
    isipadu = a * b * c
    return isipadu

def cetak_kuboid():
    x = float(input("Masukkan panjang kuboid: "))
    y = float(input("Masukkan lebar kuboid: "))
    z = float(input("Masukkan tinggi kuboid: "))
    isipadu_kuboid = float(kira_kuboid(x, y, z))
    print(f"Isipadu kuboid = {isipadu_kuboid:.2f}")

if __name__ == "__main__":
    cetak_kuboid()