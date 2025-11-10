#!/usr/bin/env python3
"""scripts/gen_wordlist.py
Gera uma wordlist curta e educativa para uso no laboratório local.
"""
import argparse
import random
import string

parser = argparse.ArgumentParser(description='Gerar wordlist curta para laboratório.')
parser.add_argument('--output', required=True, help='Arquivo de saída para a wordlist.')
parser.add_argument('--size', type=int, default=20, help='Quantidade de senhas a gerar.')
args = parser.parse_args()

base = ['password','123456','qwerty','senha','admin','user','letmein','welcome']
with open(args.output,'w',encoding='utf-8') as f:
    for i in range(args.size):
        suffix = ''.join(random.choices(string.digits, k=3))
        f.write(random.choice(base) + suffix + '\n')

print(f'Wordlist gerada em: {args.output}')