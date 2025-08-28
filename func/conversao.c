#include <math.h>
#include "conversao.h"

CONVERSAO_EXPORT char* decbin_part_frac(float num)
{
    static char bin[33];
    int i = 0;

    while (num > 0 && i < 32)
    {
        num *= 2;
        if (num >= 1.0f) {
            bin[i++] = '1';
            num -= 1.0f;
        } else {
            bin[i++] = '0';
        }
    }
    bin[i] = '\0';
    return bin; 
}

CONVERSAO_EXPORT char* dec_bin(int num)
{
    static char bin[32];
    int i = 0, idx= 0, vet[32];

    do
    {
        vet[i++] = num % 2;
        num /= 2;
    } while (num > 0);

    for (int j = i - 1; j >= 0; j--)
    {
        bin[idx++] = vet[j] + '0';
    }
    bin[idx] = '\0';
    return bin;
}

CONVERSAO_EXPORT int parteint(const int* vet, int j)
{
    int soma = 0;
    for (int i = 0; i < j; i++)
    {
        if (vet[i] == 1)
        {
            soma += (int)pow(2, j - 1 - i);
        }
    }
    return soma;
}

CONVERSAO_EXPORT float partfrac(const int* vet, int j)
{
    float soma = 0;
    for (int i = 0; i < j; i++)
    {
        if (vet[i] == 1)
        {
            soma += pow(2, -(i + 1));
        }
    }
    return soma;
}

CONVERSAO_EXPORT float ler_binario(const int* parte_int, int tam_int, const int* parte_frac, int tam_frac)
{
    float resultado = 0;
    if (tam_int > 0)
        resultado += parteint(parte_int, tam_int);
    if (tam_frac > 0)
        resultado += partfrac(parte_frac, tam_frac);
    return resultado;
}

CONVERSAO_EXPORT float adicaobin(
    const int* parte_int1, int tam_int1, const int* parte_frac1, int tam_frac1,
    const int* parte_int2, int tam_int2, const int* parte_frac2, int tam_frac2)
{
    float num1 = ler_binario(parte_int1, tam_int1, parte_frac1, tam_frac1);
    float num2 = ler_binario(parte_int2, tam_int2, parte_frac2, tam_frac2);
    return num1 + num2;
}

CONVERSAO_EXPORT float subtracaobin(
    const int* parte_int1, int tam_int1, const int* parte_frac1, int tam_frac1,
    const int* parte_int2, int tam_int2, const int* parte_frac2, int tam_frac2)
{
    float num1 = ler_binario(parte_int1, tam_int1, parte_frac1, tam_frac1);
    float num2 = ler_binario(parte_int2, tam_int2, parte_frac2, tam_frac2);
    return num1 - num2;
}

CONVERSAO_EXPORT float multibin(
    const int* parte_int1, int tam_int1, const int* parte_frac1, int tam_frac1,
    const int* parte_int2, int tam_int2, const int* parte_frac2, int tam_frac2)
{
    float num1 = ler_binario(parte_int1, tam_int1, parte_frac1, tam_frac1);
    float num2 = ler_binario(parte_int2, tam_int2, parte_frac2, tam_frac2);
    return num1 * num2;
}

CONVERSAO_EXPORT float divbin(
    const int* parte_int1, int tam_int1, const int* parte_frac1, int tam_frac1,
    const int* parte_int2, int tam_int2, const int* parte_frac2, int tam_frac2)
{
    float num1 = ler_binario(parte_int1, tam_int1, parte_frac1, tam_frac1);
    float num2 = ler_binario(parte_int2, tam_int2, parte_frac2, tam_frac2);
    if (num2 == 0) return 0; // ou trate erro de divisão por zero
    return num1 / num2;
}

CONVERSAO_EXPORT int DecimalOctal(int valor)
{
    int valorOctal=0, valorOctalFinal=0, resto;

    while (valor >= 8)
    {
        resto = valor % 8;
        valor = valor / 8;
        valorOctal = valorOctal * 10 + resto;
        if (valor < 8)
        {
            valorOctal = valorOctal * 10 + valor;
        }
    }

    while (valorOctal > 0)
    {
        resto = valorOctal % 10;
        valorOctal = valorOctal / 10;
        valorOctalFinal = valorOctalFinal * 10 + resto;
    }
    return valorOctalFinal;
}

CONVERSAO_EXPORT int OctalDecimal(int valorOctal)
{
    int valorDecimalFinal=0, resto, index=0;

    while (valorOctal >= 8)
    {
        resto = valorOctal % 10;
        valorOctal = valorOctal / 10;
        valorDecimalFinal = valorDecimalFinal + resto * pow(8 , index);
        index++;
        if (valorOctal < 8)
        {
            valorDecimalFinal = valorDecimalFinal + valorOctal * pow(8 , index);
        }
    }
    return valorDecimalFinal;
}