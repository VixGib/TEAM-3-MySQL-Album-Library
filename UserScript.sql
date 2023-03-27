-- creating users
create user customer@localhost identified by 'password';
create user librarian@localhost identified by 'password';

-- access rights for customer
grant select on library.album to customer@localhost;
grant select on library.artist to customer@localhost;
grant select on library.genre to customer@localhost;
grant select on library.record_label to customer@localhost;
grant select on library.loan_procedure to customer@localhost;
grant insert on library.loan_procedure to customer@localhost;

-- access rights for librarian
grant select on library.album to librarian@localhost;
grant select on library.artist to librarian@localhost;
grant select on library.genre to librarian@localhost;
grant select on library.record_label to librarian@localhost;
grant select on library.loan_procedure to librarian@localhost;
grant select on library.customer to librarian@localhost;
grant insert on library.album to librarian@localhost;
grant insert on library.artist to librarian@localhost;
grant insert on library.genre to librarian@localhost;
grant insert on library.record_label to librarian@localhost;
grant insert on library.loan_procedure to librarian@localhost;
grant insert on library.customer to librarian@localhost;
grant update on library.* to librarian@localhost;
