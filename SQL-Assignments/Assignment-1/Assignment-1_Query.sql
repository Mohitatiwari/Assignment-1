use Assigment;

#1.Count the number of Salesperson whose name begin with ‘a’/’A’.
select * from salesPeople where sname like 'a%' or sname like 'A%';

#2.Display all the Salesperson whose all orders worth is more than Rs. 2000.
select SalesPeople.sname from SalesPeople join Orders on 
SalesPeople.snum  = Orders.snum
where Orders.amt>2000;

#3.Count the number of Salesperson belonging to Newyork.
select count(city_comm) from salespeople where city_comm like 'Newyork%';

#4.Display the number of Salespeople belonging to London and belonging to Paris
SELECT * FROM Salespeople WHERE city_comm like 'London%' OR city_comm like 'Paris%';






