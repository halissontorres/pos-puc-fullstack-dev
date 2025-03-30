import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine('sqlite:///ocorrencias.db')
base = orm.declarative_base()

class DelegaciaPolicia(base):
    """Modelo de dados da delegacia policial"""
    __tablename__ = 'delegacia_policia'

    codigo = sa.Column(sa.Integer, primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    endereco = sa.Column(sa.VARCHAR(200), nullable=False)

class ResponsavelDelegacia(base):
    """Modelo de dados responsável pela delegacia policial"""
    __tablename__ = 'responsavel_delegacia'

    codigo_delegacia = sa.Column(sa.Integer, sa.ForeignKey('delegacia_policia.codigo', ondelete='NO ACTION'), primary_key=True, index=True)
    delegado = sa.Column(sa.VARCHAR(100), nullable=False, index=True)
    telefone = sa.Column(sa.CHAR(15), nullable=False)

class Municipio(base):
    """Modelo de dados responsável pelo Município"""
    __tablename__ = 'municipio'

    codIBGE = sa.Column(sa.Integer, primary_key=True, index=True)
    municipio = sa.Column(sa.VARCHAR(200), nullable=False)
    regiao = sa.Column(sa.VARCHAR(25), nullable=False)

class Ocorrencia(base):
    """Modelo de dados responsável pelas ocorrências"""

    __tablename__ = 'ocorrencia'
    idRegistro = sa.Column(sa.BigInteger, primary_key=True, index=True)
    codigo_delegacia = sa.Column(sa.Integer, sa.ForeignKey('delegacia_policia.codigo', ondelete='NO ACTION', onupdate='CASCADE'), nullable=False)
    codigo_municipio = sa.Column(sa.Integer, sa.ForeignKey('municipio.codIBGE', ondelete='NO ACTION', onupdate='CASCADE'), nullable=False)
    tipo_ocorrencia = sa.Column(sa.VARCHAR(50), nullable=False)
    descricao_ocorrencia = sa.Column(sa.VARCHAR(200), nullable=False)
    data_ocorrencia = sa.Column(sa.DATE, nullable=False)
    hora_ocorrencia = sa.Column(sa.TIME, nullable=False)


try:
    print('Aguardando a criação do banco de dados...')
    base.metadata.create_all(engine, checkfirst=True)
    print('Tabelas criadas com sucesso!')
    session = orm.Session(bind=engine)
    session.close()
except Exception as e:
    print(f'Erro ao criar as tabelas: {e}')