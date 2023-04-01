use Library;
-- user stories for library member
-- look up all American artists
select first_name, last_name from artist where nationality = 'American';

select album_name from album where record_label_id=1;

-- look up albums from before 1980
select album_name, first_name, last_name from album join artist on artist_id=art_id where album_year < 1980;

-- look up artists whose first name starts with 'P'
select first_name, last_name from artist where first_name like 'P%';

-- look up all due dates with customer name and album loaned
select due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id;
-- look up due date with id 8
select due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where loan_id = 8;
-- look up due date of loans by first_name and last_name
select due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where first_name = "Vicki" and last_name = "Gibbison";

-- borrow an album (using album name instead of album id)
insert into loan_procedure (loan_album_id, loan_cust_id, issue_date, due_back_date) 
select album_id, 3, "2023-03-24", "2023-04-14" from album where album_name = "Working my way back to you";

insert into loan_procedure (loan_album_id, loan_cust_id, issue_date, due_back_date) 
select album_id, 3, "2023-03-24", "2023-04-14" from album where album_name = "Gold Rush Kid";

-- borrow an album using album name and customer name
insert into loan_procedure (loan_album_id, loan_cust_id, issue_date, due_back_date) 
select album_id, cust_id, "2023-03-26", "2023-04-16" from album, customer where album_name = "Fun House" and first_name = "Carl" and last_name = "Brooks";

-- user story for library staff
-- add a new member to the library
insert into customer (first_name, last_name, email, mobile_num, address, postcode, join_date) values ("Bobby", "Brooks", "bobby@email.com", "07865234541", "3 Buttercup Crescent", "WF3 5DF", "05-08-19");

-- add a new album with existing artist
insert into album (album_name, artist_id, album_genre_id, record_label_id, album_year) values ("Trustfall", 6, 1, 7, 2023);

-- add a new album with new artist (Spice Girls)
insert into artist (first_name, last_name, nationality) values ("Spice Girls", "Spice Girls", "English");
insert into album (album_name, artist_id, album_genre_id, record_label_id, album_year) values ("Spice Girls", 13, 1, 9, 1996);

-- loan out an album
insert into loan_procedure (loan_album_id, loan_cust_id, issue_date, due_back_date) values (5, 7, "23-03-24", "23-04-14");

-- update customer name
update customer set last_name = "Brooks" where cust_id = 1;

-- update customer address
update customer set address = "24 Jackson close", postcode =  "SK8 7UR" where cust_id = 6;

-- Change customer mobile number
update customer set mobile_num = "07968497722" where cust_id = 6;

-- renew a loan
update loan_procedure set due_back_date = "23-04-14" where loan_id = 7;

-- delete a customer... we can't delete a customer that has ever borrowed anything without deleting loan history.
-- suggestion... have a membership active column on customer table and rather than deleting a customer we can disactivate their membership


