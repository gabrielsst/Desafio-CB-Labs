
import json
import sqlite3
from pathlib import Path

# Carregando o arquivo JSON
json_path = Path("ERP.json")
with open(json_path, "r") as file:
    data = json.load(file)

# Criando o banco de dados SQLite
conn = sqlite3.connect("erp_restaurant.db")
cursor = conn.cursor()

# Criando as tabelas
cursor.executescript("""
DROP TABLE IF EXISTS guest_checks;
DROP TABLE IF EXISTS detail_lines;
DROP TABLE IF EXISTS menu_items;
DROP TABLE IF EXISTS taxes;

CREATE TABLE guest_checks (
    guestCheckId INTEGER PRIMARY KEY,
    chkNum INTEGER,
    opnBusDt TEXT,
    opnUTC TEXT,
    opnLcl TEXT,
    clsdBusDt TEXT,
    clsdUTC TEXT,
    clsdLcl TEXT,
    lastTransUTC TEXT,
    lastTransLcl TEXT,
    lastUpdatedUTC TEXT,
    lastUpdatedLcl TEXT,
    clsdFlag BOOLEAN,
    gstCnt INTEGER,
    subTtl REAL,
    nonTxblSlsTtl REAL,
    chkTtl REAL,
    dscTtl REAL,
    payTtl REAL,
    balDueTtl REAL,
    rvcNum INTEGER,
    otNum INTEGER,
    ocNum INTEGER,
    tblNum INTEGER,
    tblName TEXT,
    empNum INTEGER,
    numSrvcRd INTEGER,
    numChkPrntd INTEGER
);

CREATE TABLE taxes (
    guestCheckId INTEGER,
    taxNum INTEGER,
    txblSlsTtl REAL,
    taxCollTtl REAL,
    taxRate REAL,
    type INTEGER,
    FOREIGN KEY (guestCheckId) REFERENCES guest_checks(guestCheckId)
);

CREATE TABLE detail_lines (
    guestCheckLineItemId INTEGER PRIMARY KEY,
    guestCheckId INTEGER,
    rvcNum INTEGER,
    dtlOtNum INTEGER,
    dtlOcNum INTEGER,
    lineNum INTEGER,
    dtlId INTEGER,
    detailUTC TEXT,
    detailLcl TEXT,
    lastUpdateUTC TEXT,
    lastUpdateLcl TEXT,
    busDt TEXT,
    wsNum INTEGER,
    dspTtl REAL,
    dspQty INTEGER,
    aggTtl REAL,
    aggQty INTEGER,
    chkEmpId INTEGER,
    chkEmpNum INTEGER,
    svcRndNum INTEGER,
    seatNum INTEGER,
    FOREIGN KEY (guestCheckId) REFERENCES guest_checks(guestCheckId)
);

CREATE TABLE menu_items (
    guestCheckLineItemId INTEGER,
    miNum INTEGER,
    modFlag BOOLEAN,
    inclTax REAL,
    activeTaxes TEXT,
    prcLvl INTEGER,
    FOREIGN KEY (guestCheckLineItemId) REFERENCES detail_lines(guestCheckLineItemId)
);
""")

# Inserindo os dados nas tabelas
for guest_check in data["guestChecks"]:
    cursor.execute("""
        INSERT INTO guest_checks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        guest_check["guestCheckId"],
        guest_check["chkNum"],
        guest_check["opnBusDt"],
        guest_check["opnUTC"],
        guest_check["opnLcl"],
        guest_check["clsdBusDt"],
        guest_check["clsdUTC"],
        guest_check["clsdLcl"],
        guest_check["lastTransUTC"],
        guest_check["lastTransLcl"],
        guest_check["lastUpdatedUTC"],
        guest_check["lastUpdatedLcl"],
        guest_check["clsdFlag"],
        guest_check["gstCnt"],
        guest_check["subTtl"],
        guest_check["nonTxblSlsTtl"],
        guest_check["chkTtl"],
        guest_check["dscTtl"],
        guest_check["payTtl"],
        guest_check["balDueTtl"],
        guest_check["rvcNum"],
        guest_check["otNum"],
        guest_check["ocNum"],
        guest_check["tblNum"],
        guest_check["tblName"],
        guest_check["empNum"],
        guest_check["numSrvcRd"],
        guest_check["numChkPrntd"]
    ))

    for tax in guest_check.get("taxes", []):
        cursor.execute("""
            INSERT INTO taxes VALUES (?, ?, ?, ?, ?, ?)
        """, (
            guest_check["guestCheckId"],
            tax["taxNum"],
            tax["txblSlsTtl"],
            tax["taxCollTtl"],
            tax["taxRate"],
            tax["type"]
        ))

    for line in guest_check.get("detailLines", []):
        cursor.execute("""
            INSERT INTO detail_lines VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            line["guestCheckLineItemId"],
            guest_check["guestCheckId"],
            line["rvcNum"],
            line["dtlOtNum"],
            line["dtlOcNum"],
            line["lineNum"],
            line["dtlId"],
            line["detailUTC"],
            line["detailLcl"],
            line["lastUpdateUTC"],
            line["lastUpdateLcl"],
            line["busDt"],
            line["wsNum"],
            line["dspTtl"],
            line["dspQty"],
            line["aggTtl"],
            line["aggQty"],
            line["chkEmpId"],
            line["chkEmpNum"],
            line["svcRndNum"],
            line["seatNum"]
        ))

        menu_item = line["menuItem"]
        cursor.execute("""
            INSERT INTO menu_items VALUES (?, ?, ?, ?, ?, ?)
        """, (
            line["guestCheckLineItemId"],
            menu_item["miNum"],
            menu_item["modFlag"],
            menu_item["inclTax"],
            menu_item["activeTaxes"],
            menu_item["prcLvl"]
        ))

conn.commit()
conn.close()
print("Banco de dados criado com sucesso.")
