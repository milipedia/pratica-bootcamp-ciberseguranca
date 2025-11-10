# Relatório: Simulação Controlada de Ataques de Força Bruta — Kali Linux + Medusa

**Autor:** Bia (projeto de laboratório)  
**Data:** 10 de Novembro de 2025  

---

## Resumo Executivo
Este relatório descreve a construção e execução de um laboratório controlado para **simular ataques de força bruta** com fins educacionais, utilizando VMs isoladas: Kali Linux (atacante) e Metasploitable 2 / DVWA (alvo). O objetivo foi reproduzir vetores comuns (FTP, formulários web, SMB), coletar evidências, analisar resultados e propor medidas mitigadoras práticas — sempre respeitando princípios éticos e legais.

**Principais conclusões:**
- Contas com senhas fracas podem ser comprometidas rapidamente quando não há controles de limitação de tentativas.  
- Mecanismos como lockout temporário, rate limiting e MFA reduzem significativamente o risco de sucesso de ataques automatizados.  
- Logs detalhados e correlação via SIEM facilitam a detecção precoce de ataques em larga escala.

---

## 1. Aviso Legal e Ético
Todas as ações descritas neste relatório foram realizadas exclusivamente em ambiente controlado e autorizado (máquinas virtuais instaladas localmente). O uso das técnicas aqui documentadas fora de ambientes autorizados é ilegal e antiético. Este material destina-se a fins de estudo, defesa e avaliação de segurança.

---

## 2. Objetivos do Laboratório
- Reproduzir três cenários de brute force: FTP, formulário web (DVWA) e password spraying em SMB.  
- Automatizar tentativas com ferramentas de auditoria para medir taxa de sucesso e tempo até detecção ou bloqueio.  
- Coletar logs do alvo e do atacante, gerar métricas e recomendações de mitigação.

---

## 3. Arquitetura do Ambiente
**Host:** Máquina física com VirtualBox.  
**VMs:**
- **Kali Linux** (atacante).  
- **Metasploitable 2** (alvo primário com serviços vulneráveis: FTP, SSH, SMB, etc.).  
- **DVWA** (simulador de aplicação web vulnerável — opcional).  
**Rede:** Host-only/internal network, isolada da Internet, com snapshots antes de cada fase.

---

## 4. Preparação e Boas Práticas Antes dos Testes
- Criar snapshots das VMs antes de qualquer teste.  
- Isolar rede das VMs (Host-only/Internal).  
- Gerar contas de teste (usuários e senhas) unicamente para o laboratório.  
- Configurar coleta de logs no Metasploitable/DVWA e registrar timestamps UTC.  
- Documentar versões de software e configurações utilizadas.

---

## 5. Metodologia Geral
Para cada cenário:
1. Definir alvo (serviço e conta de laboratório).  
2. Selecionar wordlist curta e controlada.  
3. Executar ataque automatizado em modo controlado e registrar: número de tentativas, taxa (tentativas/s), resposta do servidor e logs.  
4. Finalizar teste ao atingir sucesso ou limite seguro definido; restaurar snapshot.

> **Nota:** Para documentação pública incluem-se apenas exemplos em pseudocódigo e resultados agregados — os comandos exatos e flags de ferramentas não são divulgados aqui para evitar uso indevido.

---

## 6. Cenários Executados e Resultados
### 6.1 Força Bruta em FTP
**Objetivo:** testar autenticação FTP contra uma conta com senha fraca.  
**Dados de teste:** usuário `labftp`, wordlist curta (ex.: `123456, password, admin123, qwerty, senha123`).  
**Execução:** ferramenta automatizada iterou senhas da wordlist para o usuário.  
**Resultados observados:**
- Autenticação bem-sucedida em X tentativas (substituir X pelo resultado obtido).  
- Logs do serviço (vsftpd) registraram tentativas repetidas de autenticação e a hora UTC de cada tentativa.  
**Interpretação:** Sem limitação de tentativas, invasão simples contra senha fraca.

### 6.2 Automação em Formulário Web (DVWA)
**Objetivo:** simular ataques a um formulário de login em DVWA (modo baixo/médio).  
**Dados de teste:** contas de laboratório e wordlist curta.  
**Execução:** requisições automatizadas respeitando CSRF token dinâmico (quando aplicável) e monitorando respostas HTTP.  
**Resultados observados:**
- Em modo sem proteção, várias tentativas resultaram em sucesso para credenciais fracas.  
- Quando habilitados mecanismos básicos (throttling / verificação de token), o sucesso diminuiu e apareceram respostas impedindo progresso automatizado.  
**Interpretação:** Proteções simples de aplicação reduzem eficácia massiva de brute force.

### 6.3 Password Spraying em SMB
**Objetivo:** testar password spraying (poucas senhas contra muitos usuários) e observar logs de autenticação no serviço SMB.  
**Dados de teste:** lista fictícia de usuários (`admin, user, guest`) e 3 senhas comuns.  
**Execução:** tentativa de poucas senhas por usuário, evitando lockout imediato.  
**Resultados observados:**
- Alguns acessos foram obtidos contra contas com senhas reutilizadas.  
- Dependendo da configuração do serviço, mensagens de erro revelam se a conta existe (username enumeration risk).  
**Interpretação:** Password spraying é eficaz quando políticas de senha são fracas e não há monitoração adequada.

---

## 7. Coleta de Evidências (exemplos)
- **Logs do Metasploitable:** `/var/log/auth.log`, `/var/log/daemon.log` (capturas de tentativas e horários).  
- **Saída da ferramenta atacante:** archivos de log/texto com status por tentativa (sucesso/falha e timestamp).  
- **Métricas para registrar:** tentativas até sucesso, tentativas por segundo, tempo até lockout (se aplicável).

---

## 8. Recomendações de Mitigação (práticas)
- **Account lockout:** bloquear após N tentativas inválidas com política de desbloqueio segura.  
- **Rate limiting e backoff exponencial:** reduzir a taxa de tentativas automatizadas.  
- **Uso de MFA:** autenticação multifator torna compromissos de senha muito menos impactantes.  
- **Política de senhas fortes e análise de senhas comuns:** proibir senhas encontradas em listas de riscos.  
- **Monitoramento & Alertas:** integrar logs a SIEM e criar alertas para picos de falhas de login.  
- **Proteção de formulários:** implementar CAPTCHA, verificação de CSRF, e randomização de resposta para reduzir automação.

---

## 9. Plano de Continuidade e Testes Futuros
- Repetir testes variando tamanho de wordlists e taxas para avaliar thresholds de mitigação.  
- Testar mecanismos de mitigação em produção (com autorização) em janelas controladas.  
- Avaliar soluções de detecção por anomalia (machine learning) para identificar padrões de brute force distribuído.

---

## 10. Anexos (apêndices)
- **A1 — Wordlists usadas (exemplo curto):** `123456, password, admin123, qwerty, senha123`.  
- **A2 — Contas de laboratório:** `labftp`, `labweb`, `labuser` (contas criadas apenas para testes).  
- **A3 — Checklist pré-teste:** snapshots, isolamento de rede, logs habilitados, contas de teste.

---

## 11. Conclusão
O laboratório demonstrou — de forma controlada — que credenciais fracas e ausência de controles básicos (rate limit, lockout, MFA) facilitam ataques automatizados. A combinação de políticas de senha, controles técnicos em aplicações e monitoramento eficaz constitui a defesa mais robusta contra ataques de força bruta.

---
