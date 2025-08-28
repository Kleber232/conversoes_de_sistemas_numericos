#ifndef CONVERSAO_H
#define CONVERSAO_H

#ifdef CONVERSAO_EXPORTS
#define CONVERSAO_EXPORT __declspec(dllexport)
#else
#define CONVERSAO_EXPORT __declspec(dllimport)
#endif

#ifdef __cplusplus
extern "C" {
#endif

// Função que lê a parte decimal fracionária e converte em binário
CONVERSAO_EXPORT char* decbin_part_frac(float);
// Função que recebe como parâmetro um número decimal inteiro e converte em binário
CONVERSAO_EXPORT char* dec_bin(int);
// Função que lê a parte binária inteira e converte em decimal
CONVERSAO_EXPORT int parteint(const int*, int);
// Função que lê a parte binária fracionária e converte em decimal
CONVERSAO_EXPORT float partfrac(const int*, int);
// Função que direciona a parte inteira e fracionária para a sua devida função
CONVERSAO_EXPORT float ler_binario(const int*, int, const int*, int);

// Operação de adição
CONVERSAO_EXPORT float adicaobin(const int*, int, const int*, int, const int*, int, const int*, int);
// Operação de subtração
CONVERSAO_EXPORT float subtracaobin(const int*, int, const int*, int, const int*, int, const int*, int);
// Operação de multiplicação
CONVERSAO_EXPORT float multibin(const int*, int, const int*, int, const int*, int, const int*, int);
// Operação de divisão
CONVERSAO_EXPORT float divbin(const int*, int, const int*, int, const int*, int, const int*, int);

// Conversão de Decimal para Octal
CONVERSAO_EXPORT int DecimalOctal(int);
// Conversão de Octal para Decimal
CONVERSAO_EXPORT int OctalDecimal(int);
// Conversão de Octal para Binário
CONVERSAO_EXPORT int OctalBinario(int);

#ifdef __cplusplus
}
#endif

#endif