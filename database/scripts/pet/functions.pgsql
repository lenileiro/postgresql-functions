CREATE OR REPLACE FUNCTION find_pets(_id INT)
RETURNS TABLE (name text, age int ) AS
$$
SELECT pet.name, pet.age FROM store.owner as owner inner join store.pet as pet on owner.national_id=pet.owner_id where owner.national_id=_id
$$
LANGUAGE 'sql' STABLE;