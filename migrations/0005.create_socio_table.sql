CREATE TYPE TIPO_IDENTIFICADOR_SOCIO AS ENUM('pessoa_juridica', 'pessoa_fisica', 'estrangeiro');

CREATE TABLE socio (
   id                               SERIAL PRIMARY KEY,
   cnpj                             TIPO_IDENTIFICADOR_SOCIO,
   nome_ou_razao_social             TEXT,
   cnpj_cpf                         TEXT,
   qualificacao_socio               TEXT,
   data_entrada_sociedade           DATE,
   pais                             TEXT,
   nome_representante_legal         TEXT,
   qualificacao_representante_legal TEXT,
   faixa_etaria                     TEXT
);
