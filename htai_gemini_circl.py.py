import re
import os
import requests
from dotenv import load_dotenv
import json
from rich.markdown import Markdown
from rich import print
from typing import Optional, Dict, Any

# 🌐 Configuração da API Gemini
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# ✅ Validação de formato CVE
def validar_cve(cve_id: str) -> bool:
    return re.match(r"^CVE-\d{4}-\d{4,6}$", cve_id.upper())

# 🔍 Busca a descrição oficial na API CIRCL
def buscar_descricao_cve_circl(cve_id: str) -> str:
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        containers: Dict[str, Any] = dados.get("containers", {})
        cna: Dict[str, Any] = containers.get("cna", {})
        descricoes: list[Dict[str, str]] = cna.get("descriptions", [])
        for item in descricoes:
            if item.get("lang") == "en":
                return item.get("value")

        return dados.get("summary", "Descrição não localizada na API CIRCL.")
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API CIRCL: {e}"
    except json.JSONDecodeError:
        return "Erro ao decodificar a resposta da API CIRCL (JSON inválido)."
    except Exception as e:
        return f"Erro inesperado ao buscar descrição do CVE: {e}"

# 🧠 Criação do prompt com bloco fixo literal da Conviso
def montar_prompt(descricao: str, cve_id: str) -> str:
    return (
        f"🛡️ **Agente Educacional Hacktiba – Pulse 00 – 2025**\n\n"
        f"## Análise da vulnerabilidade: {cve_id}\n\n"
        f"### 📄 Descrição oficial:\n{descricao}\n\n"
        "Com base **estritamente** na descrição fornecida, responda:\n\n"
        "1.  **Explicação da falha (para desenvolvedor iniciante):**\n"
        "2.  **Este CVE poderia ter sido evitado se:**\n"
        "3.  **Relação com OWASP SAMM:**\n"
        "4.  Finalize com o seguinte texto **copiado literalmente, sem alterações**:\n\n"
        "---\n"
        "Quer saber mais sobre como enfrentar desafios reais com cenários de vulnerabilidades —  \n"
        "seja com CVEs conhecidos ou até mesmo falhas ainda não publicadas, identificadas diretamente no seu código?\n\n"
        "Faça o assessment gratuito da Conviso e descubra como evoluir a maturidade em AppSec da sua empresa:  \n"
        "https://www.convisoappsec.com/pt-br/recursos/security-assessment\n"
        "---"
    )

# 🚀 Envia o prompt para Gemini
def enviar_para_gemini(prompt: str) -> str:
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    try:
        response = requests.post(GEMINI_ENDPOINT, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except requests.exceptions.RequestException as e:
        return f"Erro na API Gemini: {e}"
    except json.JSONDecodeError:
        return "Erro ao decodificar a resposta da API Gemini (JSON inválido)."
    except Exception as e:
        return f"Erro inesperado ao obter resposta do Gemini: {e}"

# 🎯 Execução interativa
if __name__ == "__main__":
    print("🧠 HT-AI Hacktiba – Pulse 00 – 2025 (CIRCL.lu + Gemini)")
    print("Digite um CVE (ex: CVE-2021-24019) ou 'sair' para encerrar.")
    while True:
        entrada = input("> ")
        if entrada.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando o HT-AI. Até logo!")
            break
        try:
            if not validar_cve(entrada.strip()):
                print("⚠️  Formato inválido. Use: CVE-YYYY-NNNNN")
                continue
            descricao = buscar_descricao_cve_circl(entrada.strip())
            if descricao.startswith("Erro ao acessar") or descricao.startswith("Descrição não localizada"):
                print(descricao)
                continue
            prompt = montar_prompt(descricao, entrada.strip())
            resposta = enviar_para_gemini(prompt)
            if resposta.startswith("Erro na API Gemini"):
                print(resposta)
                continue
            print("\n" + "—" * 30 + "\n")
            print(f"Resposta do HT-AI:\n")
            print(Markdown(resposta))
            print("\n" + "—" * 30 + "\n")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
