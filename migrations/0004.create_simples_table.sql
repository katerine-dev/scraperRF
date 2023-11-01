CREATE TYPE TIPO_OPCAO_SIMPLES AS ENUM('sim', 'nao', 'vazio');
CREATE TYPE TIPO_OPCAO_MEI AS ENUM('sim', 'nao', 'vazio');

CREATE TABLE simples (
   id                    SERIAL PRIMARY KEY,
   cnpj                  TEXT,
   opcao_simples         TIPO_OPCAO_SIMPLES,
   data_opcao_simples    DATE,
   data_exclusao_simples DATE,
   opcao_mei             TIPO_OPCAO_MEI,
   data_opcao_mei        DATE,
   data_exclusao_mei     TEXT
);
