hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}
hari_kedua.add("keju")
barang_sama = hari_pertama.intersection(hari_kedua)
print("c. Barang yang sama:",barang_sama)
hanya_hari_pertama = hari_pertama.difference(hari_kedua)
print("d. Hanya dibeli hari pertama:", hanya_hari_pertama)
hari_pertama.remove("garam")
hanya_hari_kedua = hari_kedua.difference(hari_pertama)
print("f. Hanya dibeli hari kedua:", hanya_hari_kedua)
barang_tidak_sama = hari_pertama.symmetric_difference(hari_kedua)
print("g. Barang yang tidak sama"), (barang_tidak_sama)
print("h. Semua pembelian hari pertama:", hari_pertama)
print("i. Semua pembelian hari kedua:", hari_kedua)