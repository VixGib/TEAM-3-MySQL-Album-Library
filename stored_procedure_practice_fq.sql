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