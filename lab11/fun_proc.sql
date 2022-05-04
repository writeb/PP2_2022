create table phone(
    first_name varchar(100),
    num varchar(100)
);
drop table phone;

-- Updating procedure
create or replace procedure update(firrst_name varchar, numm varchar)
as
$$
begin
    update phone
    set num = $2
    where first_name = $1;
end;
$$ language plpgsql;

-- Inserting procedure
create or replace procedure insert(first_name varchar, num varchar)
as
$$
begin
    insert into phone(first_name, num) values ($1, $2);
end;
$$ language plpgsql;

-- Deleting procedure
create or replace procedure delete(data varchar)
as
$$
begin
    delete from phone where first_name = $1  or num = $1;
end;
$$ language plpgsql;

-- Querying function
create or replace function querying(data varchar(100))
    returns table
        (
        first_namee varchar(100),
        numm varchar(100)
        )
as
$$
begin
    return query
    select * from phone where first_name ilike $1 or num ilike $1;
end;
$$ language plpgsql;