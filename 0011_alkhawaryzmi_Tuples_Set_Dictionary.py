harga_buah={
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
harga= harga_buah.values()
total =0
for buah, harga in harga_buah.items():
    print(f'harga {buah}: Rp{harga}')
    total += harga
print(f'Total harga buah: Rp{total}')