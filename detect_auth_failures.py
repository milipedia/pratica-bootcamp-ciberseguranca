#!/usr/bin/env python3
"""scripts/detect_auth_failures.py
Analisa um arquivo de logs (formato simples) e lista usuários com muitas falhas de autenticação.
Formato de exemplo esperado (cada linha): <timestamp> <service>: Failed login for user '<username>'
Este é um script educacional; adapte-o ao formato real dos seus logs antes de usar.
"""
import argparse
from collections import defaultdict
import re

parser = argparse.ArgumentParser(description='Detectar usuários com muitas falhas de autenticação (exemplo).')
parser.add_argument('--log', required=True, help='Caminho para o arquivo de log (texto).')
parser.add_argument('--threshold', type=int, default=10, help='Número de falhas para disparar um alerta.')
args = parser.parse_args()

fail_re = re.compile(r"failed.*for user\s+'(?P<user>[^']+)'", re.IGNORECASE)
counts = defaultdict(int)

with open(args.log, encoding='utf-8', errors='ignore') as f:
    for line in f:
        m = fail_re.search(line)
        if m:
            user = m.group('user')
            counts[user] += 1

print(f"Relatório de falhas (threshold = {args.threshold}):\n")
for user, c in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    status = 'ALERTA' if c >= args.threshold else ''
    print(f"{user:20} {c:5} {status}")