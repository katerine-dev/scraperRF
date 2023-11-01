CREATE TYPE TIPO_ESTABELECIMENTO AS ENUM('matriz', 'filial');
CREATE TYPE TIPO_CODIGO_SITUACAO_CADASTRAL AS ENUM('01', '02', '03', '04', '08');
CREATE TYPE TIPO_NOME_SITUACAO_CADASTRAL AS ENUM('NULA', 'ATIVA', 'SUSPENSA', 'INAPTA', 'BAIXADA');

CREATE TABLE estabelecimento (
   id                               SERIAL PRIMARY KEY,
   id_endereco                      INT REFERENCES endereco(id), -- FOREIGN KEY
   CNPJ                             VARCHAR (14) NOT NULL,
   tipo_estabelecimento             TIPO_ESTABELECIMENTO NOT NULL,
   nome_fantasia                    TEXT,
   codigo_situacao_cadastral        TIPO_CODIGO_SITUACAO_CADASTRAL,
   nome_situacao_cadastral          TIPO_NOME_SITUACAO_CADASTRAL,
   data_situacao_cadastral          DATE,
   codigo_motivo_situacao_cadastral TEXT,
   nome_cidade_exterior             TEXT,
   codigo_pais                      TEXT,
   data_inicio_atividade            DATE,
   cnae_fiscal_principal            TEXT,
   cnae_fiscal_secundaria           TEXT,
   ddd_telefone_1                   TEXT,
   telefone_1                       TEXT,
   ddd_telefone_2                   TEXT,
   telefone_2                       TEXT,
   ddd_fax                          TEXT,
   fax_numero                       TEXT,
   email                            TEXT,
   situacao_especial                TEXT,
   data_situacao_especial           DATE
);

