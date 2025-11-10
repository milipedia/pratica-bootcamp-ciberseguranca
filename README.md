# 🔐 Simulação de Força Bruta — Laboratório Educacional (Kali Linux + Metasploitable/DVWA)

**Autora:** Bia  
**Propósito:** Projeto educacional de cibersegurança — laboratório prático para compreender e mitigar ataques de força bruta.

---

## ⚠️ Aviso Legal e Ético

Este repositório é **exclusivamente para fins educacionais e laboratoriais**.  
Todos os testes devem ser realizados apenas em ambientes **isolados e de sua propriedade** (ex.: VMs locais).  
Qualquer tentativa de uso contra sistemas de terceiros sem permissão explícita é **ilegal e antiética**.

> ⚠️ Nenhum dos arquivos aqui fornece instruções ofensivas; o foco é em análise, prevenção e detecção.

---


## 🧠 Objetivo

O projeto demonstra, em ambiente controlado:
- Testes de **força bruta** simulados em serviços como FTP, SMB e formulários web (DVWA);
- Ferramentas de auditoria como **Medusa** no Kali Linux;
- Coleta de **logs** e análise de **falhas consecutivas** de autenticação;
- Boas práticas de **mitigação** e **resposta**.

---

## ⚙️ Requisitos

- **VirtualBox** (ou VMware)
- **2 VMs configuradas:**
  - Kali Linux → atacante (com Medusa instalada)
  - Metasploitable 2 → alvo vulnerável
- Rede **Host-Only/Internal**
- Python 3 (para executar os scripts)

---

## 🧩 Scripts incluídos

### 🔍 `detect_auth_failures.py`
Script para analisar logs e identificar contas com muitas falhas de login consecutivas.

```
python3 scripts/detect_auth_failures.py --log sample_logs/auth.log --threshold 5
```

Saída esperada:
```
Relatório de falhas (threshold = 5):

user1               8    ALERTA
user2               2
```

gen_wordlist.py

Gera uma pequena wordlist de senhas comuns para testes autorizados.
```
python3 scripts/gen_wordlist.py --output wordlists/wordlist_curta.txt --size 30
```

Resultado:
```
Wordlist gerada em: wordlists/wordlist_curta.txt
```

Relatório

O arquivo relatorio_forca_bruta.md
 descreve:

Arquitetura do laboratório

Cenários de ataque simulados

Logs coletados e evidências

Recomendações de mitigação

Conclusões e próximos passos
