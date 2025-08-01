# 🚀 Desafio Engenharia de Dados – Armazenamento de APIs no Data Lake

## ✅ 1. Por que armazenar as respostas das APIs?

Armazenar as respostas das APIs é essencial por vários motivos:

### 🎯 **Motivações principais:**

* **Rastreabilidade e Auditoria**
  Permite acompanhar o histórico de dados, reprocessar análises e garantir integridade.

* **Desacoplamento de sistemas**
  Evita chamadas frequentes às APIs externas, reduzindo dependência e melhorando desempenho.

* **Controle de versões de dados**
  Mantém registros conforme os dados evoluem com o tempo.

* **Análise em lote e reprocessamento**
  Permite ETLs periódicos e uso de ferramentas analíticas como Spark, Athena ou Presto.

* **Economia de custos e escalabilidade**
  Uma vez armazenado, o dado pode ser processado em larga escala no Data Lake sem penalizar sistemas de origem.

---

## 🗂️ 2. Como você armazenaria os dados?

### 🧱 Estrutura de Pastas Sugerida (em um Data Lake como S3, GCS, etc.)

```bash
data-lake/
└── restaurant_chain/
    └── raw/
        ├── bi/
        │   └── getFiscalInvoice/
        │       └── year=2024/month=07/day=31/storeId=R001/
        │           └── response.json
        ├── res/
        │   └── getGuestChecks/
        │       └── year=2024/month=07/day=31/storeId=R001/
        │           └── response.json
        ├── org/
        │   └── getChargeBack/
        │       └── year=2024/month=07/day=31/storeId=R001/
        │           └── response.json
        ├── trans/
        │   └── getTransactions/
        │       └── year=2024/month=07/day=31/storeId=R001/
        │           └── response.json
        └── inv/
            └── getCashManagementDetails/
                └── year=2024/month=07/day=31/storeId=R001/
                    └── response.json
```

### 📌 **Detalhes da Estrutura:**

* `year=YYYY/month=MM/day=DD` ➜ particionamento temporal para performance de leitura em ferramentas de análise.
* `storeId=R001` ➜ particionamento por loja para facilitar análise segmentada.
* `response.json` ➜ arquivo bruto da API, mantendo a estrutura original.

---

## 🔁 3. E se a resposta da API mudar? (ex: `taxes` → `taxation`)

### 📉 **Impactos:**

* **Falha em ETLs e transformações**
  Scripts e pipelines que esperam a chave `guestChecks.taxes` quebrarão.

* **Schema drift (deriva de esquema)**
  Dificulta manutenção e requer versionamento do schema de leitura.

* **Inconsistência nos dados históricos vs atuais**
  Dados anteriores usarão `taxes`, novos usarão `taxation`, dificultando análises uniformes.

### 🧠 **Soluções sugeridas:**

1. **Schema evolution consciente no Data Lake**
   Use ferramentas como Apache Iceberg, Delta Lake ou Glue para adaptar schemas.

2. **Pipeline resiliente ao schema**
   Validar esquema dinamicamente com `try-except`, `dict.get()` ou estruturas de mapeamento.

3. **Versão de schema no nome da pasta** (opcional):

   ```bash
   getGuestChecks_v2/
   ```

4. **Catalogação e validação com data contracts**
   Definir schemas em JSON Schema ou Avro + contratos em ferramentas como OpenAPI.

---

## 🛠️ Processo de Desenvolvimento

* 📌 **Input**: Resposta da API (`busDt`, `storeId`)
* ⏳ **Processo**: Armazenar `response.json` em estrutura versionada e particionada
* ✅ **Output**: Dados acessíveis para análise, históricos mantidos, com governança clara

---

## 🧪 Exemplo de Código Python (Armazenamento em S3)

```python
import boto3
import json
from datetime import date

s3 = boto3.client('s3')
bucket = 'data-lake'
store_id = 'R001'
today = date.today()

# Simulação de endpoint e resposta
endpoint = 'res/getGuestChecks'
payload = {"busDt": today.isoformat(), "storeId": store_id}
response = call_api(endpoint, payload)  # função fictícia

# Caminho particionado
key = f"restaurant_chain/raw/res/getGuestChecks/year={today.year}/month={today.month:02}/day={today.day:02}/storeId={store_id}/response.json"

# Upload para o S3
s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(response))
```