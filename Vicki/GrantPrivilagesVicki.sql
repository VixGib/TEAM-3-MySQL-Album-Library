use Library;

-- create customer local host and privilages

-- Customer
create user customer@localhost identified by 'password';

grant select on Library.album to customer@localhost;
grant select on Library.artist to customer@localhost;
grant select on Library.genre to customer@localhost;
grant select on Library.record_label to customer@localhost;
grant select on Library.loan_procedure to customer@localhost;

grant insert on Library.loan_procedure to customer@localhost;

-- Staff
create user staff@localhost identified by 'password';

grant select on Library.* to staff@localhost;

grant insert on Library.* to staff@localhost;

grant update on Library.* to staff@localhost;

