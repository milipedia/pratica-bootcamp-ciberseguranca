# Simulação de Força Bruta — Laboratório Educacional (Kali + Alvos Vulneráveis)

**Aviso importante:** Este repositório contém materiais educacionais para uso **exclusivamente em ambientes controlados e autorizados** (por exemplo, máquinas virtuais que você possui). Fazer testes de intrusão em sistemas de terceiros sem permissão é ilegal e antiético. Alguns arquivos aqui são exemplos de wordlists e scripts de **detecção/monitoramento**, não ferramentas de ataque. Use com responsabilidade.

## Conteúdo do repositório
- `README.md` - este arquivo com instruções e contexto.
- `wordlists/` - contém wordlists de exemplo (curtas) para fins de teste controlado.
- `scripts/` - scripts seguros para **detecção** (ex.: analisar logs de autenticação) e utilitários (gerar wordlists de teste).
- `images/` - pasta opcional para capturas de tela organizadas (adicione suas imagens se desejar).
- `docs/` - documentação adicional e o relatório em Markdown (`relatorio_forca_bruta.md`).

## Objetivo
Reunir material didático para montar um laboratório local que permita estudar ataques de força bruta, análise de logs e medidas de mitigação. Este repositório **NÃO** fornece instruções operacionais para atacar sistemas de terceiros.

## Como usar (passo a passo)
1. **Clone o repositório** localmente:
```bash
git clone https://github.com/<seu-usuario>/<seu-repositorio>.git
cd <seu-repositorio>
```

2. **Insira suas capturas de tela** (opcional):
Coloque imagens em `images/` e atualize `images/README.md` com legendas e contexto.

3. **Executar o script de detecção de falhas (exemplo)**:
O script `scripts/detect_auth_failures.py` examina um arquivo de log (ex.: `/var/log/auth.log`) e mostra usuários com muitas falhas de login.
```bash
# Pré-requisito: Python 3
python3 scripts/detect_auth_failures.py --log sample_logs/auth.log --threshold 5
```

> **ATENÇÃO:** Nunca aponte scripts automáticos para sistemas que não sejam de sua propriedade ou sem autorização explícita.

4. **Gerar wordlists de teste (curtas)**:
Use `scripts/gen_wordlist.py` para criar listas de senhas de exemplo para o laboratório.
```bash
python3 scripts/gen_wordlist.py --output wordlists/wordlist_curta.txt --size 50
```

## Boas práticas ao publicar
- Remova credenciais e logs sensíveis antes de commitar.  
- Não inclua comandos que facilitem explorações em ambientes não autorizados.  
- Prefira publicar apenas relatórios e materiais de mitigação para o público geral.

## Estrutura sugerida de pastas
```
/ (root)
├─ README.md
├─ relatorio_forca_bruta.md
├─ wordlists/
│  ├─ wordlist_curta.txt
├─ scripts/
│  ├─ detect_auth_failures.py
│  ├─ gen_wordlist.py
├─ images/
│  ├─ README.md
└─ docs/
   ├─ relatorio_forca_bruta.md
```

## Licença
Material educativo — sinta-se livre para reutilizar com atribuição. Consulte [LICENSE](LICENSE) se desejar incluir uma licença formal (p.ex. MIT).
