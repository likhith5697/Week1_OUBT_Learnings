SELECT * FROM Customers WHERE Country = 'USA';

-- List all products under $500
SELECT ProductName, Price FROM Products WHERE Price < 500;

--  Count total number of orders
SELECT COUNT(*) AS TotalOrders FROM Orders;

--  Get all orders for customer 'Likhith'
SELECT o.OrderID, o.OrderDate, o.TotalAmount FROM Orders o JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Name = 'Likhith';





--  Total spent by each customer
SELECT c.Name, SUM(o.TotalAmount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.Name;

--  List all orders with product names
SELECT o.OrderID, c.Name AS CustomerName, p.ProductName, od.Quantity
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID;

--  Find top 2 customers by spending
SELECT c.Name, SUM(o.TotalAmount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.Name
ORDER BY TotalSpent DESC
LIMIT 2;

--  Find products never ordered
SELECT p.ProductName
FROM Products p
LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID
WHERE od.ProductID IS NULL;

--  Average order amount per country
SELECT c.Country, AVG(o.TotalAmount) AS AvgOrderAmount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.Country;


