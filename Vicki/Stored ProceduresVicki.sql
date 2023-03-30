use Library;

-- stored procedure

delimiter //

create procedure SeeCustomers()
begin
select * from customer;
end //

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

-- search what has been loaned out since a certain date
delimiter //
create procedure OnLoanSince(
in DateFrom date)
begin
select loan_id, due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where DateFrom < due_back_date;
end //
delimiter ;

call OnLoanSince("2023-02-01");

-- search loan by first name and last name
delimiter //
create procedure SearchLoanByFirstAndLastName(
in FirstName varchar(70), LastName varchar(70))
begin
select loan_id, issue_date, due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where first_name = FirstName and last_name = LastName;
end //
delimiter ;
call SearchLoanByFirstAndLastName("Phil", "Brown");

-- search loan by due date
delimiter //
create procedure SearchByDueDate(
in DueDate date)
begin
select loan_id, due_back_date, album_name, first_name, last_name from loan_procedure join album on album_id = loan_album_id join customer on cust_id = loan_cust_id where due_back_date = DueDate;
end //
delimiter ;
call SearchByDueDate("2023-04-14")

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
delimiter ;
call spCustomer_check_history("Carl", "Turner");

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

call spCustomer_check_due("Vicki", "Gibbison");

-- for librarian to check on current loans
delimiter //
create procedure spLibrarian_loans_check()
begin
select loan_id, issue_date as "Loan date", due_back_date as "Due date", album_name as Album, concat(customer.first_name, " ", customer.last_name) as Customer
from loan_procedure left outer join customer on loan_cust_id = cust_id
join album on album_id = loan_album_id
where due_back_date > curdate() order by issue_date;
end //
delimiter ;
call spLibrarian_loans_check();



-- popularity of loan albums
delimiter //
create procedure spPopular_loan_album()
begin
select distinct album_name as Album, count(loan_album_id) as "Number of Loans" 
from loan_procedure join album on album_id = loan_album_id group by album_name order by count(loan_album_id) desc;
end //
delimiter ;

call spPopular_loan_album()







