# ⚡ Desafio Clarke Energia - Backend

### 🌍 API para Escolha Inteligente de Fornecedores de Energia

Este é o **backend** do **Desafio Clarke Energia**, uma API desenvolvida em **Flask** com **PostgreSQL**, responsável por gerenciar fornecedores e processar os dados de consumo de energia dos usuários. 🔥🚀

---

## 🚀 Funcionalidades Principais
✅ Endpoint para o usuário informar seu **consumo mensal de energia**

✅ Retorno de **fornecedores disponíveis** que atendem à demanda informada

✅ Cada fornecedor possui:
   - **Nome e logo** 🏢
   - **Estado de origem** 📍
   - **Custo por kWh** 💰
   - **Limite mínimo de consumo** ⚠️
   - **Número total de clientes** 👥
   - **Avaliação média dos clientes** ⭐

✅ Banco de dados **PostgreSQL** para armazenamento eficiente dos fornecedores

---

## 🛠️ Tecnologias Utilizadas

🔹 **Python (Flask)** - API leve e escalável

🔹 **PostgreSQL** - Banco de dados relacional

🔹 **SQLAlchemy** - Comunicação com o banco de dados

🔹 **Flask-CORS** - Permitir requisições do frontend

---

## 📦 Instalação e Execução

### 🔧 1. Configurar e rodar localmente

1️⃣ **Clone este repositório:**
```bash
 git clone https://github.com/GabrielSales10/clarke_desafio_backend.git
```

2️⃣ **Acesse o diretório do projeto:**
```bash
 cd clarke_desafio_backend
```

3️⃣ **Crie e ative um ambiente virtual:**
```bash
 python -m venv venv
 source venv/bin/activate  # Linux/macOS
 venv\Scripts\activate  # Windows
```

4️⃣ **Instale as dependências:**
```bash
 pip install -r requirements.txt
```

A API estará disponível em **http://127.0.0.1:5000** 🚀

---
