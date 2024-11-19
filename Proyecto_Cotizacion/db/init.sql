CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE ventanas (
    id SERIAL PRIMARY KEY,
    alto FLOAT NOT NULL,
    ancho FLOAT NOT NULL,
    precio FLOAT NOT NULL
);
