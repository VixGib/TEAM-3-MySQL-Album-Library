-- As a member I want to be able to:
--          -borrow an album
--          -search for an album by artist
--          -search for an album by album name
--          -view my history
--          -check my due dates
-- As the lending system I want top be able to:
--           -to see who is borrowing what
--           -to be able to contact a member
--           -find most popular album
--           -add a new album

use library;

-- member browse by artist
delimiter //
create procedure spCustomer_artist_browse()
begin
select if(first_name = last_name, last_name, concat(first_name, " ", last_name)) as artist, album_name as album 
from artist join album on art_id = artist_id order by artist;
end //

-- member browse by genre
delimiter //
create procedure spCustomer_genre_browse()
begin
select genre_name as Genre, if(first_name = last_name, last_name, concat(first_name, " ", last_name)) as Artist, album_name as Album  
from artist join album on art_id = artist_id join genre on genre_id = album_genre_id order by Genre;
end //

-- member search for a chosen album
delimiter //
create procedure spAlbum_search(
in album_choice varchar(70) )
begin
select album_name as Album, album_genre as Genre, album_year as "Album year" from album where lower(album_name) = lower(album_choice);
end //

-- to check history of chosen customer by first and last name
delimiter //
create procedure spCustomer_check_history(
in Customer_first_name varchar(20), Customer_last_name varchar(20) )
begin
select loan_id, issue_date, customer.first_name, customer.last_name, album_name
from loan_procedure left outer join customer on loan_cust_id = cust_id
join album on album_id = loan_album_id
where Customer_last_name = customer.last_name and Customer_first_name = customer.first_name
order by issue_date;
end //

-- for customer to check due date on current loans
delimiter //
create procedure spCustomer_check_due(
in Customer_first_name varchar(20), Customer_last_name varchar(20) )
begin
select loan_id, issue_date, due_back_date, album_name
from loan_procedure left outer join customer on loan_cust_id = cust_id
join album on album_id = loan_album_id
where Customer_last_name = customer.last_name and Customer_first_name = customer.first_name
and due_back_date > curdate() order by issue_date;
end //

-- for librarian to check on current loans
delimiter //
create procedure spLibrarian_loans_check()
begin
select loan_id, issue_date as "Loan date", due_back_date as "Due date", album_name as Album, concat(customer.first_name, " ", customer.last_name) as Customer
from loan_procedure left outer join customer on loan_cust_id = cust_id
join album on album_id = loan_album_id
where due_back_date > curdate() order by issue_date;
end //

-- customer borrow NOT WORKING GIVING ERROR SUBQUERY RETURNS MORE THAN ONE ROW
delimiter //
create procedure spCustomer_loan_album(
in Customer_name varchar(30), Album_name varchar(70) )
begin
insert into loan_procedure(issue_date, due_back_date, loan_cust_id, loan_album_id) 
values (curdate(), (curdate() + interval 3 week), 
(select cust_id from customer where Customer_name = concat(customer.first_name, " ", customer.last_name) limit 1),
(select album_id from album where Album_name = album_name limit 1) );
end //

-- select cust_id from customer where "Vicki Gibbison" = concat(customer.first_name, " ", customer.last_name)
-- select album_id from album where "Anti" = album_name

-- popularity of loan albums
delimiter //
create procedure spPopular_loan_album()
begin
select distinct album_name as Album, count(loan_album_id) as "Number of Loans" 
from loan_procedure join album on album_id = loan_album_id group by album_name order by count(loan_album_id) desc;
end //

delimiter ;
call spPopular_loan_album()

delimiter ;
call spLibrarian_loans_check();

delimiter ;
call spCustomer_loan_album("John Barnes", "Anti");

select * from loan_procedure;

delimiter ;
call spAlbum_search("True love");

delimiter ;
call spCustomer_check_history("Vicki", "Gibbison");

insert into loan_procedure values(15, 17, 6, "2023-03-01", "2023-03-22");
insert into loan_procedure values(16, 18, 6, "2023-03-10", "2023-03-31");
insert into loan_procedure values(17, 19, 6, "2023-03-26", "2023-04-16");

delimiter ;
call spCustomer_check_due("Vicki", "Gibbison");

delimiter ;
call spCustomer_artist_browse()

delimiter ;
call spCustomer_genre_browse()