CREATE DATABASE oubt_day4_db;

USE oubt_day4_db;

-- Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(50),
    Country VARCHAR(50)
);

INSERT INTO Customers VALUES
(1, 'Likhith', 'likhith@gmail.com', 'USA'),
(2, 'Sasank', 'sasank@gmail.com', 'India'),
(3, 'Venkat', 'venkat@yahoo.com', 'Canada'),
(4, 'Durga', 'durga@gmail.com', 'UK'),
(5, 'Yuvraj', 'yuvraj@hotmail.com', 'USA');

-- Products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);

INSERT INTO Products VALUES
(1, 'iPad', 'Electronics', 999.00),
(2, 'Whey Protein', 'Health', 49.99),
(3, 'Ring', 'Accessories', 199.00),
(4, 'Gaming PC', 'Electronics', 1800.00),
(5, 'Jacket', 'Apparel', 120.00);

-- Orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders VALUES
(1, 1, '2025-10-01', 1048.99),
(2, 2, '2025-10-03', 2199.00),
(3, 3, '2025-10-05', 1800.00),
(4, 4, '2025-10-08', 120.00),
(5, 5, '2025-10-10', 999.00);



CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO OrderDetails VALUES
(1, 1, 2, 1),
(2, 1, 5, 1),
(3, 2, 1, 1),
(4, 2, 3, 2),
(5, 3, 4, 1),
(6, 4, 5, 1),
(7, 5, 1, 1);
