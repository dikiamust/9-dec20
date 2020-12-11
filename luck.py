# 1ST LESSON
print( 'hello world!!!' )
import requests

r = requests.get( 'https://google.com' )
print( r.status_code )
if r.status_code == 200:
    print( r.text )

# SEQUENTIAL = EKSEKUSI BERURUTAN
print( 'print adalah perintah menulis kata2/ string' )
print( '---' * 4 )

# PERCABANGAN : eksekusi terpilih / perintah untuk memilih beberapa pilihan
ingin_cepat = False
if ingin_cepat:
    print( 'jalan lurus' )
else:
    print( 'jalan lain/belok' )

# PERULANGAN

jumlah_anak = 10

for index_anak in range( 1, jumlah_anak + 1 ):
    print( f'Hallo anak #{index_anak}' )

# TIPE DATA SEDERHANA
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'catur'

print( anak1 )
print( anak2 )
print( anak3 )
print( anak4 )

#TIPE DATA LIST/ DAFTAR / ARRAY
anak = ['eko','dwi','tri','catur']
print(anak)

#APPEND ADALAH PERINTAH UNTUK MENAMBAHKAN PADA DAFTAR
anak.append('limo')
print(anak)

#SAPA ANAK KE3
print(f'Hai {anak[2]}!')

#sapa anak 1-5 (eko,dwi,tri,catur,limo)
for a in anak:
    print( f"Hai {a}!" )

#SAPA SEMUA ANAK CARA RIBET
for a in range (0, len(anak)):
    print(f'Hai {anak[a]}!')

#SPA SEMUA ANAK CARA RIBET MEMAKAI URUTAN NOMOR
for a in range (0, len(anak)) :
    print(f'{a+1}.Hai {anak[a]}!')



