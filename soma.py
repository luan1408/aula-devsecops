import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', required=True, help='Primeiro número')
parser.add_argument('-b', required=True, help='Segundo número')
args = parser.parse_args()

try:
    a = int(args.a)
    b = int(args.b)
    soma = a + b
    print(f"A soma é: {soma}")
except ValueError:
    print("Erro: os valores de 'a' e 'b' devem ser números inteiros.")
    exit(1)
