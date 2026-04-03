--upsert
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;


--bulk insert
CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],
    phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    temp_invalid TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]{10,}$' THEN
            CALL upsert_user(names[i], phones[i]);
        ELSE
            temp_invalid := array_append(temp_invalid, names[i] || ':' || phones[i]);
        END IF;
    END LOOP;

    invalid_data := temp_invalid;
END;
$$;


--delete
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$;