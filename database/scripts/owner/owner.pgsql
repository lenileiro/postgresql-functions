CREATE TABLE IF NOT EXISTS store.owner (
            id SERIAL NOT NULL,
            national_id int NOT NULL PRIMARY KEY,
            name VARCHAR (20) NOT NULL,
            email VARCHAR (50) NOT NULL,
            phone VARCHAR (20) NOT NULL);