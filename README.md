# Phishing Lab Simulator 🛡️

Este é um projeto de simulação de phishing desenvolvido para fins estritamente **educacionais** e de **treinamento em segurança cibernética**. A ferramenta demonstra como ataques de *Credential Harvesting* funcionam na prática, integrando um servidor local com um túnel público via Ngrok.

## 🚀 Funcionalidades
- **Seleção de Templates:** Escolha entre interfaces pré-definidas (Facebook, Instagram) ou carregue seu próprio projeto HTML.
- **Túnel Público Automático:** Integração nativa com `pyngrok` para exposição segura e temporária do ambiente de teste.
- **Captura em Tempo Real:** Monitoramento de logs diretamente no terminal com formatação de cores.
- **Redirecionamento Seguro:** Após a captura, o alvo é redirecionado para o site oficial, simulando um ataque real de engenharia social.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Framework Web:** Flask
- **Túnel de Rede:** Ngrok
- **Interface de Terminal:** Colorama

## 📋 Pré-requisitos
1. **Python 3.10+** instalado.
2. **Conta no Ngrok:** É necessário um token de autenticação (grátis) para gerar a URL pública.
   - Obtenha em: [https://dashboard.ngrok.com/](https://dashboard.ngrok.com/)
3. **Edite o Código:** Após obter seu código de autenticação, procure o trecho no código onde ele deve ser inserido

## 🔧 Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/d34uthy/PhishingLab.git](https://github.com/d34uthy/PhishingLab.git)
   cd PhishingLab

2. **Instale o requirement:**
    ```bash
    pip install -r requirements.txt

3. **Execute a Ferramenta e Siga os Passos:**
    ```bash
    python lab_phishing.py
