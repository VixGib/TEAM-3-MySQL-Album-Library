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
-- Add a new customer
insert into customer(first_name, last_name, email, mobile_num, address, postcode, join_date) 
values ("Georgia", "Gibbison", "georgiagibbison@email.com", "07936728022", "25 Brown Street", "SK8 6YT", "2023-03-24");
-- Add new Album(existing artist)
insert into album(album_name, artist_id, album_genre_id, record_label_id, album_year)
values ("Greatest Hits.....So Far!!!", 6, 1, 8, 2010);
-- Add new Album from new artist
insert into artist(first_name, last_name, nationality)
values("Craig", "David", "English");
insert into record_label(label_name)
values("Wildstar Records");
insert into album(album_name, artist_id, album_genre_id, record_label_id, album_year)
values ("Born to Do It", 13, 7, 18, 2000);
-- Add new loan procedure
insert into loan_procedure(loan_album_id, loan_cust_id, issue_date, due_back_date)
values (21, 6, "2023-03-24", "2023-04-14");
-- Change customer email
update customer set email = "vickigibbison@email.com" where cust_id = 6;
-- Change customer address and postcode
update customer set address = "24 Jackson close", postcode =  "SK8 7UR" where cust_id = 6;
-- Change customer mobile number
update customer set mobile_num = "07968497722" where cust_id = 6;
-- Update customer loan due back date  y customer id
update loan_procedure set due_back_date = "2023-04-29" where loan_cust_id = 6;
-- Delete a loan procedure
delete from loan_procedure where loan_cust_id = 6;
-- Delete a customer
delete from customer where cust_id = 10;
-- stored procedure

delimiter //

create procedure SeeCustomers()
begin
select * from customer;
end //

call SeeCustomers;

delemiter //
create procedure SearchLoanByFirstAndLastName(
in FirstName varchar(70), LastName varchar(70))
begin
select * from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where first_name = FirstName and last_name = LastName ;
end //

call SearchLoanByFirstAndLastName("Phil", "Brown");

 










