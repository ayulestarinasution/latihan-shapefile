# Nama : Ayu Lestari Nasution
#NPM : 1194007
# Kelas: D4 TEKNIK INFORMATIKA - 3A
# 1194007 MOD 8 = 7 jadi gambar segitiga siku-siku

import shapefile

w = shapefile.Writer('soal10')
w.shapeType

w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("coba1", "satu")
w.record("coba2", "dua")
w.record("coba3", "tiga")
w.record("coba4", "empat")
w.record("coba5", "lima")
w.record("coba6", "enam")
w.record("coba7", "tujuh")
w.record("coba8", "nalan")

w.poly([[[5, 2], [3, 2], [5, 4]]])
w.poly([[[2, 1], [2, 5], [2, 12]]])
w.poly([[[8, 1], [11, 1], [8, 5]]])
w.poly([[[2, 14], [5, 14], [2, 18]]])
w.poly([[[19, 1], [17, 1], [19, 5]]])
w.poly([[[2, 8], [5, 8], [2, 12]]])
w.poly([[[8, 8], [11, 8], [8, 12]]])
w.poly([[[19, 8], [17, 8], [19, 12]]])
