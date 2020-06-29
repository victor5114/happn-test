-- Query 1 : Indiquer par pays, le nombre de clients qui n’ont pas effectué de commandes.
SELECT "Country", count("Country") FROM (
    SELECT
    custs."CustomerID",
    custs."Country",
    count(ords."OrderID") as order_count
    FROM [Customers] AS custs
    LEFT JOIN [Orders] AS ords ON ords."CustomerID" = custs."CustomerID"
    GROUP BY custs."CustomerID", custs."Country" HAVING order_count = 0)
GROUP BY country



-- Query 2 : Indiquer l’id produit ainsi que la somme des quantités achetées pour ce produit.
SELECT odets."ProductID", SUM(odets."Quantity") AS product_sum_quantity
FROM [Orders] AS ords
INNER JOIN [OrderDetails] AS odets ON ords."OrderID" = odets."OrderID"
GROUP BY odets."ProductID"

-- Query 3 : Indiquer la moyenne des années de naissance des employés arrondi à l’entier le plus proche.
SELECT ROUND(AVG(emp."BirthDate")) AS avg_age_of_employees FROM [Employees] AS emp

-- Query 4 : Indiquer les ville et leur pays respectif ainsi que leur nombre de clients dont le nombre de clients est strictement supérieur à 3.
SELECT city, country, count(CustomerID) AS unique_cust FROM [Customers] GROUP BY city, country HAVING unique_cust > 3