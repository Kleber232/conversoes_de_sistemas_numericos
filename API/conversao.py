import ctypes
import os

# Caminho absoluto para a DLL
DLL_PATH = os.path.join(os.path.dirname(__file__), '..', 'func', 'conversao.dll')
conversao = ctypes.CDLL(DLL_PATH)

# 1. char* decbin_part_frac(float);
conversao.decbin_part_frac.argtypes = [ctypes.c_float]
conversao.decbin_part_frac.restype = ctypes.c_char_p

# 2. char* dec_bin(int);
conversao.dec_bin.argtypes = [ctypes.c_int]
conversao.dec_bin.restype = ctypes.c_char_p

# 3. int parteint(const int*, int);
conversao.parteint.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
conversao.parteint.restype = ctypes.c_int

# 4. float partfrac(const int*, int);
conversao.partfrac.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
conversao.partfrac.restype = ctypes.c_float

# 5. float ler_binario(const int*, int, const int*, int);
conversao.ler_binario.argtypes = [
    ctypes.POINTER(ctypes.c_int), ctypes.c_int,
    ctypes.POINTER(ctypes.c_int), ctypes.c_int
]
conversao.ler_binario.restype = ctypes.c_float

# 6. float adicaobin(const int*, int, const int*, int, const int*, int, const int*, int);
conversao.adicaobin.argtypes = [
    ctypes.POINTER(ctypes.c_int), ctypes.c_int,
    ctypes.POINTER(ctypes.c_int), ctypes.c_int,
    ctypes.POINTER(ctypes.c_int), ctypes.c_int,
    ctypes.POINTER(ctypes.c_int), ctypes.c_int
]
conversao.adicaobin.restype = ctypes.c_float

# 7. float subtracaobin(...)
conversao.subtracaobin.argtypes = conversao.adicaobin.argtypes
conversao.subtracaobin.restype = ctypes.c_float

# 8. float multibin(...)
conversao.multibin.argtypes = conversao.adicaobin.argtypes
conversao.multibin.restype = ctypes.c_float

# 9. float divbin(...)
conversao.divbin.argtypes = conversao.adicaobin.argtypes
conversao.divbin.restype = ctypes.c_float

# 10. int DecimalOctal(int);
conversao.DecimalOctal.argtypes = [ctypes.c_int]
conversao.DecimalOctal.restype = ctypes.c_int

# 11. int OctalDecimal(int);
conversao.OctalDecimal.argtypes = [ctypes.c_int]
conversao.OctalDecimal.restype = ctypes.c_int

# 12. int OctalBinario(int);
conversao.OctalBinario.argtypes = [ctypes.c_int]
conversao.OctalBinario.restype = ctypes.c_int

# Exemplo de uso:
if __name__ == "__main__":
    print(conversao.dec_bin(10).decode())  # Exemplo: binário de 10