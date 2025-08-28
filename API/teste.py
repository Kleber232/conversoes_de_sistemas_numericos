from conversao import *

def input_int_list(msg):
    return [int(x) for x in input(msg).strip().split()]

def main():
    print("Teste decbin_part_frac")
    num = float(input("Digite um número fracionário: "))
    print("Binário da parte fracionária:", decbin_part_frac(num))

    print("\nTeste dec_bin")
    num = int(input("Digite um número inteiro: "))
    print("Binário:", dec_bin(num))

    print("\nTeste parteint")
    bits = input_int_list("Digite os bits da parte inteira separados por espaço (ex: 1 0 1 1): ")
    print("Decimal:", parteint(bits))

    print("\nTeste partfrac")
    bits = input_int_list("Digite os bits da parte fracionária separados por espaço (ex: 1 0 1): ")
    print("Decimal:", partfrac(bits))

    print("\nTeste ler_binario")
    parte_int = input_int_list("Bits da parte inteira: ")
    parte_frac = input_int_list("Bits da parte fracionária: ")
    print("Decimal:", ler_binario(parte_int, parte_frac))

    print("\nTeste adicaobin")
    pi1 = input_int_list("Bits parte inteira 1: ")
    pf1 = input_int_list("Bits parte fracionária 1: ")
    pi2 = input_int_list("Bits parte inteira 2: ")
    pf2 = input_int_list("Bits parte fracionária 2: ")
    print("Soma:", adicaobin(pi1, pf1, pi2, pf2))

    print("\nTeste subtracaobin")
    pi1 = input_int_list("Bits parte inteira 1: ")
    pf1 = input_int_list("Bits parte fracionária 1: ")
    pi2 = input_int_list("Bits parte inteira 2: ")
    pf2 = input_int_list("Bits parte fracionária 2: ")
    print("Subtração:", subtracaobin(pi1, pf1, pi2, pf2))

    print("\nTeste multibin")
    pi1 = input_int_list("Bits parte inteira 1: ")
    pf1 = input_int_list("Bits parte fracionária 1: ")
    pi2 = input_int_list("Bits parte inteira 2: ")
    pf2 = input_int_list("Bits parte fracionária 2: ")
    print("Multiplicação:", multibin(pi1, pf1, pi2, pf2))

    print("\nTeste divbin")
    pi1 = input_int_list("Bits parte inteira 1: ")
    pf1 = input_int_list("Bits parte fracionária 1: ")
    pi2 = input_int_list("Bits parte inteira 2: ")
    pf2 = input_int_list("Bits parte fracionária 2: ")
    print("Divisão:", divbin(pi1, pf1, pi2, pf2))

    print("\nTeste DecimalOctal")
    num = int(input("Digite um número decimal: "))
    print("Octal:", DecimalOctal(num))

    print("\nTeste OctalDecimal")
    num = int(input("Digite um número octal: "))
    print("Decimal:", OctalDecimal(num))

    print("\nTeste OctalBinario")
    num = int(input("Digite um número octal: "))
    print("Binário:", OctalBinario(num))

if __name__ == "__main__":
    main()
