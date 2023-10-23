--
-- depends:

CREATE TABLE endereco (
   id                     SERIAL PRIMARY KEY,
   tipo_logradouro        TEXT,
   logradouro             TEXT,
   numero_logradouro      TEXT,
   complemento_logradouro TEXT,
   bairro                 TEXT,
   cep                    TEXT,
   uf                     TEXT,
   municipio              TEXT,
   start_dt               TEXT,
   end_dt                 TEXT,
   row_status_id          TEXT,
   updated_dt             TEXT,
);

-- [...]

   [...]
   WHEN MATCHED THEN
UPDATE
   SET T1.end_dt         =  CASE WHEN t1.tipo_logradouro <> T2.tipo_logradouro
                              OR T1.logradouro <> T2.logradouro
                              THEN GETDATE()
                              ELSE T1.end_dt
                              END,
        T1.row_status_id =  CASE WHEN t1.tipo_logradouro <> T2.tipo_logradouro
                              OR T1.logradouro <> T2.logradouro
                              THEN GETDATE()
                              ELSE T1.end_dt
                              END,
      T1. [...]