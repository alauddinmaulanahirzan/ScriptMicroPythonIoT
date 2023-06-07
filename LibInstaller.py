import network
import mip

SSID = "Free Wifi USM 1"
Password = ""
reset = True

print(">> Memulai Installer Libs ESP8266 ... ")
print(">> Menghubungkan ... ")
wlan0 = network.WLAN(network.STA_IF)
if reset:
    wlan0.active(True)
        
    # Masukkan SSID dan Password
    wlan0.connect(SSID, Password)
        
    while not wlan0.isconnected():
        wlan0.active(True)
        pass

status = wlan0.isconnected()

if(status == True):
    print("==>> Terhubung")
    print(">> Mengecek Libs urequests ...")
    try:
        import urequests
        print("==>> OK")
    except:
        print("==>> Gagal. Menginstall Libs ... ")
        mip.install('urequests')
        
    print(">> Mengecek Libs umqtt.robust ...")
    try:
        import umqtt.robust
        print("==>> OK")
    except:
        print("==>> Gagal. Menginstall Libs ... ")
        mip.install("umqtt.robust")
        
    print(">> Mengecek Libs umqtt.simple ...")
    try:
        import umqtt.simple
        print("==>> OK")
    except:
        print("==>> Gagal. Menginstall Libs ... ")
        mip.install("umqtt.simple")
    print(">> Mengecek Libs ssd1306 ...")
    try:
        import ssd1306
        print("==>> OK")
    except:
        print("==>> Gagal. Menginstall Libs ... ")
        mip.install("ssd1306")
else:
    print("==>> Koneksi Gagal")
