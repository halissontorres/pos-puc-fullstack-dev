import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm

import vendas as vd

# Pasta raiz
path_dados = '/home/halisson/Downloads/Dados_Exemplo/'

# Arquivo
vendedor_file = pd.read_csv(path_dados + 'vendedor.csv', sep=';')
vendedorDF = pd.DataFrame(vendedor_file)

# Engine
engine = sa.create_engine('sqlite:///vendas.db')
base = orm.declarative_base()

# Sessão
sessao = orm.sessionmaker(bind=engine)()


for i in range(len(vendedorDF)):
    dados_vendedor = vd.Vendedor(
        registro_vendedor = int(vendedorDF['registro_vendedor'][i]),
        cpf = vendedorDF['cpf'][i],
        nome = vendedorDF['nome'][i],
        genero = vendedorDF['genero'][i],
        email = vendedorDF['email'][i],
    )
    try:
        sessao.add(dados_vendedor)
        sessao.commit()
        print(f'Vendedor {dados_vendedor.nome} cadastrado com sucesso!')
    except ValueError as e:
        sessao.rollback()
        ValueError(f'Erro ao cadastrar o vendedor: {e}')

sessao.close()


#Algoritmo para inserção de dados, utilziando o DataFrame tbProduto

#variavel com o nome do arquivo
produto = pd.read_excel(path_dados + "produto.xlsx")

#Coleta os dados do arquivo para dentro do Python
tbProduto = pd.DataFrame(produto)

#######################
# PRODUTO
#######################
#Criando um conexão variável de congit stxão com o BD
conn = engine.connect()

#Variável de definição de metadados, para identificar que estrutura será atualizada
metadata = sa.schema.MetaData(bind=engine)

#Algoritmo para inserção de dados, utilziando o DataFrame tbProduto
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
DadosProduto = tbProduto.to_dict(orient='records')

#Variável que representa a tabela que se deseja inserir os dados e, um metadados.
tabela_produto = sa.Table(vd.produto.__tablename__, metadata, autoload=True) #na classe que representa a tabela de ocorrências

#Inserindo dados a partir de uma conexão com a engrenagem de BD
try:
    conn.execute(tabela_produto.insert(), DadosProduto)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbProduto criada!")

sessao.close_all()
print("Módulo de inserção de dados finalizado!")


