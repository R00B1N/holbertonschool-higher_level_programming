-- a script that lists all records with a score >= 10
-- in the current database in the MySQL server
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
