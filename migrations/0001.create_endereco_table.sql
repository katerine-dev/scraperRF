CREATE TABLE endereco (
   id                     SERIAL PRIMARY KEY,
   tipo_logradouro        TEXT,
   logradouro             TEXT,
   numero_logradouro      TEXT,
   complemento_logradouro TEXT,
   bairro                 TEXT,
   cep                    TEXT,
   uf                     TEXT,
   municipio              TEXT
);
