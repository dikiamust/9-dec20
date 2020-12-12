# TIPE DATA DICTIONARY = PERINTAH MENGHUBUNGKAN ANTARA KEY DAN VALUE / KEY VALUE PAIR /KVP

kamus = {}
kamus['anak'] = 'son'
kamus['ayah'] = 'father'
kamus['ibu'] = 'mother'
kamus['istri'] = 'wife'
kamus['suami'] = 'husband'
print( kamus['anak'] )
print( kamus['ibu'] )

# STUDY CASE DATA DRIVER YANG BERADA DI SEKITAR (DATA DARI SERVER)
data_dari_server_gojek = {
    'tanggal': '2020-12-11',
    'driver_list': ['eko', 'dwi', 'tri', 'catur','limo']
}
print(data_dari_server_gojek)
print(f" driver kedua {data_dari_server_gojek['driver_list'][1]}")

# STUDY CASE SEDIKIT KOMPLEKS
data_dari_server_gokar = {
    'gokar_list': [
    {'nama': 'eko','jarak': 10},
    {'nama' : 'dwi', 'jarak' : 20},
    {'nama' : 'tri', 'jarak' : 30},
    {'nama' : 'catur', 'jarak' : 40},
    {'nama' : 'limo', 'jarak' : 50}
]
}
print('berikut adalah data gokar :')
print(f" gokar ke-4 {data_dari_server_gokar ['gokar_list'] [3]}")
print(f" gokar ke-5 {data_dari_server_gokar ['gokar_list'] [4]}")