CREATE TABLE IF NOT EXISTS store.pet (
            id SERIAL NOT NULL,
            pet_id int NOT NULL PRIMARY KEY,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            owner_id INT NOT NULL,
            FOREIGN KEY (owner_id) REFERENCES store.owner(national_id) ON DELETE CASCADE 
            );