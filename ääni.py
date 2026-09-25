import ctypes
def toista_ääni(taajuus, kesto):
    ctypes.windll.kernel32.Beep(taajuus, kesto)