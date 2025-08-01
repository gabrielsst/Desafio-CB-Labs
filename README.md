# 🍽️ Desafio de Engenharia de Dados – Rede de Restaurantes

## 📌 Objetivo

Este projeto tem como objetivo coletar, armazenar e estruturar dados provenientes de múltiplos endpoints de API relacionados ao funcionamento de restaurantes (pedidos, pagamentos, impostos, etc.). Os dados são armazenados de forma organizada em um data lake local para futura análise por equipes de BI.

---

## 🚀 Funcionalidades

- 📥 Postagem automática de dados de 5 endpoints via `POST`
- 🗂️ Armazenamento em estrutura de pastas particionada por:
  - **Data** (`year=YYYY/month=MM/day=DD`)
  - **Loja** (`storeId=XXX`)
  - **Endpoint**
- 🧪 Manipulação de JSON e controle de schema
- 💾 Persistência local (data lake simulado com arquivos `.json`)
- 📊 Suporte à normalização para bancos relacionais (como SQLite)

---

## 🔗 Endpoints Utilizados

| Serviço | Endpoint |
|--------|----------|
| Fiscal | `bi/getFiscalInvoice` |
| Comandas | `res/getGuestChecks` |
| Estornos | `org/getChargeBack` |
| Transações | `trans/getTransactions` |
| Caixa | `inv/getCashManagementDetails` |

---

## 🛠️ Tecnologias

- Python 3.10+
- Biblioteca `requests`
- `json` e `pathlib` para manipulação de arquivos
- SQLite (opcional para normalização)
- VS Code (suporte opcional com Markdown Kanban)

---

## 📂 Estrutura de Pastas

