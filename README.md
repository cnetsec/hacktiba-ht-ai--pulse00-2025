# 🧠 HT-AI CVE Gemini CIRCL

**Agente Educacional Hacktiba – Pulse 00 – 2025**

Este projeto é um assistente interativo que analisa vulnerabilidades com base em um ID CVE. Ele consulta a **API pública do CIRCL.lu** para obter a descrição oficial da falha e utiliza o **Gemini 2.0 Flash**, da Google, para gerar uma explicação acessível e educativa com base nas práticas do **OWASP SAMM**.

---

## 🎯 Objetivo

> Fornecer uma explicação clara, prática e embasada sobre vulnerabilidades reais, com foco educacional e direcionado para desenvolvedores e profissionais de segurança.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- [API CIRCL](https://cve.circl.lu/)
- [Gemini 2.0 Flash](https://aistudio.google.com/)
- `requests`, `python-dotenv`, `rich`

---

## 🚀 Instalação

1. Clone o repositório ou baixe os arquivos.
2. Instale as dependências:

```bash
pip install -r requirements.txt

A ferramenta solicitará que você insira um ID de CVE. Digite o CVE desejado (por exemplo, CVE-2021-24019) e pressione Enter.Para encerrar o programa, digite sair, exit ou quit.Exemplo de Saída🧠 HT-AI Hacktiba – Pulse 00 – 2025 (CIRCL.lu + Gemini)
Digite um CVE (ex: CVE-2021-24019) ou 'sair' para encerrar.
> CVE-2024-23091

——————————————————————————————

Resposta do HT-AI:

🛡️ Agente Educacional Hacktiba – Pulse 00 – 2025

## Análise da vulnerabilidade: CVE-2024-23091

### 📄 Descrição oficial:
Weak password hashing using MD5 in funzioni.php in HotelDruid before 1.32 allows an attacker to obtain plaintext passwords from hash values.

Com base estritamente na descrição fornecida, responda:

1.  **Explicação da falha (para desenvolvedor iniciante):**

    A falha CVE-2024-23091 no HotelDruid, antes da versão 1.32, ocorre porque as senhas dos usuários são armazenadas de forma insegura. Em vez de usar um método forte para "embaralhar" as senhas (o que chamamos de "hashing") para que não possam ser lidas diretamente, o sistema usa o MD5, que é considerado fraco. Imagine que você quer guardar um segredo, mas em vez de colocá-lo em um cofre com uma combinação complexa, você o esconde debaixo do tapete. O MD5 seria como esconder o segredo debaixo do tapete: é fácil para alguém mal-intencionado encontrar o segredo original a partir da versão "escondida" (o hash). Na prática, um atacante que tenha acesso aos hashes das senhas (por exemplo, acessando o banco de dados) pode facilmente "quebrar" o MD5 e descobrir as senhas reais dos usuários.

2.  **Este CVE poderia ter sido evitado se:**

    Para evitar esse tipo de problema, siga estas práticas:

    * Não use MD5 para hashing de senhas. Ele é obsoleto e facilmente quebrado.
    * Use algoritmos de hashing robustos: Use algoritmos como bcrypt, scrypt ou Argon2. Eles são projetados para serem mais resistentes a ataques de "força bruta" e "tabelas rainbow".
    * Use "salt" junto com o hash: Um "sal" é um valor aleatório único para cada senha que é adicionado à senha antes de ser "embaralhada" com o algoritmo de hashing. Isso torna ainda mais difícil quebrar o hash, mesmo que o atacante tenha acesso a tabelas precomputadas de hashes.
    * Mantenha as bibliotecas atualizadas: Certifique-se de usar as versões mais recentes das bibliotecas de segurança que você usa, pois elas podem incluir correções de bugs e melhorias de segurança.
    * Implemente políticas de senha fortes: Incentive os usuários a usar senhas complexas e alterá-las regularmente.

3.  **Relação com OWASP SAMM:**

    A falha CVE-2024-23091 está relacionada a várias práticas do OWASP SAMM (Software Assurance Maturity Model):

    * Design de Segurança (SD): Principalmente com SD-1: Definir Requisitos de Segurança. Uma falha como essa indica que não foram definidos requisitos claros de segurança para a proteção de dados sensíveis, como senhas. Também se relaciona com SD-3: Realizar Revisões de Design de Segurança. Revisões de design poderiam ter identificado o uso de MD5 e recomendado algoritmos mais robustos.
    * Implementação de Segurança (SI): Principalmente com SI-1: Aplicar Práticas de Codificação Seguras. O uso de MD5 demonstra uma falta de práticas de codificação seguras no tratamento de senhas. Também se relaciona com SI-3: Executar Análise Estática de Segurança. Uma análise estática de código poderia ter detectado o uso do MD5.
    * Teste de Segurança (ST): Principalmente com ST-3: Realizar Testes de Penetração. Testes de penetração focados em quebrar senhas (password cracking) provavelmente revelariam a fraqueza do algoritmo MD5.

    Em resumo, a correção desta vulnerabilidade e a implementação de boas práticas para hashing de senhas contribuem para aumentar a maturidade da segurança do software, em linha com os princípios e práticas do OWASP SAMM.

---

Quer saber mais sobre como enfrentar desafios reais com cenários de vulnerabilidades — seja com CVEs conhecidos ou até mesmo falhas ainda não publicadas, identificadas diretamente no seu código?

Faça o assessment gratuito da Conviso e descubra como evoluir a maturidade em AppSec da sua empresa:
https://www.convisoappsec.com/pt-br/recursos/security-assessment

---
