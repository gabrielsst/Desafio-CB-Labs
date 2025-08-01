# 🍽️ Desafio de Engenharia de Dados – Rede de Restaurantes

## 📌 Objetivo

Este projeto tem como objetivo coletar, armazenar e estruturar dados provenientes de múltiplos endpoints de API relacionados ao funcionamento de restaurantes (pedidos, pagamentos, impostos, etc.). Os dados são armazenados de forma organizada em um data lake local para futura análise por equipes de BI.

---

## 🚀 Funcionalidades

- 📥 Coleta automática de dados de 5 endpoints via `POST`
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

```

data-lake/
└── restaurant\_chain/
└── raw/
├── bi/
│   └── getFiscalInvoice/
│       └── year=2025/month=07/day=31/storeId=R001/response.json
├── res/
│   └── getGuestChecks/
│       └── ...
└── ...

````

---

## ⚙️ Como usar

### 1. Clonar o projeto

```bash
git clone https://github.com/seuusuario/nome-do-repo.git
cd nome-do-repo
````

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

> Obs: Se não existir um `requirements.txt`, basta instalar `requests`:

```bash
pip install requests
```

### 3. Executar o script de coleta

```bash
python coletor_respostas_api.py
```

---

## ✅ Checklist de Atividades

* [x] Análise do JSON do ERP
* [x] Transformação para modelo relacional
* [x] Armazenamento local com partições
* [x] Estrutura de código modular e legível
* [x] Kanban para acompanhamento no VS Code
* [ ] Integração com armazenamento em nuvem (futuro)

---

## 🧠 Lições aprendidas

* A importância do versionamento de schemas para APIs corporativas
* Como organizar dados brutos de forma escalável para análise posterior
* Práticas de engenharia de dados modernas aplicadas localmente

---

## 📄 Licença

Este projeto é de uso educacional e pode ser adaptado livremente.

Se quiser, posso gerar esse `README.md` como arquivo direto para download, ou personalizar para outro formato de documentação (ex: GitHub Wiki, MkDocs, etc.). Deseja isso?
