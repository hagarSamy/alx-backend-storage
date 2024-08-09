-- a SQL script that creates an index idx_name_first on the table names and the first letter of name

ALTER TABLE names
ADD name CHAR(1) AS (LEFT(name, 1)) VIRTUAL;
CREATE INDEX idx_name_first
ON names (name);
