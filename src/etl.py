# importei as bibliotecas necessárias mediante estudos para a praticidade e eficiência do código
# uni todo os arquivos csv em um dicionário, criando uma chave para cada arquivo
# criei um dicionário para armazenar os dataframes, removendo duplicatas
# com a biblioteca sqlalchemy, criei a engine de conexão com o banco de dados PostgreSQL e subi as tabelas para o banco de dados
# com a progressão dos estudos identifiquei a necessidade de utilizar a biblioteca dotenv para armazenar as credenciais do banco de dados em um arquivo .env, evitando expor informações sensíveis no código na hora de subir o projeto para o GitHub, garantindo a segurança das informações sensíveis e facilitando a manutenção do código.

import pandas as pd
import sqlalchemy as sa
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

arquivos = {
        'clientes': BASE_DIR / 'data' / 'olist_customers_dataset.csv',
        'produtos': BASE_DIR / 'data' / 'olist_products_dataset.csv',
        'pedidos': BASE_DIR / 'data' / 'olist_orders_dataset.csv',
        'itens_pedidos': BASE_DIR / 'data' / 'olist_order_items_dataset.csv',
        'pagamentos': BASE_DIR / 'data' / 'olist_order_payments_dataset.csv',
        'avaliacoes': BASE_DIR / 'data' / 'olist_order_reviews_dataset.csv',
        'vendedores': BASE_DIR / 'data' / 'olist_sellers_dataset.csv',
        'categorias': BASE_DIR / 'data' / 'product_category_name_translation.csv',
        'localizacoes': BASE_DIR / 'data' / 'olist_geolocation_dataset.csv'
}

tabelas = {}
for nome, caminho in arquivos.items():

    df = pd.read_csv(caminho)
    tabelas[nome] = df.drop_duplicates()


engine = sa.create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

for nome, df in tabelas.items():
    df.to_sql(nome, engine, if_exists='replace', index=False)

print("Tabelas carregadas:", list(tabelas.keys()))