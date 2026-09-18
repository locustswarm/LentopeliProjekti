import ctypes
taajuus = 200
kesto = 500
for i in range(4):
    ctypes.windll.kernel32.Beep(taajuus, kesto)