use Library;
-- SP for displaying all customer details
delimiter //

create procedure SeeCustomers()
begin
select * from customer;
end //

delimiter ;

call SeeCustomers;

-- SP for searching by nationality
delimiter //
create procedure SearchByNationality(
in Nationality varchar(70) )
begin 
select * from artist where nationality = Nationality;
end //
delimiter ;

call SearchByNationality("English");

-- SP for searching by Postcode Area
delimiter //
create procedure SearchByPostcodeArea(
in AreaCode varchar(4) )
begin 
select * from customer where postcode like concat(AreaCode,'%');
end //
delimiter ;

call SearchByPostcodeArea("WF");
call SearchByPostcodeArea("LS");

-- Search loan details by first name and last name
delimiter //
create procedure SearchLoanByFirstAndLastName(
in FirstName varchar(70), LastName varchar(70))
begin
select loan_id, issue_date, due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where first_name = FirstName and last_name = LastName ;
end //
delimiter ;
call SearchLoanByFirstAndLastName("Phil", "Brown");

-- search loans by due date
delimiter //
create procedure SearchByDueDate(
in DueDate date)
begin
select loan_id, due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where due_back_date = DueDate;
end //
delimiter ;
call SearchByDueDate("2023-04-14")

-- search what has been loaned out since a certain date
delimiter //
create procedure OnLoanSince(
in DateFrom date)
begin
select loan_id, due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where DateFrom < due_back_date;
end //
delimiter ;
call OnLoanSince("2023-02-01")