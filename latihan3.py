# import library
import time
import datetime
#import nama user
nama = input('hallo.. nama saya Mr.kompie, nama anda siapa?')
#tampilkan nama user
print('oh nama anda', nama, 'nama yang bagus sekali.')
#kasih jeda 3 detik
time.sleep(3)
#input tahun lahir
thnLahir = int(input('btw...'+ nama + ' kamu lahir tahun berapa?'))
#jeda 3 detik
time.sleep(3)
#hitung usia user
skrg = datetime.datetime.now()
usia = skrg.year - thnLahir
#tampilkan usia
print('hmmm...',nama,'kamu sudah',usia,'tahun ya..')
#kasih jeda 3 detik
time.sleep(3)
#tampilkam pesan sesuai range usia
if (usia > 50):
    print("Anda sudah cukup tua ya?")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
else:
    print("Oalah.. Anda masih anak-anak toh?")
    print("Jangan suka merengek-rengek minta jajan ya!!")
#kasih jeda 3 detik
time.sleep(3)
#say goodbye
print('ok.. see you later', nama,'..senang berkenalan denganmu')