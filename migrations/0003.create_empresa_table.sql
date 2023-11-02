CREATE TYPE TIPO_PORTE_EMPRESA AS ENUM('nao_informado', 'micro_empresa', 'empresa_pequeno_porte', 'demais');

CREATE TABLE empresa (
   id                       SERIAL PRIMARY KEY,
   cnpj                     TEXT,
   nome_empresarial         TEXT,
   natureza_juridica        TEXT,
   qualificacao_responsavel TEXT,
   capital_social_empresa   TEXT,
   porte_empresa            TIPO_PORTE_EMPRESA,
   ente_federativo          TEXT
);
