<<<<<<< HEAD
# Chatbot de Voz com LLM e Integração de Áudio

## 1. Visão Geral

Este projeto implementa um **chatbot de voz** baseado em **modelos de linguagem de última geração (LLMs)**, com interação totalmente por **áudio** — o usuário fala, o sistema transcreve, gera uma resposta textual via modelo de linguagem e retorna a resposta em voz sintetizada.  

O protótipo foi desenvolvido como parte de uma apresentação conceitual para demonstrar a arquitetura, funcionalidades e aplicabilidade de soluções de IA conversacional em contextos de atendimento automatizado e assistentes inteligentes.

## 2. Arquitetura do Sistema

O fluxo principal do chatbot é composto por quatro etapas:

1. **Entrada de Áudio (Speech-to-Text)**  
   - Utiliza a biblioteca `SpeechRecognition` para capturar e transcrever a fala do usuário.

2. **Processamento da Mensagem (LLM)**  
   - O texto transcrito é enviado para um modelo de linguagem hospedado no **Groq API**, utilizando o modelo **Llama 3.3 70B Versatile** para gerar respostas contextuais e naturais.

3. **Geração de Áudio (Text-to-Speech)**  
   - A resposta textual é convertida em voz por meio da biblioteca `gTTS`, criando uma interação de conversação por áudio.

4. **Saída de Áudio**  
   - O áudio gerado é reproduzido com a biblioteca `pygame`, encerrando o ciclo de interação.

**Fluxo resumido:**
```
Usuário (voz) → SpeechRecognition → LLM (Groq / Llama 3.3) → gTTS → Pygame (voz)
```

## 3. Estrutura do Projeto

```
📁 chatbot-voz-groq/
│
├── app.py                    # Código principal do chatbot
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação do projeto
└── tests/
    └── exemplos_teste.txt    # Exemplos de entrada e saída (testes de usuário)
```

## 4. Instalação e Execução

### Pré-requisitos
- Python 3.12 ou superior  
- Conexão com a Internet  
- Microfone funcional  
- Conta gratuita ou chave de acesso da **Groq API**

### Passos de Instalação

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/chatbot-voz-groq.git
   cd chatbot-voz-groq
   ```

2. **Criar e ativar um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate        # Windows
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar a variável de ambiente:**
   ```bash
   export GROQ_API_KEY="sua_chave_aqui"      # Linux/Mac
   setx GROQ_API_KEY "sua_chave_aqui"        # Windows
   ```

5. **Executar o aplicativo:**
   ```bash
   python app.py
   ```

## 5. Funcionalidades

- Reconhecimento de fala em tempo real  
- Integração com modelo de linguagem Groq (Llama 3.3)  
- Conversão automática de texto em voz  
- Interface de linha de comando com retorno auditivo  
- Compatível com CPU (não requer GPU)

## 6. Testes com Usuários

Foram realizados testes com diferentes tipos de entrada de voz:
- Perguntas diretas: “Qual é a capital da França?”  
- Perguntas contextuais: “E da Itália?”  
- Interações com hesitação ou ruído: “Floren... digo... Roma”

Resultados:
- Boa precisão na transcrição de voz  
- Tempo médio de resposta inferior a 3 segundos  
- Conversão de áudio clara e natural

## 7. Validação Técnica

- Código modular e compatível com sistemas baseados em CPU  
- Dependências atualizadas para compatibilidade com o ambiente Python 3.12+  
- Estrutura pronta para integração com interfaces gráficas (Streamlit, Flask ou Gradio)

## 8. Validação de Negócio

O modelo demonstra a viabilidade de **assistentes de voz inteligentes** para contextos corporativos e bancários, oferecendo:
- Atendimento automatizado com linguagem natural  
- Acessibilidade aprimorada (interação por voz)  
- Redução de custos operacionais  
- Experiência de usuário mais fluida e inclusiva  

## 9. Próximos Passos

- Adição de memória de contexto nas conversas  
- Implementação de interface web com Streamlit  
- Suporte multilíngue  
- Integração com bancos de dados e APIs externas  

## 10. Autor

**João Víctor Leite**  
Projeto desenvolvido para fins de demonstração técnica e conceitual.  
Contato: [seu.email@exemplo.com]  
GitHub: [https://github.com/seu-usuario](https://github.com/seu-usuario)
=======
# Desafio_ChatBot
>>>>>>> 8d0d35af360987b4fead92f4ae1a401dcef952a8
