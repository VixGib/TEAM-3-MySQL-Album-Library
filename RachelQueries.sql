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
select if(first_name = last_name, last_name, concat(first_name, " ", last_name)) as artist, album_name as album 
from artist join album on art_id = artist_id order by artist;

-- member browse by genre
select genre_name as Genre, if(first_name = last_name, last_name, concat(first_name, " ", last_name)) as Artist, album_name as Album  
from artist join album on art_id = artist_id join genre on genre_id = album_genre_id order by Genre;

-- member search for a chosen album
delimiter //
create procedure spAlbum_search(
in album_choice varchar(70) )
begin
select album_name, album_genre, album_year from album where lower(album_name) = lower(album_choice);
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

delimiter ;
call spAlbum_search("True love");

delimiter ;
call spCustomer_check_history("Vicki", "Gibbison");

insert into loan_procedure values(15, 17, 6, "2023-03-01", "2023-03-22");
insert into loan_procedure values(16, 18, 6, "2023-03-10", "2023-03-31");
insert into loan_procedure values(17, 19, 6, "2023-03-26", "2023-04-16");

delimiter ;
call spCustomer_check_due("Vicki", "Gibbison");