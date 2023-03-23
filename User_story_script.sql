use Library;
-- look up all American artists
select first_name, last_name from artist where nationality = "American";
-- look up album before 1980
select album_name, first_name, last_name from album join artist on artist_id = art_id where album_year < 1980;
-- look up artist where first name begins with p
select first_name, last_name from artist where first_name like 'p%';
-- look up all due dates with customer name and album loaned
select due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id;
-- look up due date with id 8
select due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where loan_id = 8;
-- look up due date of loans by first_name and last_name
select due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where first_name = "Vicki" and last_name = "Gibbison";
