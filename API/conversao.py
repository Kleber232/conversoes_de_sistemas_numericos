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

__all__ = ["decbin_part_frac", 
           "dec_bin", 
           "parteint",
           "partfrac",
           "ler_binario",
           "adicaobin",
           "subtracaobin",
           "multibin",
           "divbin",
           "DecimalOctal",
           "OctalDecimal",
           "OctalBinario"
           ]

def decbin_part_frac(num: float) -> str:
    return conversao.decbin_part_frac(ctypes.c_float(num)).decode()

def dec_bin(num: int) -> str:
    return conversao.dec_bin(ctypes.c_int(num)).decode()

def parteint(bits: list[int]) -> float:
    arr = (ctypes.c_int * len(bits))(*bits)
    return conversao.parteint(arr, len(bits))

def partfrac(bits: list[int]) -> float:
    arr = (ctypes.c_int * len(bits))(*bits)
    return conversao.partfrac(arr, len(bits))

def ler_binario(parte_int: list[int], parte_frac: list[int]):
    arr_int = (ctypes.c_int * len(parte_int))(*parte_int)
    arr_frac = (ctypes.c_int * len(parte_frac))(*parte_frac)
    return conversao.ler_binario(arr_int, len(arr_int),  arr_frac, len(arr_frac))

def adicaobin(pi1, pf1, pi2, pf2):
    arr_pi1 = (ctypes.c_int * len(pi1))(*pi1)
    arr_pf1 = (ctypes.c_int * len(pf1))(*pf1)
    arr_pi2 = (ctypes.c_int * len(pi2))(*pi2)
    arr_pf2 = (ctypes.c_int * len(pf2))(*pf2)
    return conversao.adicaobin(arr_pi1, len(pi1), arr_pf1, len(pf1), arr_pi2, len(pi2), arr_pf2, len(pf2))

def subtracaobin(pi1, pf1, pi2, pf2):
    arr_pi1 = (ctypes.c_int * len(pi1))(*pi1)
    arr_pf1 = (ctypes.c_int * len(pf1))(*pf1)
    arr_pi2 = (ctypes.c_int * len(pi2))(*pi2)
    arr_pf2 = (ctypes.c_int * len(pf2))(*pf2)
    return conversao.subtracaobin(arr_pi1, len(pi1), arr_pf1, len(pf1), arr_pi2, len(pi2), arr_pf2, len(pf2))

def multibin(pi1, pf1, pi2, pf2):
    arr_pi1 = (ctypes.c_int * len(pi1))(*pi1)
    arr_pf1 = (ctypes.c_int * len(pf1))(*pf1)
    arr_pi2 = (ctypes.c_int * len(pi2))(*pi2)
    arr_pf2 = (ctypes.c_int * len(pf2))(*pf2)
    return conversao.multibin(arr_pi1, len(pi1), arr_pf1, len(pf1), arr_pi2, len(pi2), arr_pf2, len(pf2))

def divbin(pi1, pf1, pi2, pf2):
    arr_pi1 = (ctypes.c_int * len(pi1))(*pi1)
    arr_pf1 = (ctypes.c_int * len(pf1))(*pf1)
    arr_pi2 = (ctypes.c_int * len(pi2))(*pi2)
    arr_pf2 = (ctypes.c_int * len(pf2))(*pf2)
    return conversao.divbin(arr_pi1, len(pi1), arr_pf1, len(pf1), arr_pi2, len(pi2), arr_pf2, len(pf2))

def DecimalOctal(num: int) -> int:
    return conversao.DecimalOctal(ctypes.c_int(num))

def OctalDecimal(num: int) -> int:
    return conversao.OctalDecimal(ctypes.c_int(num))

def OctalBinario(num: int) -> int:
    return conversao.OctalBinario(ctypes.c_int(num))
