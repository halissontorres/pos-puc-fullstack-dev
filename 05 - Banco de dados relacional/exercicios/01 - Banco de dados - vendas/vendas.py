import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine('sqlite:///vendas.db')
base = orm.declarative_base()


class Cliente(base):
    """Modelo de dados do cliente"""
    __tablename__ = 'cliente'

    cpf = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1), nullable=False)
    salario = sa.Column(sa.DECIMAL(10, 2))
    dia_mes_aniversario = sa.Column(sa.CHAR(1))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

class Fornecedor(base):
    """Modelo de dados do fornecedor"""
    __tablename__ = 'fornecedor'

    registro_fornecedor = sa.Column(sa.Integer, primary_key=True, index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(50), nullable=False, index=True)
    razao_social = sa.Column(sa.VARCHAR(50), nullable=False, index=True)
    cnpj = sa.Column(sa.CHAR(18), nullable=False, index=True)
    telefone = sa.Column(sa.CHAR(15), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    bairro = sa.Column(sa.VARCHAR(50), nullable=False)
    cidade = sa.Column(sa.VARCHAR(50), nullable=False)
    uf = sa.Column(sa.CHAR(2), nullable=False)

class Produto(base):
    """Modelo de dados do produto"""
    __tablename__ = 'produto'

    codigo_barras = sa.Column(sa.CHAR(13), primary_key=True, index=True)
    registro_fornecedor = sa.Column(sa.Integer, sa.ForeignKey('fornecedor.registro_fornecedor', ondelete='NO ACTION', onupdate='CASCADE'), nullable=False)
    descProduto = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1), nullable=False)

class Vendedor(base):
    """Modelo de dados do vendedor"""
    __tablename__ = 'vendedor'

    registro_vendedor = sa.Column(sa.Integer, primary_key=True, index=True)
    cpf = sa.Column(sa.VARCHAR(14), nullable=False)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    genero = sa.Column(sa.CHAR(1), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)

class Vendas(base):
    """Modelo de dados das vendas"""
    __tablename__ = 'vendas'

    idTransacao = sa.Column(sa.Integer, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey('cliente.cpf', ondelete='NO ACTION', onupdate='CASCADE'), nullable=False)
    registro_vendedor = sa.Column(sa.Integer, sa.ForeignKey('vendedor.registro_vendedor', ondelete='NO ACTION'), nullable=False)
    codigo_barras = sa.Column(sa.CHAR(13), sa.ForeignKey('produto.codigo_barras',ondelete='NO ACTION'), nullable=False)
    quantidade = sa.Column(sa.Integer, nullable=False)
    valor_unitario = sa.Column(sa.DECIMAL(10, 2), nullable=False)
    valor_total = sa.Column(sa.DECIMAL(10, 2), nullable=False)

try:
    print('Aguardando a criação do banco de dados...')
    base.metadata.create_all(engine, checkfirst=True)
    print('Tabelas criadas com sucesso!')
    session = orm.Session(bind=engine)
    session.close()
except Exception as e:
    print(f'Erro ao criar as tabelas: {e}')